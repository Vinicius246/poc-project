import socket
import threading
from server import iniciar_servidor


def test_servidor_responde() -> None:
    server_thread = threading.Thread(target=iniciar_servidor, daemon=True)
    server_thread.start()

    cliente: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9090))
    cliente.send(b"Teste")
    resposta: bytes = cliente.recv(1024)
    cliente.close()

    assert resposta.decode('utf-8') == "Mensagem recebida com sucesso!"
