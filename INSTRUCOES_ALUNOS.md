# INSTRUÇÕES AOS ALUNOS
## Projeto Final - Banco de Dados I - FMP

### Objetivo
Completar uma mini aplicação acadêmica integrando **PostgreSQL + SQL + Python + Tkinter**, demonstrando domínio dos conteúdos desenvolvidos em Banco de Dados I.

---

## Etapa 1 - Modelo Lógico
Antes de alterar o código, valide o modelo:

- CIDADE 1:N ALUNO
- ALUNO N:N CURSO
- MATRICULA resolve o relacionamento N:N

Entregável: Modelo Lógico com entidades, atributos, PKs e FKs.

---

## Etapa 2 - Modelo Físico
Abra `sql/01_schema.sql`.

A tabela CIDADE está pronta como exemplo.

Complete:
- TODO 1: CURSO
- TODO 2: ALUNO
- TODO 3: MATRICULA

Teste no pgAdmin.

---

## Etapa 3 - Dados iniciais
Execute `sql/02_seed.sql`.

Depois cadastre dados fictícios suficientes para testar:
- pelo menos 5 alunos;
- mais de uma cidade;
- mais de um curso;
- pelo menos um curso sem matrícula.

---

## Etapa 4 - Primeiro fluxo funcionando
Execute a aplicação.

O botão **Cadastrar** já utiliza um exemplo completo de `INSERT` parametrizado.

Use esse fluxo para compreender:

**Tela → add_student() → inserir_aluno() → INSERT → PostgreSQL**

---

## Etapa 5 - Completar CRUD de ALUNO
Abra `repositories.py`.

Implemente:
- TODO 5: listar_alunos()
- TODO 6: atualizar_aluno()
- TODO 7: excluir_aluno()

Depois teste os botões:
- Listar
- Atualizar
- Excluir

---

## Etapa 6 - Completar MATRICULA
Implemente:
- TODO 8: inserir_matricula()
- TODO 9: atualizar_data_matricula()
- TODO 10: excluir_matricula()

Lembre-se: MATRICULA possui chave primária composta.

---

## Etapa 7 - JOIN
Implemente:
- TODO 11: listar_matriculas()

A consulta deve reunir dados que estão fisicamente separados em várias tabelas.

Resultado esperado na interface:
**Aluno | Curso | Data | Cidade**

---

## Etapa 8 - Relatório
Implemente:
- TODO 12: resumo_por_curso()

Requisitos:
- `LEFT JOIN`
- `COUNT`
- `GROUP BY`
- cursos sem alunos também devem aparecer

---

## Testes obrigatórios

1. Tentar cadastrar e-mail duplicado.
2. Tentar matricular o mesmo aluno duas vezes no mesmo curso.
3. Cadastrar matrícula válida.
4. Excluir aluno que possua matrícula e observar a regra de integridade.
5. Executar o JOIN.
6. Executar o relatório e verificar um curso com total 0.

---

## Entrega

O grupo deverá apresentar:
- Modelo Lógico final;
- scripts SQL;
- código-fonte;
- aplicação funcionando;
- CRUD;
- matrícula;
- consulta com JOIN;
- relatório;
- README curto;
- explicação técnica do funcionamento.

### Atenção
Na apresentação, qualquer integrante poderá ser questionado sobre o código e o banco.
