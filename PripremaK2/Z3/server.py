import socket,pickle

fizickaLica = {}

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

def proictaj_lice(jmbg):
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
    
def main():
    global fizickaLica



    
main()