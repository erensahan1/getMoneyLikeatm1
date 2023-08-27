erensahan = {
    "sifre": 3806,
    "bakiye": 5000,
}


def paracek(hesap, para):

    giris_hakki = 3

    while giris_hakki > 0:
        sifre = int(input("Şifreyi gir: "))

        if sifre == hesap["sifre"]:
            print("Giriş başarılı.")
            break
        else:
            giris_hakki -= 1
            print(f"Hatalı şifre. Kalan giriş hakkı: {giris_hakki}")

        if giris_hakki == 0:
            print("Giriş hakkınız tükendi.")
            return

    para = int(input("Çekmek istediğiniz miktarı girin: "))

    if hesap["bakiye"] >= para:
        toplam = hesap["bakiye"] - para
        print(f"Merhaba eren, genel bakiye = {toplam}")
        print("Parayı alabilirsiniz.")
    else:
        print("Yetersiz bakiye.")


paracek(erensahan, para=0)





