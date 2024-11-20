from flask import Flask, request, jsonify
from services import listar_reservas_service, reservar_sala_service

app = Flask(__name__)

@app.route('/reservas', methods=['GET'])
def listar_reservas():
    """Exibe a lista de reservas."""
    reservas = listar_reservas_service()
    return jsonify(reservas)

@app.route('/reservas', methods=['POST'])
def reservar_sala():
    """Registra uma nova reserva de sala."""
    data = request.json
    if not data or 'sala' not in data or 'horario' not in data:
        return jsonify({'error': 'Sala e horário são obrigatórios'}), 400
    response = reservar_sala_service(data['sala'], data['horario'])
    return jsonify(response), response.get('status', 201)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)