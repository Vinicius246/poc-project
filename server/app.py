from flask import Flask, render_template, request, redirect, url_for, jsonify
from firebase_config import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar', methods=['GET'])
def listar_auditorios():
    auditorios_ref = db.reference('auditorios')
    auditorios = auditorios_ref.get()
    return render_template('listar.html', auditorios=auditorios)

@app.route('/reservar', methods=['GET', 'POST'])
def reservar_auditorio():
    if request.method == 'POST':
        auditorio_id = request.form['auditorio_id']
        data = request.form['data']
        horario = request.form['horario']

        reservas_ref = db.reference(f'reservas/{auditorio_id}')
        reservas = reservas_ref.get() or {}

        if horario in reservas.get(data, []):
            return "Horário já reservado!", 409

        reservas.setdefault(data, []).append(horario)
        reservas_ref.set(reservas)

        return redirect(url_for('listar_auditorios'))
    
    # Filtrar auditórios com horários disponíveis
    auditorios_ref = db.reference('auditorios')
    auditorios = auditorios_ref.get()

    auditorios_disponiveis = []
    if isinstance(auditorios, list):  # Caso seja uma lista
        for index, auditorio in enumerate(auditorios):
            if auditorio.get('horarios_disponiveis'):  # Verifica se há horários
                auditorios_disponiveis.append({
                    "id": index,  # Usando o índice como identificador
                    "nome": auditorio.get('nome', f"Auditório {index}"),
                    "horarios": auditorio['horarios_disponiveis']
                })
    elif isinstance(auditorios, dict):  # Caso seja um dicionário
        for auditorio_id, auditorio in auditorios.items():
            if auditorio.get('horarios_disponiveis'):
                auditorios_disponiveis.append({
                    "id": auditorio_id,
                    "nome": auditorio['nome'],
                    "horarios": auditorio['horarios_disponiveis']
                })

    return render_template('reservar.html', auditorios=auditorios_disponiveis)

@app.route('/cancelar', methods=['GET', 'POST'])
def cancelar_reserva():
    if request.method == 'POST':
        auditorio_id = request.form['auditorio_id']
        data = request.form['data']
        horario = request.form['horario']

        reservas_ref = db.reference(f'reservas/{auditorio_id}')
        reservas = reservas_ref.get() or {}

        if data in reservas and horario in reservas[data]:
            reservas[data].remove(horario)
            if not reservas[data]:  # Remove a data se não houver horários restantes
                reservas.pop(data)
            reservas_ref.set(reservas)
            return redirect(url_for('listar_auditorios'))
        return "Reserva não encontrada!", 404
    return render_template('cancelar.html')

if __name__ == "__main__":
    app.run(debug=True)
