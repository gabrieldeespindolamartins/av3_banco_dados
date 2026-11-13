# Minha parte — Modelo Lógico e tabelas

## Status

| # | Entrega | Status |
|---|---------|--------|
| 1 | Modelo Lógico final | Pronto em `docs/modelo_logico.html` e `docs/modelo_logico.drawio` |
| 2 | Criar banco `bd_final_fmp` | Rodar `sql/00_create_database.sql` no pgAdmin |
| 3 | TODO 1 — tabela `curso` | Feito em `sql/01_schema.sql` |
| 4 | TODO 2 — tabela `aluno` | Feito em `sql/01_schema.sql` |
| 5 | TODO 3 — tabela `matricula` | Feito em `sql/01_schema.sql` |
| 6 | Testes de integridade | Script em `sql/03_testes_integridade.sql` |
| 7 | Revisar organização do código | Checklist abaixo (01/12) |
| 8 | Perguntas 1 e 3 | Respostas prontas abaixo |

---

## Como abrir o modelo lógico

1. Abra `docs/modelo_logico.html` no navegador → Imprimir → Salvar como PDF (ou print screen).
2. Ou abra `docs/modelo_logico.drawio` em https://app.diagrams.net
3. Preencha a data de aprovação do grupo no arquivo.

---

## Ordem no pgAdmin

1. Conecte no servidor local → Query Tool no banco `postgres`.
2. Execute `sql/00_create_database.sql`.
3. Atualize a lista de bancos → conecte em `bd_final_fmp`.
4. Execute `sql/01_schema.sql` (cria as 4 tabelas).
5. Execute `sql/02_seed.sql` (cidades e cursos).
6. Aviso para a Pessoa 2: banco e tabelas prontos.
7. (Opcional) rode `sql/03_testes_integridade.sql` linha a linha e confira os erros esperados.
8. Depois dos testes: rode de novo `01_schema.sql` + `02_seed.sql`.

---

## Checklist organização (01/12)

- [ ] Não há SQL dentro de `app.py` (só chama funções do repositório)
- [ ] Todo SQL está em `repositories.py`
- [ ] `db.py` só cuida da conexão
- [ ] Nenhuma função ainda lança `NotImplementedError` (TODOs 5–12 da equipe)
- [ ] Nomes de funções/variáveis claros

**Hoje (ainda em construção):** TODOs 5–12 em `repositories.py` ainda têm `NotImplementedError` — isso é trabalho das outras pessoas. Sua parte de schema está ok. Em 01/12, confira se a equipe fechou esses TODOs.

---

## Pergunta 1 — Por que MATRICULA tem PK composta?

A matrícula representa a **relação** entre um aluno e um curso. A chave composta `(id_aluno, id_curso)` identifica essa relação pelo par e **impede matrícula repetida** do mesmo aluno no mesmo curso. Separadamente, cada coluna é FK: `id_aluno` → ALUNO e `id_curso` → CURSO.

---

## Pergunta 3 — O que acontece com e-mail duplicado?

A coluna `email` tem restrição `UNIQUE` (`uq_aluno_email`). O PostgreSQL **recusa o INSERT/UPDATE** e devolve erro de violação de unicidade. A aplicação captura essa falha e **mostra a mensagem de erro** na interface, sem gravar o segundo aluno.
