#1
broj = float(input("Unesi neki broj:"))
if broj < 0 :
    print("Uneti broj je negativan")
    
#2
a = float(input("Unesi prvi broj:"))
b = float(input("Unesi drugi broj:"))
print("a je veci") if a > b else print("b je veci") if a < b else print("Jednaki su")

#3
povrce = ["grasak","krastavac"]
if "krompir" not in povrce:
    if "grasak" in povrce:
        print("grasak se nalazi u listi")
    else:
        print("Vreme je za nabavku")
else:
    print("Krompir se nalazi u listi")
    
#4
brojevi = [1,2,4,5,6,7,3]
for broj in brojevi:
    print(broj)
    
#5
torka = (True,False,False,True)
for tor in torka:
    print(tor)
    
#6
skup = {"jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"} 
for x in skup:
    print(x)

