import socket, pickle
from lek import Lek

lekovi = {}
lekovi[1] = Lek(1, "Lek broj jedan", "2024-04-05")
lekovi[2] = Lek(2, "Lek broj dva", "2024-04-08")
lekovi[3] = Lek(3, "Lek broj tri", "2024-04-06")

def log_info(message):
    # Log
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

def pisi_u_fajl(naziv_datoteke, rezim_otvaranja, podaci = lekovi):
    f = open(naziv_datoteke, rezim_otvaranja)
    pickle.dump(podaci, f)
    f.close()

def procitaj_iz_fajla(naziv_datoteke, rezim_otvaranja):
    f = open(naziv_datoteke, rezim_otvaranja)
    data = pickle.loads(f)
    f.close()
    return data