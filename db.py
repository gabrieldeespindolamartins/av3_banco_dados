"""Conexão com PostgreSQL para o Projeto Final de Banco de Dados I."""

from __future__ import annotations

import os
import psycopg
from psycopg.rows import dict_row


def get_connection() -> psycopg.Connection:
    """Cria uma nova conexão usando variáveis de ambiente.

    Defina DB_PASSWORD no sistema antes de executar a aplicação.
    Os demais valores possuem padrões adequados ao laboratório local.
    """
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "bd_final_fmp"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        row_factory=dict_row,
    )
