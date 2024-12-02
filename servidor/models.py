class Reserva:
    """Representa a entidade de uma Reserva de Sala."""
    def __init__(self, id, sala, horario):
        self.id = id
        self.sala = sala
        self.horario = horario

    def to_dict(self):
        return {'id': self.id, 'sala': self.sala, 'horario': self.horario}