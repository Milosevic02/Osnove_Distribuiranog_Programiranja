import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 6000))
print("Veza sa serverom je uspostavljena.")

while True:
    poruka = input("Unesite izraz:")
    if not poruka : break
    klijent.send(poruka.encode())
    odgovor = klijent.recv(1024).decode()
    print(f"Rezultat je : {odgovor}")
print("Konekcija se zatvara.")
klijent.close()