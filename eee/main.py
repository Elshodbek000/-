son_1=int(input("Birinchi son: "))

belgilar=input("Amal (+, -, *, /): ")

son_2=int(input("Ikkinchi son: "))

if belgilar == "+":
    print("Natija:", son_1 + son_2)
if belgilar == "-":
    print("Natija:", son_1 - son_2)
if belgilar == "*":
    print("Natija:", son_1 * son_2)
if belgilar == "/":
    if son_2 == 0:
        print("MUHAHAHA:", son_1 / son_2)
    else:
        print("MUHAHAHA:", son_1 / son_2)
else:
    print("Noto'g'ri")

summa = int(input("Xarid summasi: "))
if summa > 500000:
    chegirma = 10
if summa < 200000:
    chegirma = 5
else:
    chegirma = 0
tolov = summa - summa * chegirma / 100
print("Chegirma:", str(chegirma) + "%")
print("To'lov:", format(tolov,",.0f"), "so'm")

yosh = int(input("Yoshingiz: "))
if yosh < 0:
    print("Aldashga urinma")
if yosh <= 12:
    print("Bola")
if yosh <= 17:
    print("O'smir")
if yosh <= 59:
    print("Kattalar")
if yosh <= 67:
    print("Keksa")
if yosh <= 90:
    print("Zo`r")
if yosh <= 100:
    print("Daxshat")
if yosh <= 200 :
    print("Aldama")

rang = input("Svetofor rangi: ").lower()
if rang == "qizil":
    print("To'xta")
elif rang == "sariq":
    print("Tayyor tur")
elif rang == "yashil":
    print("Bosss")
else:
    print("Tentakmisan unday rang bo`lmaydi")
