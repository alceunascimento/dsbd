---- Exercícios
---- 1. Crie uma tabela região, que conterá as cinco regiões do Brasil.
---- a. Na tabela use como chave primária a sigla da região. Por exemplo, Nordeste é NE.
---- 2. Modiﬁque a tabela estados para que ela tenha uma ligação Nx1 entre estado e região.
---- a. Não esqueça das restrições de integridade (ex.: chave estrangeira).
---- 3. Faça as seguintes consultas:
---- a. Exiba todos os municípios em ordem alfabética, juntamente com seus estados e regiões. Use inner join.
---- b. Exiba todos os municípios homônimos, onde os homônimos devem estar na mesma região.
---- c. Exiba todas as combinações únicas entre nomes de município e região do Brasil.
---- d. Conte quantos municípios existem na região SUL do Brasil.
---- e. Liste os municípios possuem ‘ão’ em algum lugar do nome, e que ﬁcam no Nordeste.
---- 4. Faça o Diagrama Físico do banco de dados modelado até o momento no DIA ou no Oracle SQL Datamodeler
----

---  SET TABLES
DROP TABLE IF EXISTS municipio;
DROP TABLE IF EXISTS estado;
DROP TABLE IF EXISTS regiao;


CREATE TABLE regiao (
    sigla   TEXT PRIMARY KEY UNIQUE,
    nome 	TEXT NOT NULL
);

CREATE TABLE estado(
    uf          TEXT PRIMARY KEY,
    nome        TEXT NOT NULL UNIQUE,
    sigla       TEXT,
    FOREIGN KEY (sigla) REFERENCES regiao(sigla)
);

CREATE TABLE municipio (
    codigo INT		  PRIMARY KEY,
    nome 	 TEXT NOT NULL,
    uf	 TEXT	  NOT NULL,
    FOREIGN KEY (uf) REFERENCES estado(uf)
);


