import socket,pickle
from korisnik import Korisnik
import hashlib
fizickaLica = {}

korisnici = {}

def log_info(poruka):
    log = open("log.txt","a")
    log.write(poruka + "\n")
    log.close()

def dodaj_lice(poruka):
    lice = pickle.loads(poruka)
    if lice.jmbg in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} vec postoji u bazi!"
    else:
        fizickaLica[lice.jmbg] = lice
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} uspesno upisan u bazi!"
    log_info(odgovor)
    return odgovor.encode()


def izmeni_lice(poruka):
    lice = pickle.loads(poruka)
    if lice.jmbg not in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} ne postoji u bazi!"
    else:
        fizickaLica[lice.jmbg] = lice
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} uspesno izmenjen u bazi!"
    log_info(odgovor)    
    return odgovor.encode()

def izbrisi_lice(jmbg):
    if jmbg not in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {jmbg} ne postoji u bazi!"
    else:
        del fizickaLica[jmbg]
        odgovor = f"Lice sa jmbg-om: {jmbg} uspesno obrisano iz baze!"
    log_info(odgovor)   
    return odgovor.encode()

def procitaj_lice(jmbg):
    if jmbg not in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {jmbg} ne postoji u bazi!"
        log_info(odgovor)
        return odgovor.encode()
    else:
        odgovor = pickle.dumps(fizickaLica[jmbg])
        return odgovor
    
def procitaj_sve():
    if len(fizickaLica) == 0:
        odgovor = f"Lista je prazna neuspesno citanje"
        log_info(odgovor)
        return odgovor.encode()
    else:
        lica = list(fizickaLica.values())
        sortirana = sorted(lica,key=lambda l:l['prezime'])
        odgovor = pickle.dumps(sortirana)
        return odgovor
    
def hesiranje(tekst):
    return hashlib.sha256(tekst.encode()).hexdigest()

def dodaj_korisnika(korisnicko_ime,lozinka,prava):
    korisnici[korisnicko_ime] = Korisnik(korisnicko_ime,hesiranje(lozinka),prava)
    
def ocitaj_korisnike():
    f = open("Z3/korisnici.txt")
    redovi = f.read().split("\n")
    svi = []
    for r in redovi:
        lista = r.split(";")
        svi.append(lista)
    for k in svi:
        ime = k[0]
        sifra = k[1]
        prava = list(k[2].split(","))
        dodaj_korisnika(ime,sifra,prava)
    f.close()
    
def autentifikacija(korisnicko_ime,lozinka):
    if(korisnicko_ime in korisnici) and (hesiranje(lozinka) == korisnici[korisnicko_ime].lozinka):
        korisnici[korisnicko_ime].autentifikovan = True
        return True
    return False
    
def main():
    ocitaj_korisnike()
    global fizickaLica
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',6000))
    server.listen()
    print("Server je pokrenut")
    
    kanal,adresa = server.accept()
    print(f"Prihvacena je konekcija klijenta sa adrese: {adresa}")

    while True: 
        try:
            
            opcija = kanal.recv(1024).decode()
        except Exception as ex:
            print(ex)
        if not opcija : break
        if opcija == "ADD": # Dodaj lice
            odgovor = dodaj_lice(kanal.recv(1024))
        elif opcija == "UPDATE": # Izmeni lice
            odgovor = izmeni_lice(kanal.recv(1024))
        elif opcija == "DELETE": # Obrisi lice
            odgovor = izbrisi_lice(kanal.recv(1024).decode())
        elif opcija == "READ": # Procitaj lice
            odgovor = procitaj_lice(kanal.recv(1024).decode())            
        elif opcija == "READ_ALL": # Pročitaj sva lica sortirana po prezimenu
            kanal.send(procitaj_sve())
            odgovor = ("Uspesno procitani svi podaci!").encode()             
        try:
            kanal.send(odgovor)
        except Exception as ex:
            print(ex)
    
    print("Server se gasi.")
    server.close()



    
main()