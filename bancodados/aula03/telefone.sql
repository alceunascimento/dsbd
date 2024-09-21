DROP TABLE IF EXISTS telefone;

CREATE TABLE telefone (
  cod_escola INT PRIMARY KEY,
  ddd INT,
  numero INT,
  FOREIGN KEY (cod_escola) REFERENCES escola(codigo)
);

INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11022558, 041, 22252235);
INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11024275, 021, 22256987);
INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11024291, 011, 36654582);
INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11024372, 071, 58862114);
INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11024666, 085, 56688995);
INSERT INTO telefone (cod_escola, ddd, numero) VALUES (11024682, 043, 24458778);