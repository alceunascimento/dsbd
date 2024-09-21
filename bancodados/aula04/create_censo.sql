DROP TABLE IF EXISTS censo;

CREATE TABLE censo (
    ano                INT,
    cod_escola         INT,
    possui_agua_pot    BOOL,
    possui_agua_rede_pub BOOL,
    qtde_ensino_medio  INT,
    PRIMARY KEY (ano, cod_escola),  -- Chave primária composta por ano e código da escola
    FOREIGN KEY (cod_escola) REFERENCES escola(codigo)
);

