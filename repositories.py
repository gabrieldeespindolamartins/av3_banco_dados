"""Camada de persistência - Projeto Final de Banco de Dados I - FMP.

VERSÃO DOS ALUNOS.

Objetivo didático:
- manter o SQL separado da interface;
- usar SQL parametrizado;
- implementar CRUD, JOIN e consulta de negócio.

Algumas funções estão prontas como EXEMPLO.
As funções marcadas com TODO fazem parte do projeto.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from db import get_connection


# ============================================================
# EXEMPLO 1 - SELECT simples
# ============================================================
def listar_cidades() -> list[dict[str, Any]]:
    with get_connection() as conn:
        return conn.execute(
            "SELECT id_cidade, nome, uf FROM cidade ORDER BY nome"
        ).fetchall()


# ============================================================
# EXEMPLO 2 - SELECT simples
# ============================================================
def listar_cursos() -> list[dict[str, Any]]:
    with get_connection() as conn:
        return conn.execute(
            "SELECT id_curso, nome, sigla FROM curso ORDER BY nome"
        ).fetchall()


# ============================================================
# EXEMPLO 3 - INSERT parametrizado
# Esta função é fornecida pronta para mostrar o padrão.
# ============================================================
def inserir_aluno(
    nome: str,
    email: str,
    data_nascimento: date | None,
    id_cidade: int | None,
) -> None:
    sql = """
        INSERT INTO aluno (nome, email, data_nascimento, id_cidade)
        VALUES (%s, %s, %s, %s)
    """
    with get_connection() as conn:
        conn.execute(sql, (nome, email, data_nascimento, id_cidade))


# ============================================================
# TODO 5 - READ de ALUNO
# Retornar:
# id_aluno, nome, email, data_nascimento, cidade, uf, id_cidade
#
# Requisito:
# - usar LEFT JOIN com CIDADE;
# - ordenar pelo nome do aluno.
# ============================================================
def listar_alunos() -> list[dict[str, Any]]:
    raise NotImplementedError("TODO 5: implemente listar_alunos() com LEFT JOIN.")


# ============================================================
# TODO 6 - UPDATE de ALUNO
# Atualizar nome, email, data_nascimento e id_cidade
# usando id_aluno no WHERE.
# ============================================================
def atualizar_aluno(
    id_aluno: int,
    nome: str,
    email: str,
    data_nascimento: date | None,
    id_cidade: int | None,
) -> None:
    raise NotImplementedError("TODO 6: implemente atualizar_aluno().")


# ============================================================
# TODO 7 - DELETE de ALUNO
# Excluir somente o aluno recebido por id_aluno.
# ============================================================
def excluir_aluno(id_aluno: int) -> None:
    raise NotImplementedError("TODO 7: implemente excluir_aluno().")


# ============================================================
# TODO 8 - CREATE de MATRICULA
# Inserir id_aluno, id_curso e data_matricula.
# ============================================================
def inserir_matricula(id_aluno: int, id_curso: int, data_matricula: date) -> None:
    raise NotImplementedError("TODO 8: implemente inserir_matricula().")


# ============================================================
# TODO 9 - UPDATE da data da MATRICULA
# A PK é composta. Logo, o WHERE precisa identificar
# id_aluno E id_curso.
# ============================================================
def atualizar_data_matricula(
    id_aluno: int,
    id_curso: int,
    data_matricula: date,
) -> None:
    raise NotImplementedError("TODO 9: implemente atualizar_data_matricula().")


# ============================================================
# TODO 10 - DELETE de MATRICULA
# Excluir usando as duas partes da PK composta.
# ============================================================
def excluir_matricula(id_aluno: int, id_curso: int) -> None:
    raise NotImplementedError("TODO 10: implemente excluir_matricula().")


# ============================================================
# TODO 11 - CONSULTA COM JOIN
# A listagem deve combinar:
# ALUNO + CURSO + MATRICULA + CIDADE
#
# Retornar, no mínimo:
# id_aluno, aluno, id_curso, sigla, curso,
# data_matricula e cidade.
#
# Sugestão:
# - INNER JOIN para ALUNO e CURSO;
# - LEFT JOIN para CIDADE.
# ============================================================
def listar_matriculas() -> list[dict[str, Any]]:
    raise NotImplementedError("TODO 11: implemente listar_matriculas() com JOIN.")


# ============================================================
# TODO 12 - CONSULTA DE NEGÓCIO
# Exibir TODOS os cursos e a quantidade de alunos matriculados.
#
# Requisitos:
# - LEFT JOIN;
# - COUNT;
# - GROUP BY;
# - inclusive curso com total 0.
# ============================================================
def resumo_por_curso() -> list[dict[str, Any]]:
    raise NotImplementedError("TODO 12: implemente resumo_por_curso().")
