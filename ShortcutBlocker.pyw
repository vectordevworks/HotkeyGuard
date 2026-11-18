import ctypes
import json
import math
import os
import tkinter as tk

from tkinter import ttk, messagebox
from ctypes import wintypes
from pathlib import Path

# Pillow isteğe bağlıdır.
try:
    from PIL import Image, ImageTk, ImageDraw
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False

# Sistem tepsisi desteği.
try:
    import pystray
    PYSTRAY_AVAILABLE = True
except ImportError:
    PYSTRAY_AVAILABLE = False


# ============================================================
# SHORTCUT BLOCKER - VECTORDEVWORKS
# ============================================================

if os.name != "nt":
    raise OSError("Bu program yalnızca Windows içindir.")


# ============================================================
# DOSYA YOLLARI
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

ICON_PATH = ASSETS_DIR / "icon.png"
LANGUAGE_ICON_PATH = ASSETS_DIR / "language.png"

CONFIG_DIR = Path.home() / ".vectordevworks" / "shortcut_blocker"
CONFIG_FILE = CONFIG_DIR / "config.json"


# ============================================================
# WINDOWS API
# ============================================================

user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)


# ============================================================
# SABİTLER
# ============================================================

WH_KEYBOARD_LL = 13

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105

HC_ACTION = 0

VK_SHIFT = 0x10
VK_LSHIFT = 0xA0
VK_RSHIFT = 0xA1
VK_DELETE = 0x2E
VK_F1 = 0x70

PROCESS_QUERY_LIMITED_INFORMATION = 0x1000

LRESULT = ctypes.c_ssize_t
HHOOK = wintypes.HANDLE


# ============================================================
# DİLLER
# ============================================================

LANGUAGES = {
    "tr": "Türkçe",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "pt": "Português",
    "ru": "Русский",
    "ja": "日本語",
    "zh-CN": "简体中文",
    "ko": "한국어"
}


APP_NAMES = {
    "tr": "Kısayol Engelleyici",
    "en": "Shortcut Blocker",
    "de": "Tastenkombinationsblocker",
    "fr": "Bloqueur de raccourcis",
    "es": "Bloqueador de atajos",
    "pt": "Bloqueador de atalhos",
    "ru": "Блокировщик сочетаний клавиш",
    "ja": "ショートカットブロッカー",
    "zh-CN": "快捷键拦截器",
    "ko": "단축키 차단기"
}


TRANSLATIONS = {

    "en": {
        "Bu program yalnızca Windows içindir.": "This program is only available for Windows.",
        "KISAYOL": "SHORTCUT",
        "ENGELLEYİCİ": "BLOCKER",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Developed exclusively for Windows.",
        "SİSTEM DURUMU": "SYSTEM STATUS",
        "Program durduruldu": "Program stopped",
        "Koruma şu anda etkin değil.": "Protection is currently inactive.",
        "KISAYOL AYARLARI": "SHORTCUT SETTINGS",
        "Kalıcı silme kısayolunu engeller.": "Blocks the permanent deletion shortcut.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Blocks the help window in browsers and File Explorer.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "The F1 key remains available in games and other applications.",
        "F1 ENGELLEME LİSTESİ": "F1 BLOCK LIST",
        "Windows Masaüstü  |  Dosya Gezgini": "Windows Desktop  |  File Explorer",
        "KORUMAYI BAŞLAT": "START PROTECTION",
        "DURDUR": "STOP",
        "vectordevworks tarafından geliştirilmiştir.": "Developed by vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Shortcut Blocker | Version 1.0.0",
        "Koruma etkin": "Protection enabled",
        "Seçilen kısayollar engelleniyor.": "Selected shortcuts are being blocked.",
        "Koruma durduruldu": "Protection stopped",
        "Klavye kısayolları artık engellenmiyor.": "Keyboard shortcuts are no longer being blocked.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Please enable at least one shortcut block.",
        "Başlatma Hatası": "Startup Error",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "The keyboard hook could not be installed.\n\nWindows error code: {error}",
        "Kısayol Engelleyici Hatası": "Shortcut Blocker Error",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "The keyboard hook could not be removed.\n\nWindows error code: {error}",
        "Dil": "Language"
    },

    "de": {
        "Bu program yalnızca Windows içindir.": "Dieses Programm ist nur für Windows verfügbar.",
        "KISAYOL": "TASTENKÜRZEL",
        "ENGELLEYİCİ": "BLOCKER",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Ausschließlich für Windows entwickelt.",
        "SİSTEM DURUMU": "SYSTEMSTATUS",
        "Program durduruldu": "Programm angehalten",
        "Koruma şu anda etkin değil.": "Der Schutz ist derzeit nicht aktiv.",
        "KISAYOL AYARLARI": "TASTENKÜRZEL-EINSTELLUNGEN",
        "Kalıcı silme kısayolunu engeller.": "Blockiert die Tastenkombination zum endgültigen Löschen.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Blockiert das Hilfefenster in Browsern und im Datei-Explorer.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "Die F1-Taste bleibt in Spielen und anderen Anwendungen verfügbar.",
        "F1 ENGELLEME LİSTESİ": "F1-BLOCKLISTE",
        "Windows Masaüstü  |  Dosya Gezgini": "Windows-Desktop  |  Datei-Explorer",
        "KORUMAYI BAŞLAT": "SCHUTZ STARTEN",
        "DURDUR": "STOPP",
        "vectordevworks tarafından geliştirilmiştir.": "Entwickelt von vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Tastenkombinationsblocker | Version 1.0.0",
        "Koruma etkin": "Schutz aktiviert",
        "Seçilen kısayollar engelleniyor.": "Die ausgewählten Tastenkombinationen werden blockiert.",
        "Koruma durduruldu": "Schutz angehalten",
        "Klavye kısayolları artık engellenmiyor.": "Tastenkombinationen werden nicht mehr blockiert.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Bitte aktivieren Sie mindestens eine Tastenkombinationssperre.",
        "Başlatma Hatası": "Startfehler",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "Der Tastatur-Hook konnte nicht installiert werden.\n\nWindows-Fehlercode: {error}",
        "Kısayol Engelleyici Hatası": "Tastenkombinationsblocker-Fehler",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "Der Tastatur-Hook konnte nicht entfernt werden.\n\nWindows-Fehlercode: {error}",
        "Dil": "Sprache"
    },

    "fr": {
        "Bu program yalnızca Windows içindir.": "Ce programme est uniquement disponible sous Windows.",
        "KISAYOL": "RACCOURCI",
        "ENGELLEYİCİ": "BLOQUEUR",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Développé exclusivement pour Windows.",
        "SİSTEM DURUMU": "ÉTAT DU SYSTÈME",
        "Program durduruldu": "Programme arrêté",
        "Koruma şu anda etkin değil.": "La protection est actuellement inactive.",
        "KISAYOL AYARLARI": "PARAMÈTRES DES RACCOURCIS",
        "Kalıcı silme kısayolunu engeller.": "Bloque le raccourci de suppression définitive.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Bloque la fenêtre d'aide des navigateurs et de l'Explorateur de fichiers.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "La touche F1 reste disponible dans les jeux et les autres applications.",
        "F1 ENGELLEME LİSTESİ": "LISTE DE BLOCAGE DE F1",
        "Windows Masaüstü  |  Dosya Gezgini": "Bureau Windows  |  Explorateur de fichiers",
        "KORUMAYI BAŞLAT": "ACTIVER LA PROTECTION",
        "DURDUR": "ARRÊTER",
        "vectordevworks tarafından geliştirilmiştir.": "Développé par vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Bloqueur de raccourcis | Version 1.0.0",
        "Koruma etkin": "Protection activée",
        "Seçilen kısayollar engelleniyor.": "Les raccourcis sélectionnés sont bloqués.",
        "Koruma durduruldu": "Protection arrêtée",
        "Klavye kısayolları artık engellenmiyor.": "Les raccourcis clavier ne sont plus bloqués.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Veuillez activer au moins un blocage de raccourci.",
        "Başlatma Hatası": "Erreur de démarrage",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "Le hook clavier n'a pas pu être installé.\n\nCode d'erreur Windows : {error}",
        "Kısayol Engelleyici Hatası": "Erreur du bloqueur de raccourcis",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "Le hook clavier n'a pas pu être supprimé.\n\nCode d'erreur Windows : {error}",
        "Dil": "Langue"
    },

    "es": {
        "Bu program yalnızca Windows içindir.": "Este programa solo está disponible para Windows.",
        "KISAYOL": "ATAJOS",
        "ENGELLEYİCİ": "BLOQUEADOR",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Desarrollado exclusivamente para Windows.",
        "SİSTEM DURUMU": "ESTADO DEL SISTEMA",
        "Program durduruldu": "Programa detenido",
        "Koruma şu anda etkin değil.": "La protección no está activa actualmente.",
        "KISAYOL AYARLARI": "AJUSTES DE ATAJOS",
        "Kalıcı silme kısayolunu engeller.": "Bloquea el atajo de eliminación permanente.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Bloquea la ventana de ayuda en navegadores y en el Explorador de archivos.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "La tecla F1 sigue disponible en juegos y otras aplicaciones.",
        "F1 ENGELLEME LİSTESİ": "LISTA DE BLOQUEO DE F1",
        "Windows Masaüstü  |  Dosya Gezgini": "Escritorio de Windows  |  Explorador de archivos",
        "KORUMAYI BAŞLAT": "INICIAR PROTECCIÓN",
        "DURDUR": "DETENER",
        "vectordevworks tarafından geliştirilmiştir.": "Desarrollado por vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Bloqueador de atajos | Versión 1.0.0",
        "Koruma etkin": "Protección activada",
        "Seçilen kısayollar engelleniyor.": "Se están bloqueando los atajos seleccionados.",
        "Koruma durduruldu": "Protección detenida",
        "Klavye kısayolları artık engellenmiyor.": "Los atajos de teclado ya no están bloqueados.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Activa al menos un bloqueo de atajo.",
        "Başlatma Hatası": "Error de inicio",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "No se pudo instalar el hook del teclado.\n\nCódigo de error de Windows: {error}",
        "Kısayol Engelleyici Hatası": "Error del bloqueador de atajos",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "No se pudo quitar el hook del teclado.\n\nCódigo de error de Windows: {error}",
        "Dil": "Idioma"
    },

    "pt": {
        "Bu program yalnızca Windows içindir.": "Este programa está disponível apenas para Windows.",
        "KISAYOL": "ATALHO",
        "ENGELLEYİCİ": "BLOQUEADOR",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Desenvolvido exclusivamente para Windows.",
        "SİSTEM DURUMU": "ESTADO DO SISTEMA",
        "Program durduruldu": "Programa parado",
        "Koruma şu anda etkin değil.": "A proteção não está ativa no momento.",
        "KISAYOL AYARLARI": "CONFIGURAÇÕES DE ATALHOS",
        "Kalıcı silme kısayolunu engeller.": "Bloqueia o atalho de exclusão permanente.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Bloqueia a janela de ajuda nos navegadores e no Explorador de Arquivos.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "A tecla F1 continua disponível em jogos e outros aplicativos.",
        "F1 ENGELLEME LİSTESİ": "LISTA DE BLOQUEIO DO F1",
        "Windows Masaüstü  |  Dosya Gezgini": "Área de Trabalho do Windows  |  Explorador de Arquivos",
        "KORUMAYI BAŞLAT": "INICIAR PROTEÇÃO",
        "DURDUR": "PARAR",
        "vectordevworks tarafından geliştirilmiştir.": "Desenvolvido por vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Bloqueador de atalhos | Versão 1.0.0",
        "Koruma etkin": "Proteção ativada",
        "Seçilen kısayollar engelleniyor.": "Os atalhos selecionados estão sendo bloqueados.",
        "Koruma durduruldu": "Proteção parada",
        "Klavye kısayolları artık engellenmiyor.": "Os atalhos do teclado não estão mais sendo bloqueados.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Ative pelo menos um bloqueio de atalho.",
        "Başlatma Hatası": "Erro ao iniciar",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "Não foi possível instalar o hook do teclado.\n\nCódigo de erro do Windows: {error}",
        "Kısayol Engelleyici Hatası": "Erro do bloqueador de atalhos",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "Não foi possível remover o hook do teclado.\n\nCódigo de erro do Windows: {error}",
        "Dil": "Idioma"
    },

    "ru": {
        "Bu program yalnızca Windows içindir.": "Эта программа предназначена только для Windows.",
        "KISAYOL": "СОЧЕТАНИЯ",
        "ENGELLEYİCİ": "КЛАВИШ",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Разработано исключительно для Windows.",
        "SİSTEM DURUMU": "СОСТОЯНИЕ СИСТЕМЫ",
        "Program durduruldu": "Программа остановлена",
        "Koruma şu anda etkin değil.": "Защита сейчас не активна.",
        "KISAYOL AYARLARI": "НАСТРОЙКИ СОЧЕТАНИЙ",
        "Kalıcı silme kısayolunu engeller.": "Блокирует сочетание клавиш для окончательного удаления.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "Блокирует окно справки в браузерах и Проводнике.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "Клавиша F1 доступна в играх и других приложениях.",
        "F1 ENGELLEME LİSTESİ": "СПИСОК БЛОКИРОВКИ F1",
        "Windows Masaüstü  |  Dosya Gezgini": "Рабочий стол Windows  |  Проводник",
        "KORUMAYI BAŞLAT": "ВКЛЮЧИТЬ ЗАЩИТУ",
        "DURDUR": "ОСТАНОВИТЬ",
        "vectordevworks tarafından geliştirilmiştir.": "Разработано vectordevworks.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "Блокировщик сочетаний клавиш | Версия 1.0.0",
        "Koruma etkin": "Защита включена",
        "Seçilen kısayollar engelleniyor.": "Выбранные сочетания клавиш блокируются.",
        "Koruma durduruldu": "Защита остановлена",
        "Klavye kısayolları artık engellenmiyor.": "Сочетания клавиш больше не блокируются.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "Включите хотя бы одну блокировку сочетаний клавиш.",
        "Başlatma Hatası": "Ошибка запуска",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "Не удалось установить клавиатурный перехватчик.\n\nКод ошибки Windows: {error}",
        "Kısayol Engelleyici Hatası": "Ошибка блокировщика сочетаний клавиш",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "Не удалось удалить клавиатурный перехватчик.\n\nКод ошибки Windows: {error}",
        "Dil": "Язык"
    },

    "ja": {
        "Bu program yalnızca Windows içindir.": "このプログラムは Windows 専用です。",
        "KISAYOL": "ショートカット",
        "ENGELLEYİCİ": "ブロッカー",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Windows 専用に開発されています。",
        "SİSTEM DURUMU": "システム状態",
        "Program durduruldu": "プログラムは停止中です",
        "Koruma şu anda etkin değil.": "保護は現在無効です。",
        "KISAYOL AYARLARI": "ショートカット設定",
        "Kalıcı silme kısayolunu engeller.": "完全削除のショートカットをブロックします。",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "ブラウザーとエクスプローラーのヘルプ画面をブロックします。",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "ゲームやその他のアプリでは F1 キーを使用できます。",
        "F1 ENGELLEME LİSTESİ": "F1 ブロック対象",
        "Windows Masaüstü  |  Dosya Gezgini": "Windows デスクトップ  |  エクスプローラー",
        "KORUMAYI BAŞLAT": "保護を開始",
        "DURDUR": "停止",
        "vectordevworks tarafından geliştirilmiştir.": "vectordevworks によって開発されました。",
        "Kısayol Engelleyici | Sürüm 1.0.0": "ショートカットブロッカー | バージョン 1.0.0",
        "Koruma etkin": "保護は有効です",
        "Seçilen kısayollar engelleniyor.": "選択したショートカットをブロックしています。",
        "Koruma durduruldu": "保護は停止しました",
        "Klavye kısayolları artık engellenmiyor.": "キーボードショートカットはブロックされていません。",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "少なくとも 1 つのショートカットブロックを有効にしてください。",
        "Başlatma Hatası": "起動エラー",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "キーボードフックを設定できませんでした。\n\nWindows エラーコード: {error}",
        "Kısayol Engelleyici Hatası": "ショートカットブロッカーのエラー",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "キーボードフックを解除できませんでした。\n\nWindows エラーコード: {error}",
        "Dil": "言語"
    },

    "zh-CN": {
        "Bu program yalnızca Windows içindir.": "此程序仅适用于 Windows。",
        "KISAYOL": "快捷键",
        "ENGELLEYİCİ": "拦截器",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "专为 Windows 系统开发。",
        "SİSTEM DURUMU": "系统状态",
        "Program durduruldu": "程序已停止",
        "Koruma şu anda etkin değil.": "当前未启用保护。",
        "KISAYOL AYARLARI": "快捷键设置",
        "Kalıcı silme kısayolunu engeller.": "拦截永久删除快捷键。",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "拦截浏览器和文件资源管理器中的帮助窗口。",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "在游戏和其他应用中，F1 键仍可正常使用。",
        "F1 ENGELLEME LİSTESİ": "F1 拦截列表",
        "Windows Masaüstü  |  Dosya Gezgini": "Windows 桌面  |  文件资源管理器",
        "KORUMAYI BAŞLAT": "启动保护",
        "DURDUR": "停止",
        "vectordevworks tarafından geliştirilmiştir.": "由 vectordevworks 开发。",
        "Kısayol Engelleyici | Sürüm 1.0.0": "快捷键拦截器 | 版本 1.0.0",
        "Koruma etkin": "保护已启用",
        "Seçilen kısayollar engelleniyor.": "正在拦截所选快捷键。",
        "Koruma durduruldu": "保护已停止",
        "Klavye kısayolları artık engellenmiyor.": "键盘快捷键不再被拦截。",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "请至少启用一项快捷键拦截。",
        "Başlatma Hatası": "启动错误",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "无法安装键盘钩子。\n\nWindows 错误代码：{error}",
        "Kısayol Engelleyici Hatası": "快捷键拦截器错误",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "无法移除键盘钩子。\n\nWindows 错误代码：{error}",
        "Dil": "语言"
    },

    "ko": {
        "Bu program yalnızca Windows içindir.": "이 프로그램은 Windows 전용입니다.",
        "KISAYOL": "단축키",
        "ENGELLEYİCİ": "차단기",
        "Yalnızca Windows işletim sistemi için geliştirilmiştir.": "Windows 전용으로 개발되었습니다.",
        "SİSTEM DURUMU": "시스템 상태",
        "Program durduruldu": "프로그램 중지됨",
        "Koruma şu anda etkin değil.": "현재 보호 기능이 비활성화되어 있습니다.",
        "KISAYOL AYARLARI": "단축키 설정",
        "Kalıcı silme kısayolunu engeller.": "영구 삭제 단축키를 차단합니다.",
        "Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller.": "브라우저와 파일 탐색기의 도움말 창을 차단합니다.",
        "Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir.": "게임 및 기타 앱에서는 F1 키를 사용할 수 있습니다.",
        "F1 ENGELLEME LİSTESİ": "F1 차단 목록",
        "Windows Masaüstü  |  Dosya Gezgini": "Windows 바탕 화면  |  파일 탐색기",
        "KORUMAYI BAŞLAT": "보호 시작",
        "DURDUR": "중지",
        "vectordevworks tarafından geliştirilmiştir.": "vectordevworks에서 개발했습니다.",
        "Kısayol Engelleyici | Sürüm 1.0.0": "단축키 차단기 | 버전 1.0.0",
        "Koruma etkin": "보호 활성화됨",
        "Seçilen kısayollar engelleniyor.": "선택한 단축키를 차단하고 있습니다.",
        "Koruma durduruldu": "보호 중지됨",
        "Klavye kısayolları artık engellenmiyor.": "키보드 단축키가 더 이상 차단되지 않습니다.",
        "Lütfen en az bir kısayol engelini etkinleştirin.": "하나 이상의 단축키 차단을 활성화하세요.",
        "Başlatma Hatası": "시작 오류",
        "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}": "키보드 후크를 설치하지 못했습니다.\n\nWindows 오류 코드: {error}",
        "Kısayol Engelleyici Hatası": "단축키 차단기 오류",
        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}": "키보드 후크를 제거하지 못했습니다.\n\nWindows 오류 코드: {error}",
        "Dil": "언어"
    }
}


# ============================================================
# KLAVYE YAPISI
# ============================================================

class KBDLLHOOKSTRUCT(ctypes.Structure):

    _fields_ = [
        ("vkCode", wintypes.DWORD),
        ("scanCode", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_size_t)
    ]


HOOKPROC = ctypes.WINFUNCTYPE(
    LRESULT,
    ctypes.c_int,
    wintypes.WPARAM,
    wintypes.LPARAM
)


# ============================================================
# API TANIMLAMALARI
# ============================================================

user32.GetForegroundWindow.restype = wintypes.HWND

user32.GetWindowThreadProcessId.argtypes = [
    wintypes.HWND,
    ctypes.POINTER(wintypes.DWORD)
]

user32.GetWindowThreadProcessId.restype = wintypes.DWORD

kernel32.OpenProcess.argtypes = [
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD
]

kernel32.OpenProcess.restype = wintypes.HANDLE

kernel32.QueryFullProcessImageNameW.argtypes = [
    wintypes.HANDLE,
    wintypes.DWORD,
    wintypes.LPWSTR,
    ctypes.POINTER(wintypes.DWORD)
]

kernel32.QueryFullProcessImageNameW.restype = wintypes.BOOL

kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.CloseHandle.restype = wintypes.BOOL

kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
kernel32.GetModuleHandleW.restype = wintypes.HMODULE

user32.SetWindowsHookExW.argtypes = [
    ctypes.c_int,
    HOOKPROC,
    wintypes.HINSTANCE,
    wintypes.DWORD
]

user32.SetWindowsHookExW.restype = HHOOK

user32.UnhookWindowsHookEx.argtypes = [HHOOK]
user32.UnhookWindowsHookEx.restype = wintypes.BOOL

user32.CallNextHookEx.argtypes = [
    HHOOK,
    ctypes.c_int,
    wintypes.WPARAM,
    wintypes.LPARAM
]

user32.CallNextHookEx.restype = LRESULT


# ============================================================
# AYARLAR
# ============================================================

BLOCKED_APPS = {
    "chrome.exe",
    "msedge.exe",
    "firefox.exe",
    "brave.exe",
    "opera.exe",
    "explorer.exe"
}


# ============================================================
# GLOBAL DEĞİŞKENLER
# ============================================================

hook = None
callback_reference = None

block_delete = True
block_f1 = True

blocked_keys = set()
pressed_shifts = set()


# ============================================================
# AKTİF UYGULAMA
# ============================================================

def get_foreground_process():

    hwnd = user32.GetForegroundWindow()

    if not hwnd:
        return None

    process_id = wintypes.DWORD()

    user32.GetWindowThreadProcessId(
        hwnd,
        ctypes.byref(process_id)
    )

    if not process_id.value:
        return None

    process = kernel32.OpenProcess(
        PROCESS_QUERY_LIMITED_INFORMATION,
        False,
        process_id.value
    )

    if not process:
        return None

    try:

        buffer = ctypes.create_unicode_buffer(1024)
        size = wintypes.DWORD(len(buffer))

        result = kernel32.QueryFullProcessImageNameW(
            process,
            0,
            buffer,
            ctypes.byref(size)
        )

        if result:
            return os.path.basename(buffer.value).lower()

    finally:
        kernel32.CloseHandle(process)

    return None


# ============================================================
# KLAVYE KONTROLÜ
# ============================================================

def keyboard_callback(nCode, wParam, lParam):

    try:

        if nCode == HC_ACTION:

            event = ctypes.cast(
                lParam,
                ctypes.POINTER(KBDLLHOOKSTRUCT)
            ).contents

            key = event.vkCode

            key_down = wParam in (
                WM_KEYDOWN,
                WM_SYSKEYDOWN
            )

            key_up = wParam in (
                WM_KEYUP,
                WM_SYSKEYUP
            )

            if key_down:

                if key in (VK_SHIFT, VK_LSHIFT, VK_RSHIFT):
                    pressed_shifts.add(key)

                # Shift + Delete
                if (
                    block_delete
                    and key == VK_DELETE
                    and pressed_shifts
                ):
                    blocked_keys.add(key)
                    return 1

                # Uygulamaya göre F1
                if block_f1 and key == VK_F1:

                    process = get_foreground_process()

                    if process in BLOCKED_APPS:
                        blocked_keys.add(key)
                        return 1

            elif key_up:

                if key in (VK_SHIFT, VK_LSHIFT, VK_RSHIFT):
                    pressed_shifts.discard(key)

                if key in blocked_keys:
                    blocked_keys.discard(key)
                    return 1

    except Exception:
        pass

    return user32.CallNextHookEx(
        hook,
        nCode,
        wParam,
        lParam
    )


# ============================================================
# ANA UYGULAMA
# ============================================================

class ShortcutBlocker:

    def __init__(self, root):

        self.root = root
        self.language = self.load_language()

        self.window_icon = None
        self.language_icon = None

        self.language_menu_window = None
        self.language_menu_after_id = None

        self.setting_checkbuttons = []

        self.tray_icon = None
        self.is_minimized_to_tray = False
        self.is_closing = False

        self.root.title(APP_NAMES[self.language])
        self.root.geometry("620x700")
        self.root.minsize(400, 400)
        self.root.configure(bg="#10131B")

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

        self.root.bind(
            "<Unmap>",
            self.on_window_minimize
        )

        self.load_window_icon()
        self.create_variables()
        self.create_styles()
        self.create_scrollable_interface()

    # --------------------------------------------------------
    # DİL VE YAPILANDIRMA
    # --------------------------------------------------------

    def tr(self, text):

        if self.language == "tr":
            return text

        return TRANSLATIONS.get(
            self.language, {}
        ).get(text, text)

    def load_language(self):

        try:

            if CONFIG_FILE.exists():

                with CONFIG_FILE.open(
                    "r",
                    encoding="utf-8"
                ) as file:

                    config = json.load(file)

                language = config.get("language", "tr")

                if language in LANGUAGES:
                    return language

        except (
            OSError,
            json.JSONDecodeError,
            AttributeError,
            TypeError
        ):
            pass

        return "tr"

    def save_language(self):

        try:

            CONFIG_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            with CONFIG_FILE.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    {"language": self.language},
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError as error:
            print(f"Configuration save error: {error}")

    def set_language(self, language):

        if language not in LANGUAGES:
            return

        self.close_language_menu()

        if language == self.language:
            return

        delete_value = self.delete_var.get()
        f1_value = self.f1_var.get()

        self.language = language
        self.save_language()

        self.root.title(APP_NAMES[self.language])

        # Eski MouseWheel bağlantısını kaldır.
        self.canvas.unbind_all("<MouseWheel>")

        # Eski arayüzü temizle.
        for widget in self.root.winfo_children():
            widget.destroy()

        self.setting_checkbuttons.clear()

        # Yeni dilde arayüzü oluştur.
        self.create_scrollable_interface()

        # Ayarları koru.
        self.delete_var.set(delete_value)
        self.f1_var.set(f1_value)

        # Koruma durumunu koru.
        if hook:

            self.status_var.set(
                self.tr("Koruma etkin")
            )

            self.status_detail.set(
                self.tr("Seçilen kısayollar engelleniyor.")
            )

            self.status_label.config(fg="#4ADE80")
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

            self.set_settings_state("disabled")

        else:

            self.status_var.set(
                self.tr("Program durduruldu")
            )

            self.status_detail.set(
                self.tr("Koruma şu anda etkin değil.")
            )

            self.status_label.config(fg="#F87171")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

            self.set_settings_state("normal")

    def load_window_icon(self):

        try:

            if ICON_PATH.is_file():

                self.window_icon = tk.PhotoImage(
                    file=str(ICON_PATH)
                )

                self.root.iconphoto(
                    True,
                    self.window_icon
                )

        except (tk.TclError, OSError) as error:

            print(f"Window icon loading error: {error}")
            self.window_icon = None

    # --------------------------------------------------------
    # DEĞİŞKENLER
    # --------------------------------------------------------

    def create_variables(self):

        self.delete_var = tk.BooleanVar(value=True)
        self.f1_var = tk.BooleanVar(value=True)

        self.status_var = tk.StringVar(
            value=self.tr("Program durduruldu")
        )

        self.status_detail = tk.StringVar(
            value=self.tr("Koruma şu anda etkin değil.")
        )

    # --------------------------------------------------------
    # TASARIM
    # --------------------------------------------------------

    def create_styles(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "TCheckbutton",
            background="#202633",
            foreground="#E5E7EB",
            font=("Segoe UI", 10),
            padding=5,
            borderwidth=0,
            relief="flat",
            focuscolor="#202633"
        )

        style.map(
            "TCheckbutton",
            background=[
                ("active", "#202633"),
                ("disabled", "#202633")
            ],
            foreground=[
                ("disabled", "#777777")
            ],
            focuscolor=[
                ("focus", "#202633")
            ]
        )

        style.configure(
            "Vertical.TScrollbar",
            background="#30394A",
            troughcolor="#10131B",
            bordercolor="#10131B",
            lightcolor="#30394A",
            darkcolor="#30394A",
            arrowcolor="#AAB4C5",
            relief="flat",
            borderwidth=0,
            width=10
        )

        style.map(
            "Vertical.TScrollbar",
            background=[
                ("active", "#55A6FF"),
                ("pressed", "#2878D0")
            ],
            arrowcolor=[
                ("active", "#FFFFFF")
            ]
        )

    def create_card(self, parent):

        return tk.Frame(
            parent,
            bg="#202633",
            bd=0,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#30394A",
            highlightcolor="#30394A",
            relief="flat"
        )

    # --------------------------------------------------------
    # KAYDIRILABİLİR ARAYÜZ
    # --------------------------------------------------------

    def create_scrollable_interface(self):

        top_bar = tk.Frame(
            self.root,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        top_bar.pack(
            fill="x",
            padx=20,
            pady=(10, 0)
        )

        self.language_button = tk.Button(
            top_bar,
            text=self.tr("Dil"),
            image=self.get_language_icon(),
            compound="left",
            command=self.show_language_menu,
            bg="#202633",
            fg="#E5E7EB",
            activebackground="#30394A",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 9),
            relief="flat",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            takefocus=False,
            padx=10,
            pady=5,
            anchor="center"
        )

        self.language_button.pack(side="right")

        container = tk.Frame(
            self.root,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        container.pack(
            fill="both",
            expand=True
        )

        self.canvas = tk.Canvas(
            container,
            bg="#10131B",
            highlightthickness=0,
            borderwidth=0,
            bd=0,
            relief="flat"
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview,
            style="Vertical.TScrollbar"
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.content_frame = tk.Frame(
            self.canvas,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.content_frame,
            anchor="nw"
        )

        self.content_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        self.canvas.bind(
            "<Configure>",
            self.update_canvas_width
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.on_mousewheel
        )

        self.create_interface()

    # --------------------------------------------------------
    # DİL İKONU
    # --------------------------------------------------------

    def get_language_icon(self):

        try:

            if not LANGUAGE_ICON_PATH.is_file():

                self.language_icon = None
                return ""

            if PILLOW_AVAILABLE:

                with Image.open(LANGUAGE_ICON_PATH) as source:

                    source = source.convert("RGBA")

                    source.thumbnail(
                        (20, 20),
                        Image.Resampling.LANCZOS
                    )

                    image = Image.new(
                        "RGBA",
                        (20, 20),
                        (0, 0, 0, 0)
                    )

                    x = (20 - source.width) // 2
                    y = (20 - source.height) // 2

                    image.alpha_composite(
                        source,
                        (x, y)
                    )

                    self.language_icon = ImageTk.PhotoImage(image)

                return self.language_icon

            image = tk.PhotoImage(
                file=str(LANGUAGE_ICON_PATH)
            )

            width = image.width()
            height = image.height()

            factor = max(
                1,
                math.ceil(max(width, height) / 20)
            )

            if factor > 1:
                image = image.subsample(factor, factor)

            self.language_icon = image

            return self.language_icon

        except (tk.TclError, OSError, ValueError) as error:

            print(f"Language icon loading error: {error}")

            self.language_icon = None
            return ""

    # --------------------------------------------------------
    # DİL MENÜSÜ
    # --------------------------------------------------------

    def close_language_menu(self):

        menu = self.language_menu_window

        if menu is None:
            return

        self.language_menu_window = None

        if self.language_menu_after_id is not None:

            try:
                self.root.after_cancel(
                    self.language_menu_after_id
                )
            except tk.TclError:
                pass

            self.language_menu_after_id = None

        try:

            if menu.winfo_exists():

                try:
                    menu.grab_release()
                except tk.TclError:
                    pass

                menu.destroy()

        except tk.TclError:
            pass

    def show_language_menu(self):

        if self.language_menu_window is not None:
            self.close_language_menu()
            return

        menu = tk.Toplevel(self.root)

        self.language_menu_window = menu

        menu.overrideredirect(True)

        menu.configure(
            bg="#30394A",
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        menu.transient(self.root)

        outer_frame = tk.Frame(
            menu,
            bg="#30394A",
            bd=0,
            highlightthickness=0,
            relief="flat"
        )

        outer_frame.pack(
            fill="both",
            expand=True,
            padx=1,
            pady=1
        )

        inner_frame = tk.Frame(
            outer_frame,
            bg="#202633",
            bd=0,
            highlightthickness=0
        )

        inner_frame.pack(
            fill="both",
            expand=True
        )

        for code, name in LANGUAGES.items():

            selected = code == self.language

            background = "#2878D0" if selected else "#202633"
            foreground = "#FFFFFF" if selected else "#E5E7EB"

            prefix = "✓  " if selected else "   "

            button = tk.Button(
                inner_frame,
                text=prefix + name,
                command=lambda selected_code=code: self.set_language(
                    selected_code
                ),
                bg=background,
                fg=foreground,
                activebackground="#2878D0",
                activeforeground="#FFFFFF",
                font=("Segoe UI", 9),
                relief="flat",
                bd=0,
                borderwidth=0,
                highlightthickness=0,
                cursor="hand2",
                takefocus=False,
                anchor="w",
                padx=12,
                pady=6
            )

            button.pack(
                fill="x",
                padx=2,
                pady=1
            )

            if not selected:

                button.bind(
                    "<Enter>",
                    lambda event, widget=button: widget.configure(
                        bg="#2878D0",
                        fg="#FFFFFF"
                    )
                )

                button.bind(
                    "<Leave>",
                    lambda event, widget=button: widget.configure(
                        bg="#202633",
                        fg="#E5E7EB"
                    )
                )

        menu.update_idletasks()

        menu_width = max(
            155,
            menu.winfo_reqwidth()
        )

        menu_height = menu.winfo_reqheight()

        button_x = self.language_button.winfo_rootx()

        button_y = (
            self.language_button.winfo_rooty()
            + self.language_button.winfo_height()
        )

        screen_width = menu.winfo_screenwidth()
        screen_height = menu.winfo_screenheight()

        if button_x + menu_width > screen_width:
            button_x = screen_width - menu_width - 5

        if button_y + menu_height > screen_height:
            button_y = (
                self.language_button.winfo_rooty()
                - menu_height
            )

        button_x = max(0, button_x)
        button_y = max(0, button_y)

        menu.geometry(
            f"{menu_width}x{menu_height}+{button_x}+{button_y}"
        )

        menu.bind(
            "<Escape>",
            lambda event: self.close_language_menu()
        )

        menu.bind(
            "<ButtonPress-1>",
            self.on_language_menu_click,
            add="+"
        )

        menu.bind(
            "<FocusOut>",
            self.on_language_menu_focus_out
        )

        menu.deiconify()
        menu.lift()
        menu.focus_force()

        try:
            menu.grab_set()
        except tk.TclError:
            pass

    def on_language_menu_click(self, event):

        menu = self.language_menu_window

        if menu is None:
            return

        try:

            if not menu.winfo_exists():
                return

            click_x = event.x_root
            click_y = event.y_root

            menu_left = menu.winfo_rootx()
            menu_top = menu.winfo_rooty()

            menu_right = menu_left + menu.winfo_width()
            menu_bottom = menu_top + menu.winfo_height()

            outside_menu = not (
                menu_left <= click_x < menu_right
                and menu_top <= click_y < menu_bottom
            )

            if outside_menu:
                self.close_language_menu()

        except tk.TclError:
            self.close_language_menu()

    def on_language_menu_focus_out(self, event):

        menu = self.language_menu_window

        if menu is None:
            return

        if self.language_menu_after_id is not None:

            try:
                self.root.after_cancel(
                    self.language_menu_after_id
                )
            except tk.TclError:
                pass

        try:

            self.language_menu_after_id = self.root.after(
                150,
                self.check_language_menu_focus,
                menu
            )

        except tk.TclError:
            self.language_menu_after_id = None

    def check_language_menu_focus(self, expected_menu):

        self.language_menu_after_id = None

        if self.language_menu_window is not expected_menu:
            return

        menu = self.language_menu_window

        if menu is None:
            return

        try:

            if not menu.winfo_exists():
                self.language_menu_window = None
                return

            focused = menu.focus_get()

            if focused is None:
                self.close_language_menu()

        except tk.TclError:
            self.close_language_menu()

    # --------------------------------------------------------
    # KAYDIRMA KONTROLLERİ
    # --------------------------------------------------------

    def update_scroll_region(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def update_canvas_width(self, event):

        self.canvas.itemconfigure(
            self.canvas_window,
            width=event.width
        )

    def on_mousewheel(self, event):

        if not self.canvas.winfo_exists():
            return

        if event.delta:

            self.canvas.yview_scroll(
                -int(event.delta / 120),
                "units"
            )

    # --------------------------------------------------------
    # ARAYÜZ
    # --------------------------------------------------------

    def create_interface(self):

        header = tk.Frame(
            self.content_frame,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(20, 15)
        )

        tk.Label(
            header,
            text=self.tr("KISAYOL"),
            font=("Segoe UI", 25, "bold"),
            fg="#FFFFFF",
            bg="#10131B",
            bd=0,
            highlightthickness=0
        ).pack(anchor="w")

        tk.Label(
            header,
            text=self.tr("ENGELLEYİCİ"),
            font=("Segoe UI", 25, "bold"),
            fg="#55A6FF",
            bg="#10131B",
            bd=0,
            highlightthickness=0
        ).pack(anchor="w")

        tk.Label(
            header,
            text=self.tr("Yalnızca Windows işletim sistemi için geliştirilmiştir."),
            font=("Segoe UI", 9),
            fg="#8290A5",
            bg="#10131B",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # DURUM KARTI
        status_card = self.create_card(self.content_frame)

        status_card.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            status_card,
            text=self.tr("SİSTEM DURUMU"),
            font=("Segoe UI", 9, "bold"),
            fg="#8290A5",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.status_label = tk.Label(
            status_card,
            textvariable=self.status_var,
            font=("Segoe UI", 17, "bold"),
            fg="#F87171",
            bg="#202633",
            bd=0,
            highlightthickness=0
        )

        self.status_label.pack(
            anchor="w",
            padx=20
        )

        tk.Label(
            status_card,
            textvariable=self.status_detail,
            font=("Segoe UI", 9),
            fg="#AAB4C5",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 17)
        )

        # KISAYOL AYARLARI
        settings_card = self.create_card(self.content_frame)

        settings_card.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            settings_card,
            text=self.tr("KISAYOL AYARLARI"),
            font=("Segoe UI", 10, "bold"),
            fg="#FFFFFF",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 12)
        )

        self.create_setting(
            settings_card,
            "Shift + Delete",
            self.tr("Kalıcı silme kısayolunu engeller."),
            self.delete_var
        )

        self.create_setting(
            settings_card,
            "F1",
            self.tr("Tarayıcılarda ve Dosya Gezgini'nde yardım penceresini engeller."),
            self.f1_var
        )

        tk.Label(
            settings_card,
            text=self.tr("Oyunlarda ve diğer uygulamalarda F1 tuşu serbesttir."),
            font=("Segoe UI", 8),
            fg="#8290A5",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(3, 17)
        )

        # UYGULAMA LİSTESİ
        apps_card = self.create_card(self.content_frame)

        apps_card.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            apps_card,
            text=self.tr("F1 ENGELLEME LİSTESİ"),
            font=("Segoe UI", 10, "bold"),
            fg="#FFFFFF",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 8)
        )

        tk.Label(
            apps_card,
            text="Chrome  |  Edge  |  Firefox  |  Brave  |  Opera",
            font=("Segoe UI", 9),
            fg="#AAB4C5",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        tk.Label(
            apps_card,
            text=self.tr("Windows Masaüstü  |  Dosya Gezgini"),
            font=("Segoe UI", 9),
            fg="#AAB4C5",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # BUTONLAR
        buttons = tk.Frame(
            self.content_frame,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        buttons.pack(
            fill="x",
            padx=30,
            pady=18
        )

        self.start_button = tk.Button(
            buttons,
            text=self.tr("KORUMAYI BAŞLAT"),
            command=self.start,
            bg="#2878D0",
            fg="#FFFFFF",
            activebackground="#398CE8",
            activeforeground="#FFFFFF",
            disabledforeground="#AAB4C5",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            takefocus=False,
            pady=12
        )

        self.start_button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 7)
        )

        self.stop_button = tk.Button(
            buttons,
            text=self.tr("DURDUR"),
            command=self.stop,
            bg="#343D4D",
            fg="#FFFFFF",
            activebackground="#455166",
            activeforeground="#FFFFFF",
            disabledforeground="#AAB4C5",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            takefocus=False,
            pady=12,
            state="disabled"
        )

        self.stop_button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(7, 0)
        )

        # ALT BİLGİ
        footer = tk.Frame(
            self.content_frame,
            bg="#10131B",
            bd=0,
            highlightthickness=0
        )

        footer.pack(
            fill="x",
            pady=(0, 18)
        )

        tk.Label(
            footer,
            text=self.tr("vectordevworks tarafından geliştirilmiştir."),
            font=("Segoe UI", 9, "bold"),
            fg="#55A6FF",
            bg="#10131B",
            bd=0,
            highlightthickness=0
        ).pack()

        tk.Label(
            footer,
            text=self.tr("Kısayol Engelleyici | Sürüm 1.0.0"),
            font=("Segoe UI", 8),
            fg="#657187",
            bg="#10131B",
            bd=0,
            highlightthickness=0
        ).pack(pady=(3, 0))

    # --------------------------------------------------------
    # AYAR SATIRI
    # --------------------------------------------------------

    def create_setting(
        self,
        parent,
        title,
        description,
        variable
    ):

        row = tk.Frame(
            parent,
            bg="#202633",
            bd=0,
            highlightthickness=0
        )

        row.pack(
            fill="x",
            padx=20,
            pady=7
        )

        left = tk.Frame(
            row,
            bg="#202633",
            bd=0,
            highlightthickness=0
        )

        left.pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Label(
            left,
            text=title,
            font=("Segoe UI", 11, "bold"),
            fg="#FFFFFF",
            bg="#202633",
            bd=0,
            highlightthickness=0
        ).pack(anchor="w")

        tk.Label(
            left,
            text=description,
            font=("Segoe UI", 8),
            fg="#9AA6B8",
            bg="#202633",
            wraplength=390,
            justify="left",
            bd=0,
            highlightthickness=0
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        checkbutton = ttk.Checkbutton(
            row,
            variable=variable,
            takefocus=False
        )

        checkbutton.pack(
            side="right",
            padx=5
        )

        self.setting_checkbuttons.append(checkbutton)

    def set_settings_state(self, state):

        for checkbutton in self.setting_checkbuttons:
            checkbutton.configure(state=state)

    # --------------------------------------------------------
    # SİSTEM TEPSİSİ
    # --------------------------------------------------------

    def get_tray_image(self):

        if not PILLOW_AVAILABLE:
            raise RuntimeError(
                "Sistem tepsisi için Pillow gereklidir."
            )

        # Önce assets/icon.png dosyasını kullan.
        try:

            if ICON_PATH.is_file():

                with Image.open(ICON_PATH) as source:

                    source = source.convert("RGBA")

                    # Görselin oranını koruyarak 256x256 alana sığdır.
                    source.thumbnail(
                        (256, 256),
                        Image.Resampling.LANCZOS
                    )

                    # Her zaman 256x256 şeffaf tuval oluştur.
                    image = Image.new(
                        "RGBA",
                        (256, 256),
                        (0, 0, 0, 0)
                    )

                    # Görseli tuvalin ortasına yerleştir.
                    x = (256 - source.width) // 2
                    y = (256 - source.height) // 2

                    image.alpha_composite(
                        source,
                        (x, y)
                    )

                    return image

        except (OSError, ValueError) as error:

            print(f"Tray icon loading error: {error}")

        # Simge dosyası bulunamazsa varsayılan simge oluştur.
        image = Image.new(
            "RGBA",
            (256, 256),
            (16, 19, 27, 255)
        )

        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle(
            (16, 16, 240, 240),
            radius=52,
            fill=(40, 120, 208, 255)
        )

        draw.text(
            (105, 82),
            "V",
            fill=(255, 255, 255, 255)
        )

        return image

    def get_tray_menu_labels(self):

        labels = {
            "tr": ("Aç", "Çıkış"),
            "en": ("Open", "Exit"),
            "de": ("Öffnen", "Beenden"),
            "fr": ("Ouvrir", "Quitter"),
            "es": ("Abrir", "Salir"),
            "pt": ("Abrir", "Sair"),
            "ru": ("Открыть", "Выход"),
            "ja": ("開く", "終了"),
            "zh-CN": ("打开", "退出"),
            "ko": ("열기", "종료")
        }

        return labels.get(
            self.language,
            ("Aç", "Çıkış")
        )

    def on_window_minimize(self, event=None):

        try:

            if self.root.state() != "iconic":
                return

        except tk.TclError:
            return

        if self.is_closing:
            return

        self.close_language_menu()

        try:
            self.root.after(0, self.minimize_to_tray)
        except tk.TclError:
            pass

    def minimize_to_tray(self):

        if self.is_closing:
            return

        if self.tray_icon is not None:
            return

        if not PYSTRAY_AVAILABLE or not PILLOW_AVAILABLE:

            messagebox.showwarning(
                APP_NAMES[self.language],
                "Sistem tepsisi özelliği için pystray ve Pillow gereklidir.",
                parent=self.root
            )

            self.root.deiconify()
            self.root.state("normal")

            return

        tray = None

        try:

            image = self.get_tray_image()

            open_label, exit_label = self.get_tray_menu_labels()

            menu = pystray.Menu(
                pystray.MenuItem(
                    open_label,
                    self.restore_from_tray,
                    default=True
                ),
                pystray.MenuItem(
                    exit_label,
                    self.exit_from_tray
                )
            )

            tray = pystray.Icon(
                "VectorDevWorksShortcutBlocker",
                image,
                APP_NAMES[self.language],
                menu
            )

            self.tray_icon = tray
            self.is_minimized_to_tray = True

            self.root.withdraw()

            tray.run_detached()

        except Exception as error:

            if tray is not None:

                try:
                    tray.stop()
                except Exception:
                    pass

            self.tray_icon = None
            self.is_minimized_to_tray = False

            try:
                self.root.deiconify()
                self.root.state("normal")
            except tk.TclError:
                pass

            messagebox.showerror(
                APP_NAMES[self.language],
                f"Sistem tepsisine küçültme başarısız oldu:\n\n{error}",
                parent=self.root
            )

    def restore_from_tray(self, icon=None, item=None):

        try:
            self.root.after(0, self.restore_window)
        except tk.TclError:
            pass

    def restore_window(self):

        if self.is_closing:
            return

        tray = self.tray_icon

        self.tray_icon = None
        self.is_minimized_to_tray = False

        if tray is not None:

            try:
                tray.stop()
            except Exception as error:
                print(f"Tray icon stop error: {error}")

        try:

            self.root.deiconify()
            self.root.state("normal")
            self.root.lift()
            self.root.focus_force()

        except tk.TclError:
            pass

    def exit_from_tray(self, icon=None, item=None):

        try:
            self.root.after(0, self.close)
        except tk.TclError:
            pass

    # --------------------------------------------------------
    # BAŞLAT
    # --------------------------------------------------------

    def start(self):

        global hook
        global callback_reference
        global block_delete
        global block_f1

        if hook:
            return

        block_delete = self.delete_var.get()
        block_f1 = self.f1_var.get()

        if not block_delete and not block_f1:

            messagebox.showinfo(
                APP_NAMES[self.language],
                self.tr(
                    "Lütfen en az bir kısayol engelini etkinleştirin."
                ),
                parent=self.root
            )

            return

        ctypes.set_last_error(0)

        callback_reference = HOOKPROC(keyboard_callback)

        hook = user32.SetWindowsHookExW(
            WH_KEYBOARD_LL,
            callback_reference,
            kernel32.GetModuleHandleW(None),
            0
        )

        if not hook:

            error = ctypes.get_last_error()

            callback_reference = None

            messagebox.showerror(
                self.tr("Başlatma Hatası"),
                self.tr(
                    "Klavye kancası kurulamadı.\n\nWindows hata kodu: {error}"
                ).format(error=error),
                parent=self.root
            )

            return

        self.status_var.set(
            self.tr("Koruma etkin")
        )

        self.status_label.config(fg="#4ADE80")

        self.status_detail.set(
            self.tr("Seçilen kısayollar engelleniyor.")
        )

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.set_settings_state("disabled")

    # --------------------------------------------------------
    # DURDUR
    # --------------------------------------------------------

    def stop(self):

        global hook
        global callback_reference

        if hook:

            ctypes.set_last_error(0)

            result = user32.UnhookWindowsHookEx(hook)

            if not result:

                error = ctypes.get_last_error()

                messagebox.showwarning(
                    self.tr("Kısayol Engelleyici Hatası"),
                    self.tr(
                        "Klavye kancası kaldırılamadı.\n\nWindows hata kodu: {error}"
                    ).format(error=error),
                    parent=self.root
                )

                return

            hook = None

        callback_reference = None

        blocked_keys.clear()
        pressed_shifts.clear()

        self.status_var.set(
            self.tr("Koruma durduruldu")
        )

        self.status_label.config(fg="#F87171")

        self.status_detail.set(
            self.tr("Klavye kısayolları artık engellenmiyor.")
        )

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

        self.set_settings_state("normal")

    # --------------------------------------------------------
    # KAPAT
    # --------------------------------------------------------

    def close(self):

        if self.is_closing:
            return

        self.close_language_menu()

        # Önce klavye kancasını kaldır.
        if hook:

            self.stop()

            # Kanca kaldırılamadıysa uygulamayı kapatma.
            if hook:
                return

        self.is_closing = True

        # Sistem tepsisi simgesini kaldır.
        tray = self.tray_icon

        self.tray_icon = None
        self.is_minimized_to_tray = False

        if tray is not None:

            try:
                tray.stop()
            except Exception as error:
                print(f"Tray icon stop error: {error}")

        # Fare kaydırma bağlantısını kaldır.
        if hasattr(self, "canvas"):

            try:
                self.canvas.unbind_all("<MouseWheel>")
            except tk.TclError:
                pass

        # Uygulamayı tamamen kapat.
        try:
            self.root.destroy()
        except tk.TclError:
            pass


# ============================================================
# PROGRAM GİRİŞ NOKTASI
# ============================================================

def main():

    root = tk.Tk()

    try:

        app = ShortcutBlocker(root)
        root.mainloop()

    except Exception as error:

        try:
            root.destroy()
        except tk.TclError:
            pass

        error_root = tk.Tk()
        error_root.withdraw()

        messagebox.showerror(
            "Shortcut Blocker Error",
            str(error),
            parent=error_root
        )

        error_root.destroy()


if __name__ == "__main__":
    main()