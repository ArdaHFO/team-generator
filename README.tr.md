Bu uygulama, bir kişi listesini rastgele takımlara ayırır.

<h1 align="center">Team Generator</h1>

<p align="center"><strong>Tek katılımcı listesi. Yeni takım eşleşmeleri.</strong></p>
<p align="center">Virgülle ayrılmış isimleri karıştırıp seçilen sayıda takıma dağıtan küçük bir Python ve Flask prototipi.</p>

<p align="center">
  <a href="README.md">English</a> · <strong>Türkçe</strong><br />
  <a href="#yerel-olarak-çalıştır"><strong>Yerel olarak çalıştır</strong></a> ·
  <a href="#takımları-oluştur">Takımları oluştur</a> ·
  <a href="#doğrulama-ve-mevcut-sınırlar">Mevcut sınırlar</a>
</p>

---

Team Generator, formdan sonuç ekranına uzanan basit bir akışı örnekler. Katılımcı isimlerini gir, takım sayısını seç ve formu gönder. Sunucu listeyi karıştırır, ardından katılımcıları sırayla takımlara dağıtır. Geçerli pozitif takım sayısı için takım büyüklükleri en fazla bir kişi farklılaşır.

**Bu küçük bir prototiptir.** Arayüzde Türkçe ve İngilizce etiketler birlikte kullanılır. Form ve sonuç şablonları repo kökünde bulunur. Uygulama bunları açıkça bu dizinden yükler.

## Yerel olarak çalıştır

| Gereksinim | Amaç |
| --- | --- |
| pip ve venv içeren Python 3 | Geliştirme ortamı |
| Flask 3.0.0 | Form işleme ve HTML şablonları |
| Web tarayıcısı | Katılımcı formu ve takım sonuçları |

```text
git clone https://github.com/ArdaHFO/team-generator.git
cd team-generator
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 5000
```

[localhost:5000](http://127.0.0.1:5000) adresini aç. `python app.py` komutu da debug modu kapalı tek bir yerel sunucu başlatır.

## Takımları oluştur

1. İsimleri virgülle ayırarak gir. Örneğin `Ada,Deniz,Ece,Mert,Selin,Can`.
2. Pozitif bir tam sayı olarak takım sayısını yaz. Örneğin `3`.
3. Eşleşmeleri görmek için **Generate Teams** düğmesine bas.

Girilen her öğe bir kez atanır. Altı öğe ve üç takım için her takım iki öğe içerir. Formun yeniden gönderilmesi farklı eşleşmeler oluşturabilir.

## Projede neler var?

- **Kısa form akışı.** Tek sayfa katılımcıları ve istenen takım sayısını toplar.
- **Rastgele sıralama.** Python'un `random.shuffle` işlevi gönderilen listeyi karıştırır.
- **Dengeli takım sayıları.** Sıralı dağıtım, karıştırılmış öğeleri takımlara paylaştırır.
- **Basit sonuç sayfası.** Jinja şablonu her takımı ve katılımcılarını gösterir.
- **Az sayıda bağımlılık.** Uygulama Flask ve Python standart kütüphanesini kullanır. Veritabanı veya hesap sistemi içermez.

## Doğrulama ve mevcut sınırlar

Kaynak statik olarak incelendi. Bu değişiklikler için uygulama, otomatik test veya tarayıcı kontrolü çalıştırılmadı.

- Sunucu geçersiz takım sayılarını, boş katılımcı listelerini ve katılımcı sayısından fazla takım talebini reddeder. İsimlerin başındaki ve sonundaki boşluklar temizlenir, boş öğeler kaldırılır.
- İki kez girilen kişi hâlâ iki ayrı öğe sayılır. Algoritma yetenek, rol veya başka özellikleri değil, katılımcı sayılarını dengeler.
- Otomatik test paketi, kalıcı takım geçmişi veya dışa aktarma işlevi yoktur.
- Arayüz küçük bir yerel prototip olarak kalır. Statik düzeltmeler tarayıcı davranışının test edildiği anlamına gelmez.

Rastgeleleştirme günlük gruplama içindir. Uygulama denetlenebilir kura veya sabit tohumla tekrarlanabilirlik sağlamaz.

## Proje yapısı

```text
app.py            Form işleme, karıştırma ve takım atama
views.py          Alternatif /views/ sayfası
index.html        Katılımcı ve takım sayısı formu
teams.html        Jinja sonuç şablonu
requirements.txt  Sabitlenmiş Flask ortamı
```

## Geliştirme ve katkı

Formu, giriş doğrulamasını ve atama mantığını anlaşılır tut. Yeni değişiklikler pozitif ve sınırlı takım sayısını, boş olmayan öğeleri ve dengeli atamayı korumalıdır. Bu kurallar için deterministik testler güveni artıracaktır.

Hata bildiriminde takım sayısını ve küçük bir kurmaca isim listesini kullan. Gerçek katılımcı listelerini paylaşma.

## Lisans

Bu repoda proje lisansı dosyası bulunmuyor. Herkese açık olması, kod için serbest kullanım lisansı bulunduğu anlamına gelmez. Flask ve diğer bağımlılıklar kendi lisanslarına tabidir.
