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

-- ESCREVA AQUI O CREATE TABLE curso (...);


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

-- ESCREVA AQUI O CREATE TABLE aluno (...);


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

-- ESCREVA AQUI O CREATE TABLE matricula (...);
