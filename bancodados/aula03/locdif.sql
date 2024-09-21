DROP TABLE IF EXISTS localizacao_dif;

CREATE TABLE localizacao_dif (
  codigo INT PRIMARY KEY,
  descricao TEXT NOT NULL UNIQUE
);

INSERT INTO localizacao_dif (codigo, descricao) VALUES (0, 'Não está em área de localização diferenciada');
INSERT INTO localizacao_dif (codigo, descricao) VALUES (1, 'Área de assentamento');
INSERT INTO localizacao_dif (codigo, descricao) VALUES (2, 'Terra indígena');
INSERT INTO localizacao_dif (codigo, descricao) VALUES (3, 'Área de comunidade remanescente de quilombos')
