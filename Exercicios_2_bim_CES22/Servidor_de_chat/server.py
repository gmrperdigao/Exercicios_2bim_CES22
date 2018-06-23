##Server for chat application
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming():
    ### Organiza a chegada de novos clientes
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s conectou." % client_address)
        client.send(bytes("Bem-vindo ao chat, agora digite seu nome e aperte enter", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Recebe o socket do cliente como argumento.
    ## Organiza a conexão de um cliente

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Bem-vindo %s! Se você quiser sair, digite {sair}.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s entrou na sala!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{sair}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{sair}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s saiu da sala." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    ## Transmite a msg para todos os clientes

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Esperando conexao...")
    ACCEPT_THREAD = Thread(target=accept_incoming)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()