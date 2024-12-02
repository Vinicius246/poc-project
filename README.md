
# **Projeto PoC - Arquitetura Cliente-Servidor**

Este projeto é uma Prova de Conceito (PoC) desenvolvida para demonstrar uma aplicação baseada na arquitetura **Cliente-Servidor**, utilizando padrões de projeto, princípios de **SOLID**, e **Clean Code**.

---

## **Sumário**
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura](#arquitetura)
- [Como Executar](#como-executar)
- [Padrões de Projeto e Princípios Adotados](#padrões-de-projeto-e-princípios-adotados)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## **Sobre o Projeto**
Este sistema tem como objetivo gerenciar **reservas de salas**, centralizando a lógica de negócios em um servidor enquanto o cliente oferece uma interface para interação. A aplicação foi desenvolvida com o objetivo de aplicar boas práticas de desenvolvimento de software.

---

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **Flask**: Framework para criação do servidor e API REST.
- **SQLite**: Banco de dados para persistência de informações.
- **Requests**: Biblioteca para realizar chamadas HTTP no cliente.

---

## **Arquitetura**
A aplicação segue o padrão **Cliente-Servidor**:
- **Servidor**: 
  - Implementa a API REST para gerenciar reservas.
  - Utiliza o padrão **Service Layer** para a lógica de negócios e o padrão **Repository** para o acesso aos dados.
- **Cliente**: 
  - Fornece uma interface de linha de comando para interação com o servidor.

---

## **Como Executar**
### **Pré-requisitos**
- Python 3.8 ou superior
- Ambiente virtual configurado

### **Passos para execução**
1. **Clone o repositório**:
   ```bash
   git clone <link-do-repositorio>
   cd poc-project-develop
   ```

2. **Configure o ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências necessárias**:
   ```bash
   pip install flask requests
   ```

4. **Inicialize o banco de dados**:
   ```bash
   python servidor/repository.py
   ```

5. **Inicie o servidor**:
   ```bash
   python servidor/app.py
   ```

6. **Execute o cliente**:
   ```bash
   python cliente/cliente.py
   ```

---

## **Padrões de Projeto e Princípios Adotados**
### **Padrões de Projeto**:
- **Repository**: Organização do acesso ao banco de dados.
- **Service Layer**: Centralização da lógica de negócios.
- **Controller**: Gerenciamento de rotas no servidor.

### **Princípios de SOLID**:
- **Responsabilidade Única (SRP)**: Separação clara entre camadas.
- **Inversão de Dependência (DIP)**: Componentes dependem de abstrações.

### **Princípios de Clean Code**:
- Código modular e legível.
- Funções pequenas e específicas.
- Nomes autoexplicativos.

---

## **Contribuições**
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Submeta um pull request.

---

## **Licença**
Este projeto está sob a licença [MIT](LICENSE).
