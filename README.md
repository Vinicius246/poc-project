# Para executar rode os seguintes comandos

python client.py
python server.py

poc-project/
├── server/
│   ├── app.py              # Principal do Flask, contém rotas para as funcionalidades
│   ├── firebase_config.py  # Configuração do Firebase
│   ├── templates/
│   │   ├── index.html      # Página inicial com opções
│   │   ├── listar.html     # Página para listar auditórios
│   │   ├── reservar.html   # Página para fazer reservas
│   │   ├── cancelar.html   # Página para cancelar reservas
│   └── static/
│       ├── styles.css      # Estilos CSS para melhorar o visual
├── tests/                  # Testes da aplicação
│   ├── test_routes.py      # Testes para as rotas Flask
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── setup.py                # Configuração do projeto
