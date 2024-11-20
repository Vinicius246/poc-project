import socket
import json

def conectar_servidor(comando: str) -> str:
    """Conecta ao servidor e envia um comando."""
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 9090))
    cliente.send(comando.encode('utf-8'))
    resposta = cliente.recv(4096).decode('utf-8')  # Aumentado o buffer para 4096 bytes
    cliente.close()

    if not resposta.strip():  # Verifica se a resposta é vazia
        print("Nenhuma resposta recebida do servidor.")
        return ""

    return resposta

def listar_auditorios() -> dict:
    """Lista os auditórios disponíveis e retorna um dicionário numerado."""
    resposta = conectar_servidor("LIST")
    try:
        auditorios = json.loads(resposta)  # Resposta deve ser uma lista de dicionários
        if isinstance(auditorios, list):
            print("=== Lista de Auditórios Disponíveis ===")
            numerados = {}
            for index, audit in enumerate(auditorios, start=1):
                nome = audit.get('nome', 'Desconhecido')
                capacidade = audit.get('capacidade', {})
                lugares_sentados = capacidade.get('lugares_sentados', 'N/A')
                lugares_cadeirantes = capacidade.get('lugares_para_cadeirantes', 0)
                horarios = ", ".join(audit.get('horarios_disponiveis', []))
                print(
                    f"{index}. Nome: {nome}\n"
                    f"   Capacidade: {lugares_sentados} lugares sentados, {lugares_cadeirantes} para cadeirantes\n"
                    f"   Horários disponíveis: {horarios}\n"
                    "----------------------------------------"
                )
                numerados[index] = audit
            return numerados
        else:
            print("Erro: Resposta inesperada do servidor.")
            return {}
    except json.JSONDecodeError:
        print(f"Erro ao processar resposta do servidor: {resposta}")
        return {}

def reservar_auditorio() -> None:
    """Permite ao usuário selecionar um auditório e horário para reserva."""
    auditorios = listar_auditorios()
    if not auditorios:
        return

    try:
        escolha = int(input("Selecione o número do auditório: "))
        if escolha not in auditorios:
            print("Número inválido! Tente novamente.")
            return
        auditorio = auditorios[escolha]
        nome = auditorio.get('nome', 'Desconhecido')

        data = input("Informe a data (YYYY-MM-DD): ")
        horario = input("Informe o horário (HH:MM): ")

        comando = f"RESERVE {escolha} {data} {horario}"
        resposta = conectar_servidor(comando)
        print(resposta)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def cancelar_reserva() -> None:
    """Permite ao usuário cancelar uma reserva."""
    auditorios = listar_auditorios()
    if not auditorios:
        return

    try:
        escolha = int(input("Selecione o número do auditório: "))
        if escolha not in auditorios:
            print("Número inválido! Tente novamente.")
            return
        auditorio = auditorios[escolha]
        nome = auditorio.get('nome', 'Desconhecido')

        data = input("Informe a data (YYYY-MM-DD): ")
        horario = input("Informe o horário (HH:MM): ")

        comando = f"CANCEL {escolha} {data} {horario}"
        resposta = conectar_servidor(comando)
        print(resposta)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def menu() -> None:
    """Exibe o menu principal."""
    print("=== Sistema de Locação de Auditórios ===")
    print("1. Listar auditórios")
    print("2. Reservar auditório")
    print("3. Cancelar reserva")
    print("4. Sair")

def main() -> None:
    """Função principal para interação com o usuário."""
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_auditorios()
        elif opcao == "2":
            reservar_auditorio()
        elif opcao == "3":
            cancelar_reserva()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
