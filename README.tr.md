Bu uygulama, bir isim listesinden kişi sayıları birbirine yakın rastgele takımlar oluşturur.

# Team Generator

[English](README.md) · [Türkçe](README.tr.md)

İsimleri virgülle ayırarak gir, takım sayısını seç ve formu gönder. Python listeyi karıştırıp isimleri sırayla takımlara dağıtır. Takımların kişi sayıları en fazla bir farklı olur.

## Yerel kurulum

pip ve venv içeren Python 3 ile bir web tarayıcısı gerekir.

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

[localhost:5000](http://127.0.0.1:5000) adresini aç. `python app.py` komutu da debug modu kapalı yerel sunucuyu başlatır.

## Takım oluşturma

Örneğin `Ada, Deniz, Ece, Mert, Selin, Can` isimlerini ve takım sayısı olarak `3` girip **Generate Teams** düğmesine bas. Her takımda iki isim olur. Formu yeniden gönderdiğinde liste tekrar karıştırılır.

- Takım sayısı, katılımcı sayısını aşmayan pozitif bir tam sayı olmalıdır.
- İsimlerin başındaki ve sonundaki boşluklar temizlenir; boş öğeler atlanır.
- Tekrarlanan isimler ayrı katılımcı olarak sayılır.
- Dağıtım yalnız kişi sayısını dengeler. Yetenek, rol veya başka özellikleri dikkate almaz.

Kayıtlı geçmiş, dışa aktarma veya sabit tohumla tekrarlanabilir kura özelliği yoktur. Arayüzde Türkçe ve İngilizce etiketler birlikte kullanılır. Repoda otomatik test paketi bulunmaz.

## Kod

Formu ve takım dağıtımını [app.py](app.py) yönetir. [index.html](index.html) ve [teams.html](teams.html) şablonları repo kökündedir. [views.py](views.py), `/views/` adresinde alternatif giriş sağlar.

## Lisans

Projeye ait bir lisans dosyası bulunmuyor. Flask ve diğer bağımlılıklar kendi lisanslarına tabidir.
