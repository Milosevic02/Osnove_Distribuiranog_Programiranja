import hashlib

korisnici = {}

def hesiranje(tekst):
    encode_text = tekst.encode('utf-8')
    hash_tekst = hashlib.sha256(encode_text).hexdigest()
    return hash_tekst


def dodaj_korisnika(ime,lozinka):
    hash_lozinka = hesiranje(lozinka)
    if ime not in korisnici:
        korisnici[ime] = hash_lozinka 
    else:
        print("Neuspesno dodavanje korisnik sa tim imenom vec postoji")
    
def autentifikacija(ime,lozinka):
    if ime in korisnici:
        if hesiranje(lozinka) == korisnici[ime]:
            return True
    return False
