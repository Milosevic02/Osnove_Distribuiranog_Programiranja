import socket,pickle
import direktorijum_korisnika as dk
from korisnik import Korisnik

lekovi = {}
dk.dodaj_korisnika("Pera","pera",["ADD","UPDATE"])
dk.dodaj_korisnika("Zika","zika",["ADD","UPDATE","DELETE"])
dk.dodaj_korisnika("Djole","djole",["ADD","UPDATE","DELETE","READ","ADD_INGR"])



def log_info(message):
    log = open("log.txt", "a")
    log.write(message + "\n")
    log.close()
    
def dodaj_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} vec postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno upisan u bazu."
    log_info(odgovor)
    return odgovor.encode()

def izmeni_lek(poruka):
    lek = pickle.loads(poruka)
    if lek.id not in lekovi:
        odgovor = f"Lek sa id-em: {lek.id} ne postoji u bazi!"
    else:
        lekovi[lek.id] = lek
        odgovor = f"Lek sa id-em: {lek.id} uspesno izmenjen."
    log_info(odgovor)
    return odgovor.encode()

def izbrisi_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
    else:
        del lekovi[id]
        odgovor = f"Lek sa id-em: {id} uspesno obrisan."
    log_info(odgovor)
    return odgovor.encode()

def procitaj_lek(id):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
        log_info(odgovor)
        return odgovor.encode()
    else:
        odgovor = pickle.dumps(lekovi[id])
        return odgovor
    
def dodaj_sastojke(id, podaci):
    if id not in lekovi:
        odgovor = f"Lek sa id-em: {id} ne postoji u bazi!"
    else:
        sastojci = pickle.loads(podaci)
        lekovi[id].sastojci.extend(sastojci)
        odgovor = f"Uspesno dodati sastojci za lek sa id-em: {id}."
        print(odgovor)
    log_info(odgovor)
    return odgovor.encode()

def ocitaj_korisnika(k):
    korisnik = pickle.loads(k)
    return korisnik

def proveri_korisnika(k):
    korisnik = ocitaj_korisnika(k)
    return dk.autentifikacija(korisnik.ime,korisnik.lozinka)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6000))
    server.listen()
    print("Server je pokrenut.")

    kanal, adresa = server.accept()
    print(f"Prihvacena je konekcija sa adrese: {adresa}")
    autentifikacija = False
    ulogovan = False

    while True: 
        if not ulogovan:
            while(not autentifikacija):
                odgovor = kanal.recv(1024)
                autentifikacija = proveri_korisnika(odgovor)
                if not autentifikacija : kanal.send(("False").encode())
            kanal.send(("True").encode())
            ulogovan = True
            temp_korisnik = ocitaj_korisnika(odgovor)
            
        opcija = kanal.recv(1024).decode()
        if not opcija : break
        if opcija not in dk.korisnici[temp_korisnik.ime].prava:
            kanal.send(("False").encode())
        else:
            kanal.send(("True").encode())
            if opcija == "ADD": # Dodaj lek
                odgovor = dodaj_lek(kanal.recv(1024))
            elif opcija == "UPDATE": # Izmeni lek
                odgovor = izmeni_lek(kanal.recv(1024))
            elif opcija == "DELETE": # Obrisi lek
                odgovor = izbrisi_lek(kanal.recv(1024).decode())
            elif opcija == "READ": # Procitaj lek
                odgovor = procitaj_lek(kanal.recv(1024).decode())            
            elif opcija == "ADD_INGR": # Dodaj sastojke
                id = kanal.recv(1024).decode()
                sastojci = kanal.recv(1024)
                odgovor = dodaj_sastojke(id, sastojci)        
            kanal.send(odgovor)
    
    print("Server se gasi.")
    server.close()


main()