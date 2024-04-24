class Korisnik:
    def __init__(self, ime, lozinka,prava):
        self.ime = ime
        self.lozinka = lozinka
        self.ulogovan = False
        self.prava = prava
