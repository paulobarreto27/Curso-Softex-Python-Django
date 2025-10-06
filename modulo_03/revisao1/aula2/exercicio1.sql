-- Active: 1759756398339@@127.0.0.1@3306
CREATE TABLE usuarios ( 
    id INTEGER PRIMARY KEY, 
    nome TEXT NOT NULL, 
    sobrenome TEXT NOT NULL, 
    email TEXT NOT NULL, 
    senha TEXT NOT NULL
    );

CREATE TABLE postagens ( 
    id INTEGER PRIMARY KEY, 
    titulo TEXT NOT NULL, 
    postagem TEXT NOT NULL, 
    id_autor INTEGER
    );

INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('Paulo', 'Roberto', 'pauloroberto@email.com', 123456);
INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('João', 'Paulo', 'joaopaulo@email.com', 123456);
INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('Ana', 'Maria', 'anamaria@email.com', 123456);
INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('Maria', 'Alice', 'mariaalice@email.com', 123456);
INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('Ana', 'Paula', 'anapaula@email.com', 123456);

SELECT * FROM usuarios;

INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Bom dia!', 'Hoje tem aula de banco de dados', 1);
INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Olá', 'Segundou!', 2);
INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Odeio Segunda!', 'Começou tudo de novo', 3);
INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Academia', 'Projeto verão 2026', 4);
INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Dia mundial da dieta', 'Começando a minha dieta', 5);

SELECT * FROM postagens;

