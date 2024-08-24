---- QUIZ

---- Considere que criamos uma tabela produto da seguinte forma:


CREATE TABLE produto(
    CODIGO INT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

INSERT INTO produto (CODIGO, nome) VALUES ('001','uno');
INSERT INTO produto (CODIGO, nome) VALUES ('002','dos');
INSERT INTO produto (CODIGO, nome) VALUES ('003','tres');


---- Considere que cadastramos diversos produtos, e que ao executarmos o comando a seguir, obtivemos a resposta:

SELECT COUNT(*) FROM produto;
100

---- Ao executar o comando a seguir

SELECT DISTINCT nome FROM produto;

---- Qual a resposta esperada? Assinale a alternativa correta.
---- a. São geradas 100 linhas (tuplas) ou menos de resposta.
---- b. É exibido o número 100.
---- c. O comando resulta em um erro, pois DISTINCT só pode ser aplicado na chave primária.
---- d. São exibidas 100 linhas ou mais de resposta.
---- e. São exibidas exatamente 100 linhas (tuplas) de resposta.

