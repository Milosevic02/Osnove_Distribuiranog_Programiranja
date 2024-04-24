import socket,pickle

lekovi = {}

def log_info(message):
    log = open("log.txt", "a")
    log.write(message + "\n")
    log.close()