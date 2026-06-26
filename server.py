import socket
import os
import tempfile

def server():
    # Caminho único na pasta temporária
    caminho_temp = os.path.join(tempfile.gettempdir(), "dados.txt")

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Evita o erro de porta já em uso ao reiniciar
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('127.0.0.1', 5000))
    servidor.listen(5)

    print("[SERVIDOR] Aguardando conexões brutas na porta 5000...")

    # Garante que o arquivo existe
    if not os.path.exists(caminho_temp):
        with open(caminho_temp, "w", encoding="utf-8") as f:
            f.write("Aguardando dados...\n")

    while True:
        conexao, cliente = servidor.accept()
        
        try:
            # Recebe os dados brutos da requisição
            requisicao = conexao.recv(2048).decode('utf-8', errors='ignore')
            
            if requisicao:
                # SE FOR O NAVEGADOR (LIVE SERVER) PEDINDO OS DADOS
                if "GET" in requisicao:
                    with open(caminho_temp, "r", encoding="utf-8") as arquivo:
                        conteudo = arquivo.read()
                    
                    # Monta a resposta HTTP perfeita para o navegador aceitar sem dar timeout ou CORS
                    resposta = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/plain; charset=utf-8\r\n"
                        "Access-Control-Allow-Origin: *\r\n"
                        f"Content-Length: {len(conteudo.encode('utf-8'))}\r\n"
                        "Connection: close\r\n"
                        "\r\n"
                        f"{conteudo}"
                    )
                    conexao.sendall(resposta.encode('utf-8'))
                
                # SE FOR O SEU OUTRO SCRIPT ENVIANDO INFORMAÇÕES
                else:
                    print("\n--- Nova Informação Recebida ---")
                    print(requisicao)
                    
                    # Salva no arquivo temporário oculto
                    with open(caminho_temp, "a", encoding="utf-8") as arquivo:
                        arquivo.write(f"{requisicao}\n")
                    
                    # Responde pro script que deu tudo certo
                    resposta = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
                    conexao.sendall(resposta.encode('utf-8'))
                    
        except Exception as e:
            print(f"Erro ao processar conexão: {e}")
        finally:
            # ISSO DAQUI É O MAIS IMPORTANTE: Fecha a conexão pro navegador não dar timeout!
            conexao.close()
