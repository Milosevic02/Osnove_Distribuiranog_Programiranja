import socket, pickle
stanje = ""

lekovi = {}

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

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6000))
    server.listen()
    print("Server je pokrenut.")

    kanal, adresa = server.accept()
    print(f"Prihvacena je konekcija sa adrese: {adresa}")

    while True: 
        opcija = kanal.recv(1024).decode()
        if not opcija : break
        if opcija == "ADD": # Dodaj lek
            odgovor = dodaj_lek(kanal.recv(1024))
        elif opcija == "UPDATE": # Izmeni lek
            odgovor = izmeni_lek(kanal.recv(1024))
        elif opcija == "DELETE": # Obrisi lek
            odgovor = izbrisi_lek(kanal.recv(1024).decode())
        elif opcija == "READ": # Procitaj lek
            odgovor = procitaj_lek(kanal.recv(1024).decode())            
        elif opcija == "READ_ALL": # Pročitaj sve za replikaciju
            pass          
        elif opcija == "WRITE_ALL": # Pročitaj sve za replikaciju
            pass
        try:
            kanal.send(odgovor)
        except Exception as ex:
            print(ex)
    
    print("Server se gasi.")
    server.close()


main()

    
