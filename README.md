# 📚 Sistema de Biblioteca em Python
![Python](https://img.shields.io/badge/Python-3.14.3-blue)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Descrição
Sistema de gerenciamento de biblioteca desenvolvido para praticar manipulação de listas e estruturas de dados em Python.

## Versão 3.0 - Refatoração completa

## ⚙️ Funcionalidades
- Cadastro de livros
- Listagem
- Busca
- Remoção

## ▶️ Como executar

```bash
python main.py
```

## 🛠️ Tecnologias
- Python
- Estruturas de dados (dicionários)

## 📚 Conceitos aplicados

- Estruturas de dados
- Organização modular
- Refatoração de código

## 🎯 Versão anterior

- Gerenciava 3 listas paralelas separadas
- Sincronização manual entre listas
- Difícil manutenção

## 🛠️ Melhorias da v3.0

- Muito mais legível
- Estrutura de dados adequada
- Usa True/False em vez de strings
- Usa funções modulares
- Melhor manutenibilidade

## 🏗️ Arquitetura (v3.0)
```
main()
 └── menu()
      ├── adicionar_livro()
      ├── emprestar_livro()
      ├── devolver_livro()
      ├── ver_livros()
      ├── ver_disponiveis()
      ├── busca_titulo()
      ├── livro_autor()
      └── estatistica()
```

### Conceitos Aplicados

- **Manipulação de dicionários**
- **Estruturas de controle (if/elif/else)**
- **Loops e iterações**
- **Validação de entrada**
- **Booleanos vs Strings**
- **Funções modulares**
- **Main guard pattern**
- **List comprehension**
- **Case-insensitive search**
- **Código testável e manutenível**

## 🔄 Histórico de Commits

- `refactor: modularize code with functions` (v3.0)
- `docs: add comprehensive README` (v2.0)
- `refactor: replace parallel lists with dictionaries` (v2.0)
- `feat: initial library system` (v1.0)

## 📂 Autor

Eduardo Cruz Junior  
Estudante de Análise e Desenvolvimento de Sistemas

## 📫 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/educruzjr/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/edu76666)