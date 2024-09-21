-- Consulta 1: Exibir todas as escolas, juntamente com suas cidades e telefones
.print "Consulta 1: Todas as escolas com suas cidades e telefones";

SELECT 
    *
FROM 
    escola
LEFT JOIN 
    telefone
ON 
    escola.codigo = telefone.cod_escola
INNER JOIN 
    municipio
ON 
    escola.cod_municipio = municipio.codigo;

-- Consulta 2: Exibir somente as escolas que possuem telefone, juntamente com suas cidades e estados
.print "Consulta 2: Escolas que possuem telefone com suas cidades e estados";

SELECT 
    *
FROM 
    escola
INNER JOIN 
    telefone 
ON 
    escola.codigo = telefone.cod_escola
INNER JOIN 
    municipio
ON 
    escola.cod_municipio = municipio.codigo
INNER JOIN
    estado
ON 
    municipio.uf = estado.uf;

-- Consulta 3: Exibir todas as escolas, juntamente com suas cidades, telefones e localizações diferenciadas
.print "Consulta 3: Todas as escolas com cidades, telefones e localizações diferenciadas";

SELECT 
    *
FROM 
    escola
LEFT JOIN 
    telefone 
ON 
    escola.codigo = telefone.cod_escola
LEFT JOIN 
    localizacao_dif
ON 
    escola.cod_loc_dif = localizacao_dif.codigo
INNER JOIN 
    municipio
ON 
    escola.cod_municipio = municipio.codigo;