import hashlib
from korisnik import Korisnik

korisnici = {}

def hesiranje(tekst):
    encode_text = tekst.encode('utf-8')
    hash_tekst = hashlib.sha256(encode_text).hexdigest()
    return hash_tekst


def dodaj_korisnika(ime,lozinka,prava):
    hash_lozinka = hesiranje(lozinka)
    if ime not in korisnici:
        korisnici[ime] = Korisnik(ime,hash_lozinka,prava)
    else:
        print("Neuspesno dodavanje korisnik sa tim imenom vec postoji")
    
def autentifikacija(ime,lozinka):
    if ime in korisnici:
        if hesiranje(lozinka) == korisnici[ime].lozinka:
            return True
    return False
