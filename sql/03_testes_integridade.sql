-- Testes manuais de integridade (pgAdmin / Query Tool)
-- Pré-requisito: 01_schema.sql e 02_seed.sql já executados.
-- Depois dos testes, rode 01_schema.sql + 02_seed.sql de novo para limpar.

-- Preparação: um aluno e uma matrícula válidos
INSERT INTO aluno (nome, email, data_nascimento, id_cidade)
VALUES ('Teste Integridade', 'teste.integridade@fmp.edu.br', '2000-01-01', 1);

-- anote o id gerado; abaixo usamos o e-mail para achar o aluno
-- id_curso 1 = Administração (seed)

INSERT INTO matricula (id_aluno, id_curso, data_matricula)
SELECT id_aluno, 1, CURRENT_DATE
FROM aluno
WHERE email = 'teste.integridade@fmp.edu.br';

-- 1) E-mail duplicado -> esperado: erro UNIQUE (uq_aluno_email)
INSERT INTO aluno (nome, email, data_nascimento, id_cidade)
VALUES ('Outro Nome', 'teste.integridade@fmp.edu.br', '2001-02-02', 1);

-- 2) Matrícula duplicada -> esperado: erro PK composta
INSERT INTO matricula (id_aluno, id_curso, data_matricula)
SELECT id_aluno, 1, CURRENT_DATE
FROM aluno
WHERE email = 'teste.integridade@fmp.edu.br';

-- 3) FK inválida -> esperado: erro FK (curso inexistente)
INSERT INTO matricula (id_aluno, id_curso, data_matricula)
SELECT id_aluno, 9999, CURRENT_DATE
FROM aluno
WHERE email = 'teste.integridade@fmp.edu.br';

-- 4) Excluir curso com matrícula -> esperado: bloqueado (RESTRICT)
DELETE FROM curso WHERE id_curso = 1;

-- 5) Excluir aluno com matrícula -> esperado: matrícula some (CASCADE)
DELETE FROM aluno WHERE email = 'teste.integridade@fmp.edu.br';

SELECT *
FROM matricula m
JOIN aluno a ON a.id_aluno = m.id_aluno
WHERE a.email = 'teste.integridade@fmp.edu.br';
-- esperado: 0 linhas
