# KLASE (str. 39)
#1
class Student:
    fakultet = "FTN"
    
    def __init__(self,ime,prezime,br_indeksa):
        self.ime = ime
        self.prezime = prezime
        self.br_indeksa = br_indeksa
        
    def __str__(self):
       return f"{self.fakultet} {self.br_indeksa} {self.ime} {self.prezime}"

student1 = Student("Marko", "Markovic", "PR1/2020")
student2 = Student(ime ="Jovan", prezime = "Jovanovic", br_indeksa ="PR2/2020")
student3 = Student(prezime = "Petrovic", ime ="Petra", br_indeksa="PR3/2020")
student4 = Student(br_indeksa="PR4/2020", prezime = "Ivanovic", ime ="Ivana")

print("Studenti:")
print(student1)
print(student2)
print(student3)
print(student4)

#2
class Merenje:
    drzava = "srbija"
    def __init__(self,grad,merenja):
        self.grad = grad
        self.merenja = merenja
        
    def __str__(self):
        return f"{self.drzava}, {self.grad}, {self.merenja}"

    def prosek(self):
        try:
            return sum(self.merenja)/len(self.merenja)
        except Exception as e:
            print("Greska:",e)
            return 0
        
novi_sad = Merenje("Novi Sad", [1.75, 1.80, 1.65, 2.02, 1.90, 1.68, 1.73])
sombor = Merenje("Sombor", [1.85, 1.80, 1.75, 2.02, 1.95, 1.78, 1.83])
zrenjanin = Merenje("Zrenjanin", [1.75, 1.70, 1.67, 2.00, 1.80, 1.78, 1.73])

print("Prosecna visina po gradu:")
print(f"{novi_sad}, prosečna visina: {novi_sad.prosek()}")
print(f"{sombor}, prosečna visina: {sombor.prosek()}")
print(f"{zrenjanin}, prosečna visina: {zrenjanin.prosek()}")


#3
class Ucenik:
    def __init__(self,ime,prezime):
        self.ime = ime
        self.prezime = prezime
        self.ocene = {}
        self.zakljucne_ocene = {}
    
    def upisi_ocenu(self,predmet,ocena):
        if predmet in self.ocene.keys():
            self.ocene[predmet].append(ocena)
        else:
            self.ocene[predmet] = [ocena]
            
    def zakljuci_ocenu(self,predmet):
        if predmet in self.ocene.keys():
            try:
                zakljucna = round(sum(self.ocene[predmet])/len(self.ocene[predmet]))
                self.zakljucne_ocene[predmet] = zakljucna
                return zakljucna
            except Exception as e:
                print("Greska:",e)
        return None
    
    def prosek(self):
        try:
            return sum(self.zakljucne_ocene.values())/len(self.zakljucne_ocene.values())
        except Exception as e:
            print("Greska: ",e)
            
    def __str__(self):
        return f"{self.ime} {self.prezime} ocene : {self.ocene}"
    
ucenik1 = Ucenik("Marko", "Markovic")
ucenik1.upisi_ocenu("matematika", 5)
ucenik1.upisi_ocenu("matematika", 4)
ucenik1.upisi_ocenu("matematika", 5)
ucenik1.upisi_ocenu("matematika", 5)

print(ucenik1)
print("Ocene: ", ucenik1.ocene)
print("Zakljucna ocena iz matematike: ",ucenik1.zakljuci_ocenu("matematika"))
print("Zakljucna ocena iz srpskog: ", ucenik1.zakljuci_ocenu("srpski"))

ucenik1.upisi_ocenu("srpski", 5)
ucenik1.upisi_ocenu("srpski", 4)
ucenik1.upisi_ocenu("srpski", 3)
ucenik1.upisi_ocenu("srpski", 5)

print("Ocene: ", ucenik1.ocene)
print("Zakljucna ocena iz srpskog: ", ucenik1.zakljuci_ocenu("srpski"))
print("Prosek ucenika", ucenik1.prosek())

# RAD SA DATOTEKAMA (str. 46)
#1
f = open("zadatak1.txt","w")
f.write("PR41/2021 Dragan Milosevic")
f.close()

#2
f = open("zadatak2.txt","a")
while True:
    unos = input("Unesi novi red ili q za izlaz:")
    if unos == 'q':
        break
    f.write(unos+"\n")
f.close()

f = open("zadatak2.txt")
print(f.read())
f.close()

#3
from student import Student

studenti = []

f = open("zadatak3.txt")
for red in f:
    reci = red.split("|")
    reci[3] = reci[3].replace("\n","")
    student = Student(reci[0],reci[1],reci[2],reci[3])
    studenti.append(student)
f.close()

for s in studenti: print(s)

