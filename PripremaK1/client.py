import socket,pickle,json
from datetime import date
from profesor import Profesor

#1,2
def pokupi_objekat():
    jmbg = input("jmbg profesora -> ")
    ime = input("Ime ->")
    prezime = input("Prezime->")
    godina, mesec, dan = input("Godina, mesec, dan proizvodnje u obliku YYYY-MM-DD -> ").split('-')
    profesor = Profesor(jmbg,ime,prezime, date(int(godina), int(mesec), int(dan)).isoformat())
    
    return pickle.dumps(profesor)

#3,4,6
def pokupi_jmbg():
    return input("JMBG ->").encode()

#5
def pokupi_predmete():
    predmeti = input("unesi predmete odvojene zarezom").split(",")
    return pickle.dumps(predmeti)


def ispisi_profesora(poruka):
        try:
                profesor = pickle.loads(poruka)
                print(profesor)
        except:
                print(poruka.decode())


klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klijent.connect(('localhost',6000))
print("Veza sa serverom uspostavljena")


while True:
    operacija = input("\nIzaberi opciju:\n 1.Dodaj profesora \n 2.Izmeni profesora\n 3.Obrisi profesora\n 4.Pronadji profesora\n 5.Dodaj predmete profesoru\n 6.Procitaj predmete profesora\n 7.Svi profesori zaposleni duze od 20 godina\n")
    if not operacija : break
    if operacija == "1":
        klijent.send(("ADD").encode())
        klijent.send(pokupi_objekat())
        print(klijent.recv(1024).decode())
    elif operacija == "2":
        klijent.send(("EDIT").encode())
        klijent.send(pokupi_objekat())
        print(klijent.recv(1024).decode())
    elif operacija == "3":
        klijent.send(("DELETE").encode())
        klijent.send(pokupi_jmbg())
        print(klijent.recv(1024).decode())
    elif operacija == "4":
        klijent.send(("READ").encode())
        klijent.send(pokupi_jmbg())
        ispisi_profesora(klijent.recv(1024).decode())
    elif operacija == "5":
        klijent.send(("ADD_SUB").encode())
        klijent.send(pokupi_jmbg())
        klijent.send(pokupi_predmete())
        print(klijent.recv(1024).decode())
    elif operacija == "6":
        klijent.send(("READ_SORT").encode())
        klijent.send(pokupi_jmbg())
        print(klijent.recv(1024).decode())


    else:
        print("Molimo unesite validnu operaciju.")
        continue
    

print("Zatvaranje konekcije.") 
klijent.close()

