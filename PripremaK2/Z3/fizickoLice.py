class FizickoLice:
    def __init__(self,jmbg,ime,prezime):
        self.ime = ime
        self.jmbg = jmbg
        self.prezime = prezime
    def __str__(self) -> str:
        return f"{self.ime} {self.prezime} -> {self.jmbg}"