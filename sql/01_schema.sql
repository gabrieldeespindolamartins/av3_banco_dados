-- PROJETO FINAL - BANCO DE DADOS I - FMP
-- VERSÃO DOS ALUNOS
-- Etapa: transformar o Modelo Lógico em Modelo Físico no PostgreSQL.
--
-- ATENÇÃO:
-- A tabela CIDADE está pronta como exemplo.
-- As demais tabelas devem ser implementadas pelo grupo.
--
-- Modelo esperado:
-- CIDADE 1:N ALUNO
-- ALUNO N:N CURSO, resolvido por MATRICULA

DROP TABLE IF EXISTS matricula CASCADE;
DROP TABLE IF EXISTS aluno CASCADE;
DROP TABLE IF EXISTS curso CASCADE;
DROP TABLE IF EXISTS cidade CASCADE;

-- EXEMPLO COMPLETO
CREATE TABLE cidade (
    id_cidade INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL,
    CONSTRAINT uq_cidade_nome_uf UNIQUE (nome, uf)
);

-- ============================================================
-- TODO 1 - CRIAR A TABELA CURSO
-- Requisitos mínimos:
--   id_curso -> chave primária gerada automaticamente
--   nome     -> obrigatório e não pode repetir
--   sigla    -> obrigatória e não pode repetir
-- ============================================================

CREATE TABLE curso (
    id_curso INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    sigla VARCHAR(10) NOT NULL,
    CONSTRAINT uq_curso_nome UNIQUE (nome),
    CONSTRAINT uq_curso_sigla UNIQUE (sigla)
);

-- ============================================================
-- TODO 2 - CRIAR A TABELA ALUNO
-- Requisitos mínimos:
--   id_aluno        -> chave primária gerada automaticamente
--   nome            -> obrigatório
--   email           -> obrigatório e UNIQUE
--   data_nascimento -> DATE
--   id_cidade       -> FK para CIDADE
--
-- Regra sugerida:
--   se uma cidade for excluída, o aluno deve permanecer e
--   id_cidade pode ficar NULL.
-- ============================================================

CREATE TABLE aluno (
    id_aluno INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    data_nascimento DATE,
    id_cidade INTEGER,
    CONSTRAINT uq_aluno_email UNIQUE (email),
    CONSTRAINT fk_aluno_cidade
        FOREIGN KEY (id_cidade)
        REFERENCES cidade (id_cidade)
        ON DELETE SET NULL
);

-- ============================================================
-- TODO 3 - CRIAR A TABELA MATRICULA
-- Esta tabela resolve o relacionamento N:N entre ALUNO e CURSO.
--
-- Requisitos mínimos:
--   id_aluno      -> FK
--   id_curso      -> FK
--   data_matricula -> obrigatória; usar CURRENT_DATE como padrão
--   PK composta: (id_aluno, id_curso)
--
-- Regras sugeridas:
--   ao excluir ALUNO, remover suas matrículas;
--   não permitir excluir CURSO que ainda possui matrículas.
-- ============================================================

CREATE TABLE matricula (
    id_aluno INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    data_matricula DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT pk_matricula PRIMARY KEY (id_aluno, id_curso),
    CONSTRAINT fk_matricula_aluno
        FOREIGN KEY (id_aluno)
        REFERENCES aluno (id_aluno)
        ON DELETE CASCADE,
    CONSTRAINT fk_matricula_curso
        FOREIGN KEY (id_curso)
        REFERENCES curso (id_curso)
        ON DELETE RESTRICT
);
