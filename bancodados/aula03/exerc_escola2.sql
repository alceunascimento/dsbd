-- Consulta 1: 
.print "Consulta 1: consulta conta quantas escolas existem em cada município. ";

SELECT 
    cod_municipio, 
    m.nome, 
COUNT(*) 
    as contagem 
FROM 
    escola 
INNER JOIN 
    municipio m 
ON 
    escola.cod_municipio = m.codigo
GROUP BY 
    cod_municipio, m.nome 
ORDER BY 
    contagem DESC;


-- Consulta 2: Crie uma consulta que exibe quantas escolas existem em cada estado
.print "Consulta 2: Crie uma consulta que exibe quantas escolas existem em cada estado";

SELECT 
    uf, 
COUNT(*) 
    as contagem 
FROM 
    escola 
INNER JOIN 
    municipio m 
ON 
    escola.cod_municipio = m.codigo
GROUP BY 
    uf 
ORDER BY 
    contagem DESC;