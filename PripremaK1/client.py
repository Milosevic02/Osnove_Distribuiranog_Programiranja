import socket,pickle,json
from datetime import date
from profesor import Profesor

#1,2
def pokupi_objekat():
    jmbg = input("jmbg leka -> ")
    ime = input("Ime ->")
    prezime = input("Prezime->")
    godina, mesec, dan = input("Godina, mesec, dan proizvodnje u obliku YYYY-MM-DD -> ").split('-')
    profesor = Profesor(jmbg,ime,prezime,date(int(godina),int(mesec),int(dan)))
    f = open("profesor.json",'w')
    json.dump(profesor.__dict__,f)
    f.close()
    
    f = open("profesor.json")
    profesor_json = json.load(f)
    f.close()
    
    return pickle.dumps(profesor_json)

#3,4,6
def pokupi_jmbg():
    return input("JMBG ->").encode()

#5


klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klijent.connect(('localhost',6000))
print("Veza sa serverom uspostavljena")


while True:
    poruka = input("Unesi poruku")
    klijent.send(poruka.encode())
