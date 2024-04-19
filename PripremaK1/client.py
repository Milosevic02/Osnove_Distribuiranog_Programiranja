import socket,pickle
from datetime import date
from profesor import Profesor

def pokupi_objekat():
    jmbg = input("jmbg leka -> ")
    ime = input("Ime ->")
    prezime = input("Prezime->")
    godina, mesec, dan = input("Godina, mesec, dan proizvodnje u obliku YYYY-MM-DD -> ").split('-')
    profesor = Profesor(jmbg,ime,prezime,date(int(godina),int(mesec),int(dan)))
    return pickle.dumps(profesor)

klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klijent.connect(('localhost',6000))
print("Veza sa serverom uspostavljena")


while True:
    poruka = input("Unesi poruku")
    klijent.send(poruka.encode())
