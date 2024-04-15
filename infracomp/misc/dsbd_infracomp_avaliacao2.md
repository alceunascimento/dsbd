# Avaliação 2
Condições de conclusão
Aberto: sexta-feira, 5 abr. 2024, 00:00
Vencimento: segunda-feira, 29 abr. 2024, 23:59

## Associe os comandos que retornem a informação desejada

Liste todos arquivos do seu diretório HOME com as suas permissões  
Resposta 1 Questão 1  
`ls -l ~/`  
 
Mostra o espaço em disco ocupado por cada arquivo ou diretório na área do usuário, em formato humanamente legível (KB, MB, GB, etc).  
Resposta 2 Questão 1  
`du -sh $HOME`  
 
Listar todos arquivos dentro do diretório /usr/share/doc ou seus subdiretórios, que tenham seu nome terminado com a extensão .gz, sem diferenciar maiúsculas e minúsculas.   
Resposta 3 Questão 1  
`find /usr/share/doc -iname "*.gz"`  
 
Copia o arquivo “teste.txt” que está no diretório acima do corrente (pai) para dentro do seu diretório corrente  
Resposta 4 Questão 1  
`cp ../teste.txt .`  
 
Altere as permissões de acesso do seu diretório HOME para que somente você e os usuários do seu grupo tenham acesso de leitura e somente você tenha acesso de leitura, escrita e execução.  
Resposta 5 Questão 1  
`chmod u=rxw,g-r $HOME`  
 
O “username” ou login da conta que você está utilizando  
Resposta 6 Questão 1  
`whoami`  
 


## Crie um arquivo chamado "dados.txt" com os dados abaixo (sem a primeira linha de cabeçalho) e escreva os comandos que fazem o que é pedido:  
  
NOME,NOTA,CONCEITO,FALTAS  
Aldebaran Leite Agner,-,-,6  
Alessandro Bueno de Souza,103,A,0  
Alexandre Rodizio Bento,91.5,A,0  
Charles Laudemaine,82,B,0  
Debora Ruedell,102.5,A,0  
Dirlei F. Lopes da Silva,97.5,A,0  
Edson Flavio de Souza,108,A,2  
Fabiana Cristian Penter,107.5,A,0  
Helio Augusto Goncalves,79,C,0  
Isaias Arcilio dos Santos,70,C,1  
Joao Carlos Balzan,70.5,C,0  
Jonsue Trapp Martins,100,A,2  
Misael Alves Bortolaz,102.5,A,1  
Rafael Hammerschimidt,110,A,0  
Ricardo Esteves da Costa,99,A,0  
Rosangela Binneck,81,B,0  
Sergio Ribeiro da Luz Wanderley,90.2,A,3  
Stefano Chapoval Fontes,102,A,1  
Wanderlei Wormsbecker,82.5,B,2  
Wellington Telles Cunha,97.5,A,0  
Yuri Matos Freitas,99.5,A,0  
   
  
Mostre apenas o NOME e o CONCEITO dos alunos  
Resposta 1 Questão 2  
`cut -d',' -f1,3 dados.txt`  
   
Substitua o CONCEITO ‘A’ por “APROVADO”  
Resposta 2 Questão 2  
`sed 's/,A,/,APROVADO,/g' dados.txt`  
   
Mostre apenas linhas que tenham duas vogais consecutivas  
Resposta 3 Questão 2  
`egrep '[aeiou]{2}' dados.txt`  
   
Mostre os dados ordenados numericamente pela NOTA  
Resposta 4 Questão 2  
`sort -n -t',' -k2 dados.txt`  
   
Mostre quantos alunos há na turma  
Resposta 5 Questão 2  
`wc -l dados.txt`  
   
Mostre apenas alunos que tenham conceito ‘B’  
Resposta 6 Questão 2  
`egrep ',B,' dados.txt`  