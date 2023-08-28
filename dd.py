user = {
    "password": 0000,
    "balance": 5000,
}

#you must enter the correct password the above
def getmoney(hesap, para):

    giris_hakki = 3

    while giris_hakki > 0:
        password = int(input("enter password: "))

        if (password== hesap["password"]):
            print("login successfully.")
            break
        else:
            giris_hakki -= 1
            print(f"wrong password. your right of entry is 2: {giris_hakki}")

        if giris_hakki == 0:
            print("you have expired.")
            return

    para = int(input("enter you want to pull the  amount of money: "))

    if hesap["balance"] >= para:
        toplam = hesap["balance"] - para
        print(f"Merhaba user, overall balance = {toplam}")
        print("You can take the money .")
    else:
        print("insufficient balance.")


getmoney(user, para=0)





