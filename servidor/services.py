from repository import listar_reservas_repo, reservar_sala_repo

def listar_reservas_service():
    """Orquestra a listagem de reservas."""
    return listar_reservas_repo()

def reservar_sala_service(sala, horario):
    """Valida e registra uma reserva."""
    # Verificar se já existe uma reserva para a mesma sala no mesmo horário
    reservas_existentes = listar_reservas_repo()
    for reserva in reservas_existentes:
        if reserva['sala'] == sala and reserva['horario'] == horario:
            return {'error': 'A sala já está reservada para este horário'}, 409
    # Registrar a reserva
    reservar_sala_repo(sala, horario)
    return {'message': 'Reserva realizada com sucesso!'}