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

---- QUERY DATA


---- b. Exiba todos os municípios homônimos, onde os homônimos devem estar na mesma região.
SELECT m1.nome , e1.nome , r1.nome 
FROM municipio m1
INNER JOIN estado e1 ON m1.uf = e1.uf
INNER JOIN regiao r1 ON e1.sigla = r1.sigla
WHERE m1.nome IN (
    SELECT m2.nome
    FROM municipio m2
    INNER JOIN estado e2 ON m2.uf = e2.uf
    GROUP BY m2.nome, e2.sigla
    HAVING COUNT(*) > 1
    
) LIMIT 5;
