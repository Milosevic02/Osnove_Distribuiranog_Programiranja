# KLASE (str. 37)
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