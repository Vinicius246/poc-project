from client.client import conectar_servidor
from server.server import iniciar_servidor
import threading


def test_cliente_conecta() -> None:
    server_thread = threading.Thread(target=iniciar_servidor, daemon=True)
    server_thread.start()

    try:
        conectar_servidor()
        assert True
    except Exception as e:
        assert False, f"Erro ao conectar cliente: {e}"
