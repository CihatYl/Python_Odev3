class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        self.adı = adı
        self.departmanı = departmanı
        self.çalışma_yılı = çalışma_yılı
        self.maaşı = maaşı

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)
        print("Personel eklendi.")

    def personel_listele(self):
        print("\nFirma Çalışanları:")
        for i, personel in enumerate(self.personel_listesi, 1):
            print(f"{i}. Personel:")
            print("Adı:", personel.adı)
            print("Departmanı:", personel.departmanı)
            print("Çalışma Yılı:", personel.çalışma_yılı)
            print("Maaşı:", personel.maaşı)
            print("-------------------")

    def maaş_zammı(self, indeks, zam_oranı):
        personel = self.personel_listesi[indeks]
        personel.maaşı *= (1 + zam_oranı / 100)
        print("Maaş zammı yapıldı.")

    def personel_çıkart(self, indeks):
        del self.personel_listesi[indeks]
        print("Personel çıkartıldı.")

# Firma nesnesi oluşturuluyor
firma = Firma()

# Örnek personeller oluşturuluyor
personel1 = Personel("Ahmet", "İnsan Kaynakları", 5, 5000)
personel2 = Personel("Ayşe", "Finans", 3, 4500)
personel3 = Personel("Mehmet", "Pazarlama", 7, 6000)
personel4 = Personel("Fatma", "Bilgi İşlem", 2, 4800)

# Personelleri listeye ekliyoruz
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)
firma.personel_ekle(personel3)
firma.personel_ekle(personel4)

while True:
    print("\nİşlem Menüsü:")
    print("1. Personel Ekle")
    print("2. Personel Listele")
    print("3. Maaş'a Zam Yap")
    print("4. Personel Çıkart")
    print("5. Programı Bitir")

    seçim = input("Lütfen seçim yapınız: ")

    if seçim == "1":
        adı = input("Personel adını giriniz: ")
        departmanı = input("Personelin çalıştığı departmanı giriniz: ")
        çalışma_yılı = int(input("Personelin çalışma yılını giriniz: "))
        maaşı = float(input("Personelin maaşını giriniz: "))
        yeni_personel = Personel(adı, departmanı, çalışma_yılı, maaşı)
        firma.personel_ekle(yeni_personel)

    elif seçim == "2":
        firma.personel_listele()

    elif seçim == "3":
        firma.personel_listele()
        indeks = int(input("Hangi personelin maaşına zam yapmak istiyorsunuz? (1'den başlayarak indeks numarası giriniz): ")) - 1
        zam_oranı = float(input("Zam oranını giriniz (% cinsinden): "))
        firma.maaş_zammı(indeks, zam_oranı)

    elif seçim == "4":
        firma.personel_listele()
        indeks = int(input("Hangi personeli çıkartmak istiyorsunuz? (1'den başlayarak indeks numarası giriniz): ")) - 1
        firma.personel_çıkart(indeks)

    elif seçim == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
