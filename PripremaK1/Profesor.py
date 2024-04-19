class Profesor:
    def __init__(self,jmbg,ime,prezime,datum):
        self.jmbg = jmbg
        self.ime = ime
        self.prezime = prezime
        self.datum = datum
        self.predmeti = []
        
    def __str__(self) -> str:
        return f"{self.jmbg} - {self.ime} - {self.prezime} - {self.datum},predmeti: {self.predmeti}"
        