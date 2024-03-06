print("***********PRVI DEO*****************")
#1
x = 5**2 + 3/4
'''
#2
a = 17
b = 3
kolicnik = a/b
ostatak = a%b

#3
rezultat = kolicnik // 2
rezultat *= 3

#4
a5_10 = a >= 5 and a <= 10

#5
a10 = a<-10 or a>10

#6
a5_10_neg = not a5_10
a10_neg = not a10

print("1. x:", x)
print("2. kolicnik:", kolicnik)
print("2. ostatak:", ostatak)
print("3. rezultat:", rezultat)
print("4. a5_10:", a5_10)
print("5. a10:", a10)
print("6. a5_10_neg:", a5_10_neg)
print("6. a10_neg:", a10_neg)

print("***********DRUGI DEO*****************")
#1
a = int(input("1.Unesi prvi broj:"))
b = int(input("Unesi drugi broj:"))
c = a+b

#2
dan = int(input("2.Unesi dan u mesecu:"))
mesec = int(input("Unesi mesec u godini:"))
godina = int(input("Unesi godinu:"))
print(dan,mesec,godina,sep = '/')

#3
tekst = input("3.Unesite neki tekst:")
tekst = tekst.lower().strip().split(" ")
print(tekst)

#4
tekst = input("4.Unesite neki tekst:")
tekst = tekst.replace("cao","zdravo")
print(tekst)

#5
tekst = input("5.Unesite neki tekst:")
je = 'je' in tekst
sam = 'sam' not in tekst
A = 'A' == tekst[0]
duzina = len(tekst) > 0

print("je se nalazi u tekstu:", je, "\nsam se ne nalazi u tekstu:", sam, "\nA je prvo slovo teksta:", A, "\nduzina je veca od nule:", duzina)

#6
sve = input("6.Unesite ime prezime i godine odvojene zarezom")
sve = sve.split(',')
ime = sve[0]
prezime = sve[1]
godine = sve[2]
print(ime + prezime + " ima " + godina + " godina")

print("***********TRECI DEO*****************")

#1
print("Lista:")
lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"] 
print(lista[1])
lista[2] = "kupine"
print(lista)
lista.append("narandze")
print(lista)
lista.insert(2,"limun")
print(lista)
lista.remove("mandarine")
print(lista)
print(lista[2:6])
print(lista[-1])
print(len(lista))
lista.sort()
print(lista)
lista.clear()
print(lista)

#2
print("Recnik:")
recnik = {
 "marka": "Ford",
"model": "Mustang",
"godina": 1964
} 

print(recnik["model"])
print(recnik.get("model"))
recnik.update({"godina": 2003}) 
print(recnik)
recnik["boja"] = "zuta"
print(recnik)
del recnik["marka"] 
print(recnik)
recnik.clear()
print(recnik)
'''
#3
print("Torka:")
torka = ("jabuke", "banane", "kivi", "mandarine", "grozdje", "mango")
print(torka[:4])
print(torka[-2:])
*ostalo,mango = torka
print(ostalo)
print(mango)

#4
print("Skup:")
skup = {"jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"} 
skup.add("narandza")
print(skup)
skup2 = {"visnje","jagode","maline","kupine"}
skup.update(skup2)
print(skup)

voce = input("Unesi sta oces da uklonis:")

if voce in skup:
    skup.remove(voce)
    print(skup)
else:
    print("Nema toga u skupu")
