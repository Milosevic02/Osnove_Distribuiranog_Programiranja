# # Kontrola toka programa (str. 31)
# #1
# broj = float(input("Unesi neki broj:"))
# if broj < 0 :
#     print("Uneti broj je negativan")
    
# #2
# a = float(input("Unesi prvi broj:"))
# b = float(input("Unesi drugi broj:"))
# print("a je veci") if a > b else print("b je veci") if a < b else print("Jednaki su")

# #3
# povrce = ["grasak","krastavac"]
# if "krompir" not in povrce:
#     if "grasak" in povrce:
#         print("grasak se nalazi u listi")
#     else:
#         print("Vreme je za nabavku")
# else:
#     print("Krompir se nalazi u listi")
    
# #4
# brojevi = [1,2,4,5,6,7,3]
# for broj in brojevi:
#     print(broj)
    
# #5
# torka = (True,False,False,True)
# for tor in torka:
#     print(tor)
    
# #6
# skup = {"jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"} 
# for x in skup:
#     print(x)

# #7
# recnik = {
#  "marka": "Ford",
# "model": "Mustang",
# "godina": 1964
# } 
# for kljuc in recnik.keys():
#     print(kljuc)
    
# #8
# lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
# for voce in lista:
#     if "kivi" == voce:
#         continue
#     elif "grozdje" == voce:
#         break
#     print(voce)
    
# #9
# i = 5
# while i<=10:
#     print(i)
#     i +=1
    
# #10
# i=1
# while i<6 :
#     print(i)
#     i+=1
# else : print("Vrednost promenljive je",i, "više nije manja od 6")

# Obrada izuzetaka i funkcije (str. 36)
#1
def zadatak1(lista):
    maks = max(lista)
    lista.remove(maks)
    mini = min(lista)
    lista.remove(mini)
    lista.insert(0,maks)
    lista.append(mini)

lista = [4,6,9,1,6,4]
print("Lista pre promene: ",lista)
zadatak1(lista)
print("Lista posle promene: ",lista)