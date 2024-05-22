import socket,pickle
from fizickoLice import FizickoLice

def login(klijent):
    korisnicko_ime = input("Unesite korisnicko ime -> ")
    lozinka = input("Unesite lozinku -> ")
    klijent.send(korisnicko_ime.encode())
    klijent.send(lozinka.encode())
    odgovor = klijent.recv(1024).decode()
    print(odgovor)
    return "Uspesna" in odgovor

def pokupi_informacije_lica_za_slanje():
    jmbg = input("JMBG lica -> ")
    ime = input("Ime lica -> ")
    prezime = input("Prezime lica -> ")
    lice = FizickoLice(jmbg, ime,prezime)
    return pickle.dumps(lice)

def pokupi_informaciju_jmbg_lica_za_slanje():
    return input("JMBG lica -> ").encode()

def iscitaj_lice(odgovor):
    try:
        lice = pickle.loads(odgovor)
        print(lice)
    except:
        print(odgovor.decode())
        
def iscitaj_sva_lica(odgovor)