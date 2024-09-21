SELECT 
    escola.nome, vinculo.nome 
    count(*)
FROM 
    escola
INNER JOIN 
    escola_vinculo 
ON 
    escola.codigo = escola_vinculo.escola_codigo
INNER JOIN 
    vinculo 
ON 
    escola_vinculo.vinculo_codigo = vinculo.codigo;