import socket,pickle

profesori = {}

def log_info(message):
    log = open("log.txt","a")
    log.write(message + "\n")
    log.close()
    
def dodaj_lek(poruka):
    profesor = pickle.loads(poruka)
    if profesor.jmbg in profesori:
        odgovor = f"Profesor sa jmbg {profesor.jmbg} vec postoji u bazi!"
    else:
        profesori[profesor.jmbg] = profesor
        odgovor = f"Profesor sa jmbg {profesor.jmbg}  je sacuvan u bazu!"
    log_info(odgovor)
    return odgovor.encode()

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
            odgovor = dodaj_lek(kanal.recv(1024))
            
    kanal.send(odgovor)
    
    
print("Server se gasi")    
server.close()