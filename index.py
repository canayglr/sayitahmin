from random import randint
hak=3
cevap=randint(1,10)
print(f"Sayı Tahmin Etme Oyununa Hoşgeldiniz! {hak} adet hakkınız bulunmaktadır!")
while True:
    if hak==0:
        print("Hakkınız kalmadı bir dahaki sefere artık :)")
        break
    else:
        sayi=int(input("Lütfen 1'den 10'a kadar bir sayı giriniz!"))
        if cevap==sayi:
            c=input("Soruyu doğru yanıtladınız, devam etmek için [0] çıkmak için [1] tuşlayınız!")
            if c=="0":
                cevap=randint(1,10)
                hak=3
                continue
            else:
                break
        elif sayi<cevap:
            hak=hak-1
            print(f"Daha büyük sayı giriniz: {hak} hakkınız kaldı!")
        elif sayi>cevap:
            hak=hak-1
            print(f"Daha küçük sayı giriniz: {hak} hakkınız kaldı!")