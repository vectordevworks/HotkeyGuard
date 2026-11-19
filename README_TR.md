# KısayolBekçisi

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
<strong>
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe
</strong>

KısayolBekçisi, Windows üzerinde belirli klavye kısayollarını engellemenizi sağlayan, Python tabanlı hafif bir masaüstü uygulamasıdır. Basit grafik arayüzü sayesinde yanlışlıkla tetiklenebilecek kısayolları kontrol altında tutabilir ve seçtiğiniz koruma özelliklerini kolayca yönetebilirsiniz.

## Genel Bakış

Uygulama, Windows klavye olaylarını izleyerek seçtiğiniz kısayolları engeller. Koruma özelliği, uygulama başlatıldığında otomatik olarak etkinleşmez. Korumayı etkinleştirmek için arayüzdeki **Başlat** düğmesine basmanız gerekir.

## Özellikler

- **Shift + Delete engelleme:** Dosyaların kalıcı olarak silinmesini sağlayan Shift + Delete kısayolunu engeller.
- **Uygulamaya bağlı F1 engelleme:** F1 tuşunu Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, Opera ve Windows masaüstünde / Dosya Gezgini'nde engeller.
- **Seçilebilir korumalar:** Shift + Delete ve F1 engellemelerini arayüz üzerinden birbirinden bağımsız olarak etkinleştirip devre dışı bırakabilirsiniz.
- **Bildirim alanına küçültme:** Uygulamayı Windows bildirim alanına küçültmenizi sağlar.
- **Çoklu dil desteği:** Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Portekizce, Rusça, Japonca, Basitleştirilmiş Çince ve Korece dillerini destekler.
- **Kaydırılabilir arayüz:** Uygulama penceresinin içeriğini kaydırmanızı sağlar.

F1 engellemesi yalnızca yukarıda belirtilen uygulamalarda etkindir. Diğer uygulamalarda ve oyunlarda F1 tuşu engellenmez.

## Gereksinimler

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` ve `pathlib` modülleri Python standart kütüphanesinin bir parçasıdır.

Uygulamayı bildirim alanına küçültme özelliğini kullanabilmek için hem Pillow hem de pystray paketlerinin kurulu olması gerekir.

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
pyw .\HotkeyGuard.pyw
```

Alternatif olarak:

```powershell
pythonw .\HotkeyGuard.pyw
```

## Sanal Ortam (İsteğe Bağlı)

Python bağımlılıklarını diğer projelerden ayrı tutmak için sanal ortam kullanabilirsiniz:

1. Sanal ortam oluşturun:

```powershell
py -m venv .venv
```

2. Sanal ortamı etkinleştirin:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Gerekli bağımlılıkları yükleyin:

```powershell
py -m pip install -r requirements.txt
```

4. İşiniz bittiğinde sanal ortamı devre dışı bırakın:

```powershell
deactivate
```

## Kullanım

1. `HotkeyGuard.pyw` dosyasını çalıştırın.
2. Arayüzden engellemek istediğiniz kısayolları seçin.
3. Korumayı etkinleştirmek için **Başlat** düğmesine basın.
4. Koruma durumunu uygulama arayüzünden takip edin.
5. Uygulamayı bildirim alanına küçültmek için ilgili seçeneği kullanın. Bu özelliğin çalışması için Pillow ve pystray paketlerinin kurulu olması gerekir.

Dil tercihi aşağıdaki konumda saklanır:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Bu dosya yalnızca dil tercihini saklar. Kısayol engelleme seçenekleri uygulama ayarlarından belirlenebilir; bu seçeneklerin yapılandırma dosyasına kaydedildiği varsayılmamalıdır.

## Derleme (EXE Oluşturma)

Python uygulamasını tek bir EXE dosyasına dönüştürmek için PyInstaller kullanılır.

### 1. PyInstaller Kurulumu

PyInstaller'ın 6.22.3 sürümünü yükleyin:

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Proje Klasörüne Geçiş

PowerShell'i proje klasöründe açın.

### 3. Derleme Betiğini Çalıştırma

Aşağıdaki komutu çalıştırarak `embed_icon.ps1` betiğini başlatın:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Not:** `-ExecutionPolicy Bypass` parametresi, Windows'un yürütme ilkesi nedeniyle PowerShell betiklerinin çalıştırılmasını engelleyebildiği durumlarda kullanılır. Bu parametre yalnızca başlatılan PowerShell işlemi için geçerlidir ve sistem genelindeki güvenlik ayarlarını değiştirmez.

### 4. Derleme İşlemi

Derleme betiği aşağıdaki işlemleri gerçekleştirir:

1. Ana Python dosyasının ve `assets\icon.png` dosyasının mevcut olup olmadığını kontrol eder.
2. PyInstaller'ın kullanılabilir olduğunu doğrular.
3. Eski `dist` ve `build` klasörlerini temizler.
4. Uygulamayı konsol penceresi göstermeyen tek dosyalı bir EXE olarak derler.
5. `assets` klasörünü ve uygulama simgesini derlemeye dahil eder.
6. Oluşturulan EXE dosyasını kontrol eder.

### 5. Derleme Çıktısı

Derleme başarıyla tamamlandığında EXE dosyası aşağıdaki konumda oluşturulur:

```text
dist\HotkeyGuard.exe
```

**Yeni bir sürüm derlemek için izlenecek adımlar:**

1. PowerShell'i açın.
2. PyInstaller'ın kurulu olduğundan emin olun.
3. Proje klasörüne geçin.
4. Derleme betiğini çalıştırın.
5. Oluşturulan EXE dosyasını `dist` klasöründe bulabilirsiniz.

## Geliştirici

**vectordevworks**

## Lisans

Lisans koşulları hakkında bilgi edinmek için proje deposundaki `LICENSE` dosyasına bakın.
