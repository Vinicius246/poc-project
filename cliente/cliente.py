import requests
import sys

SERVER_URL = "http://127.0.0.1:5000"

def listar_reservas():
    """Lista todas as reservas no servidor."""
    response = requests.get(f"{SERVER_URL}/reservas")
    if response.status_code == 200:
        reservas = response.json()
        print("Reservas cadastradas:")
        for r in reservas:
            print(f"ID: {r['id']}, Sala: {r['sala']}, Horário: {r['horario']}")
    else:
        print(f"Erro ao listar reservas: {response.status_code}")

def reservar_sala(sala, horario):
    """Registra uma nova reserva no servidor."""
    data = {"sala": sala, "horario": horario}
    response = requests.post(f"{SERVER_URL}/reservas", json=data)
    if response.status_code == 201:
        print("Reserva realizada com sucesso!")
    else:
        print(f"Erro ao reservar sala: {response.json()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python cliente.py listar            - Listar reservas")
        print("  python cliente.py reservar <sala> <horario> - Reservar sala")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "listar":
        listar_reservas()
    elif comando == "reservar" and len(sys.argv) == 4:
        sala = sys.argv[2]
        horario = sys.argv[3]
        reservar_sala(sala, horario)
    else:
        print("Comando inválido ou argumentos insuficientes.")