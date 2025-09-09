[README.md](https://github.com/user-attachments/files/21781126/README.md)
Otel Rezervasyon Sistemi

Bu proje, **Python** ve **SQLite** kullanarak otel odalarını yönetebileceğiniz basit bir rezervasyon sistemidir.

Özellikler
- Oda ekleme
- Oda listesini görüntüleme
- Oda rezerve etme (müsaitlik durumunu değiştirme)
- Odayı boşaltma
- Verilerin **SQLite** veritabanında kalıcı olarak saklanması

Kullanılan Teknolojiler
- **Python 3**
- **SQLite3**


Dosya Yapısı

 otel-rezervasyon-sistemi
 otel_rezervasyon.py 
 README.md            
.gitignore          


veriTabani = VeriTabaniBaglantisi("rezervasyonsistemi.db", "Oda")
veriTabani.odaEkle(2)
Oda.odalariYazdir()
veriTabani.odaDoldur(1)
Oda.odalariYazdir()

