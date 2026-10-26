import os

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")