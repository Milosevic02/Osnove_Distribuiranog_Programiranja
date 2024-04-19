import socket

klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klijent.connect(('localhost',6000))
print("Veza sa serverom uspostavljena")


while True:
    poruka = input("Unesi poruku")
    klijent.send(poruka.encode())
