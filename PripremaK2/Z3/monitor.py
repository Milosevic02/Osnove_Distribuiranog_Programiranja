import socket

def azuriraj_stanje(socket,stanje):
    socket.send(stanje.encode())
    print(socket.recv(1024).decode())
    
def main():
    monitorP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    monitorS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        monitorP.connect(('localhost',6000))
        print("Veza sa primarnim serverom je uspostavljena")
        
        azuriraj_stanje(monitorP,'primarni')
    except Exception as ex:
        print(ex)
        
    try:
        monitorS.connect(('localhost',7000))
        print("Veza sa sekundarnim serverom je uspostavljena.")

        azuriraj_stanje(monitorS, "sekundarni")
    except Exception as ex:
        print(ex)
        
    print("Zatvaranje konekicja.")
    monitorP.close()
    monitorS.close()


main()    