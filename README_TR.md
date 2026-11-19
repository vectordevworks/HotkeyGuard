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
<strong>
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe
</strong>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Basitleştirilmiş Çince"> Basitleştirilmiş Çince
</a>

## Kısayol Bekçisi, Windows üzerinde belirli klavye kısayollarını engellemenizi sağlayan, Python tabanlı hafif bir masaüstü uygulamasıdır. Basit grafik arayüzü sayesinde yanlışlıkla tetiklenen kısayolları kontrol altında tutabilir ve istediğiniz korumaları kolayca yönetebilirsiniz.

## Genel Bakış

Uygulama, Windows klavye olaylarını izler ve seçtiğiniz kısayolları engeller. Kısayol koruması uygulama başlatıldığında otomatik olarak etkinleşmez; arayüzdeki **Başlat** düğmesine tıklamanız gerekir.

## Özellikler

- **Shift + Delete engelleme:** Kalıcı silme kısayolunu engeller.
- **Uygulamaya özel F1 engelleme:** Chrome, Microsoft Edge, Firefox, Brave, Opera ve Windows Masaüstü / Dosya Gezgini'nde F1 tuşunu engeller.
- **Seçilebilir korumalar:** Shift + Delete ve F1 engelleme özelliklerini arayüz üzerinden birbirinden bağımsız olarak etkinleştirebilir veya devre dışı bırakabilirsiniz.
- **Sistem tepsisine küçültme:** Uygulamayı sistem tepsisine küçültebilirsiniz.
- **Çoklu dil desteği:** Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Portekizce, Rusça, Japonca, Basitleştirilmiş Çince ve Korece dillerini destekler.
- **Kaydırılabilir arayüz:** Uygulama penceresinin içeriği kaydırılabilir.

F1 engelleme özelliği yalnızca yukarıda listelenen uygulamalarda etkindir. F1 tuşu diğer uygulamalarda veya oyunlarda engellenmez.

## Gereksinimler

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` ve `pathlib`, Python standart kütüphanesinin bir parçasıdır.

Sistem tepsisine küçültme özelliğini kullanabilmek için hem Pillow hem de pystray gereklidir.

## Kurulum

1. Proje dosyalarını bilgisayarınıza indirin veya depoyu klonlayın.
2. Proje klasörünü açın.
3. Bu klasörde PowerShell'i açın.
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

1. Bir sanal ortam oluşturun:

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
3. Korumayı etkinleştirmek için **Başlat** düğmesine tıklayın.
4. Uygulama arayüzünden koruma durumunu takip edin.
5. Uygulamayı sistem tepsisine göndermek için küçültme seçeneğini kullanın. Bu özelliğin çalışması için Pillow ve pystray kurulu olmalıdır.

Dil tercihi aşağıdaki konumda saklanır:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Bu dosya dil seçimini saklar. Kısayol engelleme seçenekleri uygulama ayarlarından seçilebilir; bu seçeneklerin yapılandırma dosyasına kaydedildiğini varsaymayın.

## EXE Oluşturma (Derleme)

Python uygulamasını tek bir EXE dosyasına dönüştürmek için PyInstaller kullanılır.

### 2. Proje Klasörüne Gitme

Proje klasöründe PowerShell'i açın.

### 3. Derleme Betiğini Çalıştırma

`embed_icon.ps1` betiğini başlatmak için aşağıdaki komutu çalıştırın:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Not:** Windows, yürütme ilkesi nedeniyle PowerShell betiklerinin çalıştırılmasını engelleyebilir. `-ExecutionPolicy Bypass` parametresi bu nedenle kullanılır. Bu ayar yalnızca başlatılan PowerShell işlemi için geçerlidir. Sistem genelindeki güvenlik ayarları değiştirilmez.

### 4. Derleme Süreci

Derleme betiği aşağıdaki işlemleri gerçekleştirir:

1. Ana Python dosyasını ve `assets\icon.png` dosyasını kontrol eder.
2. PyInstaller'ın kullanılabilir durumda olduğunu doğrular.
3. Eski `dist` ve `build` klasörlerini temizler.
4. Uygulamayı konsol penceresi olmadan, tek dosyalık bir EXE olarak derler.
5. `assets` klasörünü ve uygulama simgesini derlemeye dahil eder.
6. Oluşturulan EXE dosyasını kontrol eder.

### 5. Derleme Çıktısı

Derleme başarıyla tamamlandıktan sonra EXE dosyası aşağıdaki konumda oluşturulur:

```text
dist\HotkeyGuard.exe
```

**Yeni bir sürüm derlerken izlenecek adımlar:**

1. PowerShell'i açın.
2. PyInstaller'ın kurulu olduğundan emin olun.
3. Proje klasörüne gidin.
4. Derleme betiğini çalıştırın.
5. Oluşturulan EXE dosyasını `dist` klasöründen alın.

## Geliştirici

**vectordevworks**

## Lisans

Lisans koşulları için proje deposundaki `LICENSE` dosyasına bakın.
