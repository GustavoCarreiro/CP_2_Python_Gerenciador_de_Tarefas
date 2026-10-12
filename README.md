# 📋 Gerenciador de Tarefas.

Repositório estruturado para demonstrar boas práticas de desenvolvimento de software em Python, utilizando **arquitetura em camadas**, **persistência de dados em JSON**, **validação de entradas** e **controle de versão profissional**.

---

## 🛠️ Tecnologias Utilizadas:

- [x] **Linguagem:** Python 3
- [x] **Modularização:** Separação de responsabilidades em múltiplos arquivos (`Interface`, `Tarefas`, `Persistencia`).
- [x] **Persistência de Dados:** Manipulação de arquivos JSON utilizando as bibliotecas nativas `json` e `os`.
- [x] **Validação e Tipagem:** Validação estrita de datas via `datetime` e controle de status por listas restritas. 
- [x] **Engenharia de Software:** Uso do padrão de **Conventional Commits** para o histórico de versionamento.

---

## 📂 Arquitetura e Estrutura do Projeto.

O projeto é dividido em três camadas lógicas independentes:

```text
📦 Gerenciador de Tarefas
 ┣ 📜 Interface.py          # Camada de Apresentação (Menus, inputs, exibições)
 ┣ 📜 Tarefas.py            # Camada de Regras de Negócio (Lógica, validações e manipulação)
 ┣ 📜 Persistencia.py       # Camada de Dados (Leitura e escrita em JSON)
 ┣ 📜 .gitignore            # Arquivos ignorados pelo Git (cache e banco local)
 ┗ 📜 tarefas_cadastradas.json # Banco de dados local em formato JSON (gerado automaticamente)
```

---

## 👥 Integrantes do Grupo:

- **Gustavo Carreiro** | RM 576379
- **Manuela Prieto Fazzato** | RM 576587
- **Naiara Sousa Soares** | RM 574792
- **Lucas Longo Rosette** | RM 576306
