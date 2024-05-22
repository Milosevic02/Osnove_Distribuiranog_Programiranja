import socket,pickle

fizickaLica = {}

def dodaj_lice(poruka):
    lice = pickle.loads(poruka)
    if lice.jmbg in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} vec postoji u bazi!"
    else:
        fizickaLica[lice.jmbg] = lice
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} uspesno upisan u bazi!"
    return odgovor.encode()


def izmeni_lice(poruka):
    lice = pickle.loads(poruka)
    if lice.jmbg not in fizickaLica:
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} ne postoji u bazi!"
    else:
        fizickaLica[lice.jmbg] = lice
        odgovor = f"Lice sa jmbg-om: {lice.jmbg} uspesno izmenjen u bazi!"
        
    return odgovor.encode()

    
