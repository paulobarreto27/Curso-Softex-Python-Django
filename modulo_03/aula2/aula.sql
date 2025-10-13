-- Active: 1759756398339@@127.0.0.1@3306
CREATE TABLE alunos ( id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEREGER);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 22);

SELECT * FROM alunos;
SELECT nome, idade FROm alunos;
SELECT * FROM alunos WHERE idade = 20

DELETE FROM alunos WHERE nome = 'Maria';


