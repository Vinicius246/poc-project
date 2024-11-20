import sys
from pathlib import Path

from flask import app

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent.resolve()))

from server.firebase_config import db

# Resto do código
if __name__ == "__main__":
    app.run(debug=True, port=5000)