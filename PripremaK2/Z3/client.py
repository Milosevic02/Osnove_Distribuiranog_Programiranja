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
        
def iscitaj_sva_lica(odgovor):
    try:
        lista = pickle.loads(odgovor)
        for l in lista:
            print(l)
    except:
        print(odgovor.decode())
    
        
        
def main():
    klijentP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    klijentP.connect(('localhost',6000))
    print("Veza sa primarnim serverom je uspostavljena")
    
    while not login(klijentP):
        pass
    
    klijentS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    klijentS.connect(('localhost',7000))
    print("Veza sa sekundarnim serverom je uspostavljena.")
        
    while True: 
        operacija = input("Odaberite operaciju: \n1.Dodaj lice \n2.Izmeni lice \n3.Obrisi lice\n4.Procitaj lice\n5.Procitaj Sortiranu Listu Lica\n6.Repliciraj podatke\n") 
        if not operacija : break        
        if operacija == "1": # Dodaj lek   
            klijentP.send(("ADD").encode())
            odgovor = klijentP.recv(1024).decode()
            if odgovor == "False":
                print("Nemate prava za ovu opciju izaberite neku drugu")
            else:
                klijentP.send(pokupi_informacije_lica_za_slanje())
                print(klijentP.recv(1024).decode())
                
        elif operacija == "2": # Izmeni lek 
            klijentP.send(("UPDATE").encode())
            odgovor = klijentP.recv(1024).decode()
            if odgovor == "False":
                print("Nemate prava za ovu opciju izaberite neku drugu")
            else:
                klijentP.send(pokupi_informacije_lica_za_slanje())
                print(klijentP.recv(1024).decode())
        elif operacija == "3": # Obrisi lek 
            klijentP.send(("DELETE").encode())
            odgovor = klijentP.recv(1024).decode()
            if odgovor == "False":
                print("Nemate prava za ovu opciju izaberite neku drugu")
            else:
                klijentP.send(pokupi_informaciju_jmbg_lica_za_slanje())
                print(klijentP.recv(1024).decode())     
        elif operacija == "4": # Procitaj lek 
            klijentP.send(("READ").encode())
            odgovor = klijentP.recv(1024).decode()
            if odgovor == "False":
                print("Nemate prava za ovu opciju izaberite neku drugu")
            else: 
                klijentP.send(pokupi_informaciju_jmbg_lica_za_slanje())
                iscitaj_lice(klijentP.recv(1024))
        elif operacija == "5":
            klijentP.send(("READ_SORT").encode())
            odgovor = klijentP.recv(1024).decode()
            if odgovor == "False":
                print("Nemate prava za ovu opciju izaberite neku drugu")
            else: 
                iscitaj_sva_lica(klijentP.recv(1024))
        elif operacija == "5":
            try:
                klijentP.send(("READ_ALL").encode())
                klijentS.send(("WRITE_ALL").encode())
                klijentS.send(klijentP.recv(1024))
                
                print(klijentP.recv(1024).decode())
                print(klijentS.recv(1024).decode())
            except Exception as ex:
                print(ex)
                
        else:
            print("Molimo unesite validnu operaciju.")
            continue

    klijentP.close() 
    print("Zatvaranje konekcije.")
    
main()
