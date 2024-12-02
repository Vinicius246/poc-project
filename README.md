    arquitetura_em_camadas_aluguel/
    │
    ├── servidor/
    │   ├── app.py         # Camada de Apresentação (APIs REST)
    │   ├── services.py    # Camada de Aplicação (regras de negócio)
    │   ├── models.py      # Camada de Domínio (representação das entidades)
    │   ├── repository.py  # Camada de Persistência (interação com o banco)
    │   ├── database.db    # Banco de dados SQLite
    │
    └── cliente/
        ├── cliente.py     # Script cliente CLI

