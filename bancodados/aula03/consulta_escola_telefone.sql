# Identificar numero de escolas com telefone
SELECT 
    COUNT(DISTINCT escola.codigo) AS escolas_com_telefone
FROM 
    escola
INNER JOIN 
    telefone 
ON 
    escola.codigo = telefone.cod_escola;


# Listas escolas e telefones
SELECT 
    *
FROM 
    escola
LEFT JOIN 
    telefone 
ON 
    escola.codigo = telefone.cod_escola;


