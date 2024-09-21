DROP TABLE IF EXISTS escola_vinculo;

CREATE TABLE escola_vinculo (
    escola_codigo  INT NOT NULL,
    vinculo_codigo INT NOT NULL,
    PRIMARY KEY (escola_codigo,vinculo_codigo),
    FOREIGN KEY (escola_codigo) REFERENCES escola(codigo),
    FOREIGN KEY (vinculo_codigo) REFERENCES vinculo(codigo)
);


INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11022558, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024275, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024291, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024372, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024666, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024682, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024828, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024917, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024968, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025034, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025077, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025115, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025280, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025310, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025352, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025620, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025654, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11037962, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11038047, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11038373, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11039493, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11046236, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11046244, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11046252, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11047402, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11047461, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11049782, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11050594, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006757, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006773, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006846, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006854, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006889, 1);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006900, 1);


INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11024917, 2);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025077, 2);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11025638, 2);
INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006900, 2);

INSERT INTO escola_vinculo (escola_codigo, vinculo_codigo) VALUES (11006900, 3);