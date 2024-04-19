import socket,pickle

profesori = {}

def log_info(message):
    log = open("log.txt","a")
    log.write(message + "\n")
    log.close()
    
def dodaj_profesora(poruka):
    profesor = pickle.loads(poruka)
    if profesor.jmbg in profesori:
        odgovor = f"Profesor sa jmbg {profesor.jmbg} vec postoji u bazi!"
    else:
        profesori[profesor.jmbg] = profesor
        odgovor = f"Profesor sa jmbg {profesor.jmbg}  je sacuvan u bazu!"
    log_info(odgovor)
    return odgovor.encode()

def izmeni_profesora(poruka):
    profesor = pickle.loads(poruka)
    if profesor.jmbg in profesori:
        profesori[profesor.jmbg] = profesor
        odgovor = f"Profesor sa jmbg {profesor.jmbg} izmenjen u bazi!"
    else:
        odgovor = f"Profesor sa jmbg {profesor.jmbg}  ne postoji u bazi!"
    log_info(odgovor)
    return odgovor.encode()

def obrisi(poruka):
    if poruka in profesori:
        del profesori[poruka]
        odgovor = f"Profesor sa JMBG-om: {poruka} je uspesno obrisan"
    else:
        odgovor = f"Profesor sa JMBG-om: {poruka} ne postoji u bazi"
        
    log_info(odgovor)
    return odgovor.encode()

def procitaj(poruka):
    if poruka not in profesori:
        odgovor = f"Profesor sa JMBG-om: {poruka} ne postoji u bazi"
        log_info(odgovor)
    else:
        odgovor = pickle.dump(profesori[poruka])
        return odgovor.encode()

def dodaj_predmete(jmbg,predmeti):
    if jmbg not in profesori:
        odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
    else:
        pr = pickle.loads(predmeti)
        profesori[jmbg].predmeti.extend(pr)
        odgovor = f"Dodati su predmeti za profesora sa JMBG-om: {jmbg}"
    
    log_info(odgovor)
    return odgovor.encode()

def sortiraj(jmbg):
    if jmbg not in profesori:
        odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
    else:
        odgovor = profesori[jmbg].predmeti.sort()
    return odgovor.encode()

def preko20():
    f = open("20god.txt","w")
    retVal = []
    for profesor in profesori.values():
        god = 2024 - int(profesor.datum.year)
        if god >= 20:
            retVal.append(profesor)
            f.write(profesor.__str__())
            
    f.close()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6000))
server.listen()
print("Server je pokrenut")

kanal,adresa = server.accept()
print(f"Prihvacena je konekcija sa adrese: {adresa}")

while True:
    opcija = kanal.recv(1024).decode()
    if not opcija :break
    match opcija:
        case "ADD":
            odgovor = dodaj_profesora(kanal.recv(1024))
        case "EDIT":
            odgovor = izmeni_profesora(kanal.recv(1024))
        case "DELETE":
            odgovor = obrisi(kanal.recv(1024))
        case "READ":
            odgovor = procitaj(kanal.recv(1024))
        case "ADD_SUB":
            jmbg = kanal.recv(1024).decode()
            predmeti = kanal.recv(1024).decode()
            odgovor = dodaj_predmete(jmbg,predmeti)
        case "READ_SORT":
            jmbg = sortiraj(kanal.recv(1024).decode())
        case "20_GOD":
            preko20()
            odgovor = "Procitaj 20god.txt".encode()
            
            
    kanal.send(odgovor)
    
    
print("Server se gasi")    
server.close()