# 🎬 Rede de Cinemas - Engenharia de Software

Sistema desenvolvido para a disciplina de Engenharia de Software com o objetivo de gerenciar uma rede de cinemas utilizando arquitetura em camadas, UML e persistência em banco de dados SQLite.

---

# 📚 Objetivo do Projeto

O sistema foi desenvolvido para auxiliar no gerenciamento de:

- Filmes em cartaz;
- Cinemas da rede;
- Sessões;
- Controle de público;
- Consultas de informações.

---

# 🛠 Tecnologias Utilizadas

- Python
- SQLite
- Git
- GitHub
- PlantUML
- VS Code

---

# 🧱 Arquitetura Utilizada

O projeto utiliza:

- MVC (Model View Controller)
- Service Layer
- Repository Pattern

Fluxo da aplicação:

```txt
View -> Controller -> Service -> Repository -> SQLite
```

---

# 📂 Estrutura do Projeto

```txt
RedeCinemas_Atvd/
│
├── docs/
│   ├── requisitos.md
│   ├── caso-de-uso.png
│   ├── diagrama-classes.png
│   ├── sequencia.png
│   └── atividade.png
│
├── src/
│   ├── controller/
│   ├── model/
│   ├── service/
│   ├── repository/
│   ├── database/
│   └── main.py
│
└── README.md
```

---

# ✅ Funcionalidades

- Cadastro de filmes
- Listagem de filmes
- Cadastro de cinemas
- Listagem de cinemas
- Cadastro de sessões
- Listagem de sessões
- Controle de capacidade do cinema

---

# 📋 Regras de Negócio

- O público da sessão não pode ultrapassar a capacidade do cinema;
- Filmes podem possuir várias sessões;
- Cinemas podem possuir várias sessões;
- Toda sessão deve estar vinculada a um filme e a um cinema.

---

# 🗄 Banco de Dados

O sistema utiliza SQLite para persistência dos dados.

Tabelas:
- filmes
- cinemas
- sessoes

---

# ▶ Como Executar

## 1. Clonar o repositório

```bash
git clone LINK_DO_SEU_REPOSITORIO
```

## 2. Executar o banco

```bash
python src/database/database.py
```

## 3. Executar o sistema

```bash
python src/main.py
```

---

# 📌 Diagramas UML

O projeto contém:

- Diagrama de Casos de Uso
- Diagrama de Classes
- Diagrama de Sequência
- Diagrama de Atividade

---

# 👨‍💻 Autor

Calebe Matheus Moreira Moraes para a disciplina de Engenharia de Software.