#!/usr/bin/env python
import socket

def client_thread(client, address):
    while True:
        donnees = client.recv(1024)
        if not donnees:
            print('[' + str(address) + '] connection broke?')
            break

        print('[' + str(address) + '] sent ' + str(donnees))
    client.close()

if __name__ == "__main__":
    print("Starting socket server on localhost:9117")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 80))
    server.listen(5)

    while True:
        (client, address) = server.accept()
        print('[' + str(address) + '] connected')
        ct = client_thread(client, address)
        ct.run()

    server.close()