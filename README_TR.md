# Shortcut Blocker

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="İngilizce"> İngilizce
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Almanca"> Almanca
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="İspanyolca"> İspanyolca
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Fransızca"> Fransızca
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonca"> Japonca
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Korece"> Korece
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portekizce"> Portekizce
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Rusça"> Rusça
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Basitleştirilmiş Çince"> Basitleştirilmiş Çince
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe
</a>

Shortcut Blocker, Windows üzerinde belirli klavye kısayollarını engellemenizi sağlayan basit bir masaüstü uygulamasıdır. Uygulama, yanlışlıkla kullanılabilecek kısayolları kontrol altında tutmanıza yardımcı olur.

## Genel Bakış

Uygulama, Windows klavye olaylarını izleyerek seçtiğiniz kısayolları engeller. Engelleme koruması uygulama açıldığında otomatik başlamaz; arayüzden **Başlat** düğmesine basmanız gerekir.

## Özellikler

- **Shift + Delete engelleme:** Kalıcı silme kısayolunu engeller.
- **Uygulamaya bağlı F1 engelleme:** F1 tuşunu Chrome, Microsoft Edge, Firefox, Brave, Opera ve Windows Masaüstü / Dosya Gezgini üzerinde engeller.
- **Seçilebilir korumalar:** Shift + Delete ve F1 engellemelerini arayüzden ayrı ayrı açıp kapatabilirsiniz.
- **Sistem tepsisine küçültme:** Uygulamayı sistem tepsisine küçültebilirsiniz.
- **Çoklu dil desteği:** Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Portekizce, Rusça, Japonca, Basitleştirilmiş Çince ve Korece.
- **Kaydırılabilir arayüz:** Uygulama penceresinin içeriği kaydırılabilir.

F1 engellemesi yalnızca yukarıda belirtilen uygulamalarda etkindir. Diğer uygulamalarda ve oyunlarda F1 tuşu engellenmez.

## Gereksinimler

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` ve `pathlib` Python standart kütüphanesinin parçalarıdır.

Sistem tepsisine küçültme özelliğini kullanmak için hem Pillow hem de pystray gereklidir.

## Kurulum

1. Proje dosyalarını bilgisayarınıza indirin veya depoyu klonlayın.
2. Proje klasörünü açın.
3. PowerShell'i bu klasörde başlatın.
4. Gerekli Python paketlerini yükleyin:

```powershell
py -m pip install -r requirements.txt
```

`requirements.txt` dosyasının içeriği:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Uygulamayı başlatın:

```powershell
pyw .\ShortcutBlocker.pyw
```

Alternatif olarak:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Sanal Ortam (İsteğe Bağlı)

Bağımlılıkları proje için ayrı bir sanal ortamda tutabilirsiniz:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Kullanım

1. `ShortcutBlocker.pyw` dosyasını çalıştırın.
2. Arayüzden engellemek istediğiniz kısayolları seçin.
3. Korumayı etkinleştirmek için **Başlat** düğmesine basın.
4. Koruma durumunu uygulama arayüzünden takip edin.
5. Uygulamayı sistem tepsisine küçültmek için küçültme seçeneğini kullanın. Bu özellik için Pillow ve pystray kurulu olmalıdır.

Dil tercihi aşağıdaki konumda saklanır:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Bu dosya dil seçimini saklar. Kısayol engelleme seçenekleri uygulama ayarlarında seçilebilir; bu seçeneklerin config dosyasına kaydedildiği varsayılmamalıdır.

## Derleme (EXE Oluşturma)

EXE oluşturmak için PyInstaller gerekir. PyInstaller'ı ayrıca yükleyin:

```powershell
py -m pip install pyinstaller==6.22.3
```

Ardından PowerShell'i proje klasöründe açın ve derleme scriptini çalıştırın:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

Script şu işlemleri gerçekleştirir:

1. Ana Python dosyasını ve `assets\icon.png` dosyasını kontrol eder.
2. PyInstaller'ın kullanılabilir olduğunu doğrular.
3. Eski `dist` ve `build` klasörlerini temizler.
4. Uygulamayı tek dosyalı, konsol penceresi göstermeyen bir EXE olarak derler.
5. `assets` klasörünü ve uygulama ikonunu derlemeye dahil eder.
6. Oluşturulan EXE dosyasını kontrol eder.

Derleme tamamlandığında uygulama şu konumda bulunur:

```text
dist\ShortcutBlocker.exe
```

## Geliştirici

**vectordevworks**

## Lisans

Lisans koşulları için proje deposundaki `LICENSE` dosyasına bakın.
