import socket, pickle
from datetime import date
from lek import Lek

def pokupi_informacije_leka_za_slanje():
    id = input("ID leka -> ")
    naziv = input("Naziv leka -> ")
    godina, mesec, dan = input("Godina, mesec, dan proizvodnje u obliku YYYY-MM-DD -> ").split('-')
    lek = Lek(id, naziv, date(int(godina), int(mesec), int(dan)))
    return pickle.dumps(lek)

def pokupi_informaciju_id_leka_za_slanje():
    return input("ID leka -> ").encode()

def iscitaj_lek(odgovor):
    try:
        lek = pickle.loads(odgovor)
        print(lek)
    except:
        print(odgovor.decode())

def pokupi_informacije_sastojci_za_slanje():
    sastojci = input("Sastojci (odvojeni zarezom) -> ").split(',')
    return pickle.dumps(sastojci)

def pokupi_informaciju_za_lokaciju_fajla():
    return input("Putanja fajla -> ").encode()