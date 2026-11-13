-- PROJETO FINAL - BANCO DE DADOS I - FMP
-- VERSÃO DOS ALUNOS
-- Carga inicial do cenário didático.
--
-- Execute este arquivo SOMENTE depois de concluir corretamente
-- as tabelas do arquivo 01_schema.sql.

INSERT INTO cidade (nome, uf) VALUES
('Palhoça', 'SC'),
('Florianópolis', 'SC'),
('São José', 'SC'),
('Biguaçu', 'SC');

-- Cursos utilizados no cenário do projeto.
INSERT INTO curso (nome, sigla) VALUES
('Administração', 'ADM'),
('Pedagogia', 'PED'),
('Processos Gerenciais', 'PG'),
('Análise e Desenvolvimento de Sistemas', 'ADS');

-- ============================================================
-- TODO 4 - DADOS DE TESTE
-- NÃO há alunos nem matrículas prontos neste arquivo.
--
-- O grupo deverá:
--   1. cadastrar pelo menos 5 alunos fictícios;
--   2. usar mais de uma cidade;
--   3. criar matrículas em diferentes cursos;
--   4. manter pelo menos um curso sem matrícula, para testar
--      posteriormente o LEFT JOIN do relatório.
--
-- Você pode inserir alguns dados pelo pgAdmin e outros pela
-- própria aplicação Python.
-- ============================================================
