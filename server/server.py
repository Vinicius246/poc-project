import socket
import json
from firebase_admin import firestore
from firebase_config import db  # Arquivo firebase_config.py com a configuração do Firestore

def carregar_auditorios():
    """Carrega os auditórios do Realtime Database."""
    ref = db.reference('auditorios')
    auditorios = ref.get()  # Retorna os dados como um dicionário
    if auditorios is None:
        return []
    return auditorios


def processar_comando(comando):
    """Processa os comandos recebidos do cliente."""
    partes = comando.strip().split()
    operacao = partes[0].upper()

    if operacao == "LIST":
        # Listar auditórios
        auditorios = carregar_auditorios()  # Deve retornar uma lista
        resposta = ["=== Lista de Auditórios Disponíveis ==="]
        for index, audit in enumerate(auditorios, start=1):
            nome = audit.get('nome', 'Desconhecido')
            capacidade = audit.get('capacidade', {})
            lugares_sentados = capacidade.get('lugares_sentados', 'N/A')
            lugares_cadeirantes = capacidade.get('lugares_para_cadeirantes', 0)
            horarios = ", ".join(audit.get('horarios_disponiveis', []))
            detalhes = (
                f"{index}. Nome: {nome}\n"
                f"   Capacidade: {lugares_sentados} lugares sentados, {lugares_cadeirantes} para cadeirantes\n"
                f"   Horários disponíveis: {horarios}\n"
                "----------------------------------------"
            )
            resposta.append(detalhes)
        return "\n".join(resposta)

    # Outras operações (RESERVE e CANCEL) seguem

def iniciar_servidor():
    """Inicia o servidor e aguarda conexões."""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 9090))
    servidor.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        cliente, _ = servidor.accept()
        comando = cliente.recv(1024).decode('utf-8')
        resposta = processar_comando(comando)
        cliente.send(resposta.encode('utf-8'))
        cliente.close()

if __name__ == "__main__":
    iniciar_servidor()
