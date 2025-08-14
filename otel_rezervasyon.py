import sqlite3

class Oda:
    odaListesi = []

    def __init__(self, odaNo, kisiSayisi, musaitlik):
        self.odaNo = odaNo
        self.kisiSayisi = kisiSayisi
        self.musaitlik = musaitlik
        Oda.odaListesi.append(self)

    @classmethod
    def odalariYazdir(cls):
        for oda in cls.odaListesi:
            durum = "Müsait" if oda.musaitlik == 1 else "Dolu"
            print(f"Oda No: {oda.odaNo}, Kişi Sayısı: {oda.kisiSayisi}, Durum: {durum}")


class VeriTabaniBaglantisi:
    def __init__(self, veriTabaniIsim, tabloIsim):
        self.veritabani = sqlite3.connect(veriTabaniIsim)
        self.tablo = tabloIsim
        self.imlec = self.veritabani.cursor()
        self.imlec.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.tablo}(
                odaNo INTEGER PRIMARY KEY AUTOINCREMENT,
                kisiSayisi INTEGER NOT NULL,
                odaMusaitlik INTEGER
            )
        """)
        self.veritabani.commit()

    def odalariGetir(self):
        sorgu = f"SELECT * FROM {self.tablo}"
        self.imlec.execute(sorgu)
        Oda.odaListesi.clear()
        for oda in self.imlec.fetchall():
            Oda(oda[0], oda[1], oda[2])

    def odaEkle(self, kisiSayisi):
        sorgu = f"INSERT INTO {self.tablo}(kisiSayisi, odaMusaitlik) VALUES(?, ?)"
        self.imlec.execute(sorgu, (kisiSayisi, 1))
        self.veritabani.commit()
        self.odalariGetir()

    def odaDoldur(self, odaNo):
        sorgu = f"SELECT odaMusaitlik FROM {self.tablo} WHERE odaNo=?"
        self.imlec.execute(sorgu, (odaNo,))
        musaitlik = self.imlec.fetchone()[0]
        if musaitlik == 1:
            sorgu2 = f"UPDATE {self.tablo} SET odaMusaitlik=0 WHERE odaNo=?"
            self.imlec.execute(sorgu2, (odaNo,))
            self.veritabani.commit()
            self.odalariGetir()
            print("Oda rezerve edildi.")
        else:
            print("Oda zaten dolu.")

    def odayiBosalt(self, odaNo):
        sorgu = f"SELECT odaMusaitlik FROM {self.tablo} WHERE odaNo=?"
        self.imlec.execute(sorgu, (odaNo,))
        musaitlik = self.imlec.fetchone()[0]
        if musaitlik == 0:
            sorgu2 = f"UPDATE {self.tablo} SET odaMusaitlik=1 WHERE odaNo=?"
            self.imlec.execute(sorgu2, (odaNo,))
            self.veritabani.commit()
            self.odalariGetir()
            print("Oda boşaltıldı.")
        else:
            print("Oda zaten boş durumda.")


# --- Test ---
veriTabani = VeriTabaniBaglantisi("rezervasyonsistemi.db", "Oda")
veriTabani.odaEkle(1)
veriTabani.odaEkle(2)
veriTabani.odaEkle(3)
veriTabani.odaEkle(1)

Oda.odalariYazdir()
print("--- Rezervasyon yapılıyor ---")
veriTabani.odaDoldur(1)
Oda.odalariYazdir()
