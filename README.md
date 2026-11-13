# Projeto Base - Banco de Dados I - FMP
## Versão dos alunos

Este projeto contém a **estrutura inicial** da mini aplicação acadêmica que será desenvolvida na Unidade Final de Banco de Dados I.

O objetivo NÃO é apenas fazer a tela abrir. O grupo deverá completar o banco, as operações SQL e as consultas solicitadas, compreendendo o fluxo:

**Interface → Python → SQL parametrizado → PostgreSQL → Resultado → Interface**

---

## O que já está pronto

- estrutura de pastas;
- conexão com PostgreSQL em `db.py`;
- dependência Psycopg 3;
- interface Tkinter/ttk;
- tabela `CIDADE` como exemplo de modelo físico;
- carga inicial de cidades e cursos;
- `listar_cidades()` e `listar_cursos()` como exemplos de `SELECT`;
- `inserir_aluno()` como exemplo completo de `INSERT` parametrizado.

## O que o grupo deve desenvolver

### Modelo físico
- `CURSO`;
- `ALUNO`;
- `MATRICULA`;
- PKs, FKs, `NOT NULL`, `UNIQUE` e regras de integridade.

### CRUD de ALUNO
- listar;
- atualizar;
- excluir.

> O `INSERT` de aluno já está pronto como exemplo.

### MATRICULA
- cadastrar;
- atualizar data;
- excluir.

### JOIN
Criar uma consulta que mostre:
- aluno;
- curso;
- sigla;
- data da matrícula;
- cidade.

### Consulta de negócio
Exibir todos os cursos e a quantidade de alunos matriculados, inclusive cursos com total zero.

---

## Arquivos

```text
Projeto_Base_BDI_FMP_ALUNOS/
├── app.py
├── db.py
├── repositories.py
├── requirements.txt
├── .env.example
├── INSTRUCOES_ALUNOS.md
└── sql/
    ├── 00_create_database.sql
    ├── 01_schema.sql
    └── 02_seed.sql
```

---

## Ordem de trabalho

1. Leia `INSTRUCOES_ALUNOS.md`.
2. Crie o banco com `sql/00_create_database.sql`.
3. Complete `sql/01_schema.sql`.
4. Execute `sql/02_seed.sql`.
5. Valide as tabelas no pgAdmin.
6. Configure a conexão Python/PostgreSQL.
7. Execute `python app.py`.
8. Teste o `INSERT` de aluno fornecido como exemplo.
9. Complete os TODOs de `repositories.py`.
10. Teste cada funcionalidade pela interface.

---

## Preparar o Python

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois:

```bash
pip install -r requirements.txt
python -m tkinter
```

Configure a senha do PostgreSQL:

```powershell
$env:DB_PASSWORD="sua_senha"
python app.py
```

> Nunca envie a senha real do banco no Classroom ou em repositório público.

---

## Regra importante

Não substitua os TODOs por código copiado sem compreender.

Na apresentação, o grupo deverá explicar:
- por que cada tabela existe;
- onde estão PKs e FKs;
- qual SQL cada botão executa;
- como funciona o JOIN;
- como o dado chega ao PostgreSQL;
- por que o SQL é parametrizado.
