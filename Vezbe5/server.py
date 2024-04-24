import socket,pickle

lekovi = {}

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
