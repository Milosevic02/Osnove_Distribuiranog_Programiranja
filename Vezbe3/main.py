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

