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

 Kurulum ve Çalıştırma
1. Bu projeyi bilgisayarınıza klonlayın veya indirin:
   ```bash
   git clone https://github.com/KULLANICI_ADIN/otel-rezervasyon-sistemi.git
   cd otel-rezervasyon-sistemi
   ```
2. Python dosyasını çalıştırın:
   ```bash
   python otel_rezervasyon.py
   ```

Dosya Yapısı
```
   otel-rezervasyon-sistemi
 ├── otel_rezervasyon.py   # Ana uygulama kodu
 ├── README.md             # Proje açıklaması
 └── .gitignore            # Gereksiz dosyaları hariç tutma
```

 Kullanım Örneği
```python
veriTabani = VeriTabaniBaglantisi("rezervasyonsistemi.db", "Oda")
veriTabani.odaEkle(2)
Oda.odalariYazdir()
veriTabani.odaDoldur(1)
Oda.odalariYazdir()
```

