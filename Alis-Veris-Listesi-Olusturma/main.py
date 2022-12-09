liste = []
fiyatListe = []
uygulamaKpansin = False

def listeElemanEkle():
    print("Çıkmak için Q tuşuna tıklayın !")
    while True:
        yeniEleman = input("Listeye Eleman Ekle: ")
        yeniEleman = yeniEleman.lower()
        if yeniEleman == "q":
            print("-------Liste------")
            for eleman in liste:
                print(eleman,"-> ", end=" ")
                i=0
                print(fiyatListe[i])
            break
        else:
            try:
                liste.append(yeniEleman)
                elemanFiyat = float(input("Fiyatı: "))
                fiyatListe.append(elemanFiyat)
            except:
                print("-> Bir Hata Oluştu! Lütfen Programı Yeniden Başlatınız.")
                exit()

#Programı çalıştırıyoruz

listeElemanEkle()