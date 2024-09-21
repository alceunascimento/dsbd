DROP TABLE IF EXISTS escola_vinculo;
DROP TABLE IF EXISTS vinculo;

CREATE TABLE vinculo(
    codigo INT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL UNIQUE
);

INSERT INTO vinculo (codigo, nome,descricao) VALUES (1, 'Secretaria da Educação', 'Escola pública vinculada à Secretaria de Educação, ou Ministério da Educação.');
INSERT INTO vinculo (codigo, nome,descricao) VALUES (2, 'Segurança Pública', 'Escola pública vinculada à Secretaria de Segurança Pública, ou Forças Armadas, ou Militar.');
INSERT INTO vinculo (codigo, nome,descricao) VALUES (3, 'Secretaria da Saúde', 'Escola pública vinculada à Secretaria de Saúde ou Ministério da Saúde.');