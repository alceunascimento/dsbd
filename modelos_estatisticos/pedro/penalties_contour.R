# Carregar o pacote necessário
library(plotly)

# Definir uma sequência de valores para x e y
x <- seq(-10, 10, length.out = 100)
y <- seq(-10, 10, length.out = 100)

# Criar uma grade de valores para x e y
t <- outer(x, y, function(x, y) x^2 + y^2)

# Criar o gráfico tridimensional
fig <- plot_ly(x = ~x, y = ~y, z = ~t, type = "surface")

# Adicionar título e rótulos aos eixos usando expression
fig <- fig %>% layout(title = "Penalização",
                      scene = list(
                        xaxis = list(title = "<b>β<sub>1</sub></b>"),
                        yaxis = list(title = "<b>β<sub>2</sub></b>"),
                        zaxis = list(title = "t")
                      ))

# Mostrar o gráfico
fig

# Criar o gráfico tridimensional
plot_ly(x = ~x, y = ~y, z = ~t, type = "contour")%>% 
  layout(title = "Curvas de Nível",
         xaxis = list(title = "<b>β<sub>1</sub></b>"),
         yaxis = list(title = "<b>β<sub>2</sub></b>"))


# Criar uma grade de valores para x e y
t2 <- outer(x, y, function(x, y) abs(x) + abs(y))

# Criar o gráfico tridimensional
fig2 <- plot_ly(x = ~x, y = ~y, z = ~t2, type = "surface")

# Adicionar título e rótulos aos eixos usando expression
fig2 <- fig2 %>% layout(title = "Penalização",
                      scene = list(
                        xaxis = list(title = "<b>β<sub>1</sub></b>"),
                        yaxis = list(title = "<b>β<sub>2</sub></b>"),
                        zaxis = list(title = "t")
                      ))

# Mostrar o gráfico
fig2

# Criar o gráfico tridimensional
plot_ly(x = ~x, y = ~y, z = ~t2, type = "contour")%>% 
  layout(title = "Curvas de Nível",
         xaxis = list(title = "<b>β<sub>1</sub></b>"),
         yaxis = list(title = "<b>β<sub>2</sub></b>"))

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

# Definir uma sequência de valores para x e y
beta_1 <- seq(-10, 10, length.out = 100)
beta_2 <- seq(-10, 10, length.out = 100)


scad_j<-function(beta_j, lambda,gamma){
        ifelse( 
          abs(beta_j) <= lambda, 
          lambda*abs(beta_j),
            ifelse(
              ( lambda<abs(beta_j) ) & (abs(beta_j) < gamma * lambda ), 
              (2 * gamma * lambda * abs(beta_j) - beta_j^2 - lambda^2) / (2 * (gamma-1) ),
               (lambda^2*(gamma+1)) /2   
            )
        )
}

# Criar uma grade de valores para beta_1 e beta_2
t3 <- outer(beta_1, beta_2, function(x, y) scad_j(x,1,5) + scad_j(y,1,5))#gamma>1
#Rodar variando gamma

#Aqui não estou avaliando a versão lagrangeana, então faço lambda=1. 
#Deixei com lambda (como objeto) ao invés de substituí-lo por 1 na função para ter correspondencia (explícita) com a versão lagrangeana dos livros

#Lembrar que lambda da versão lagrangeana tem relação com o t. Quanto menor t, maior lambda


# Criar o gráfico tridimensional
fig3 <- plot_ly(x = ~x, y = ~y, z = ~t3, type = "surface")

# Adicionar título e rótulos aos eixos usando expression
fig3 <- fig3 %>% layout(title = "Penalização",
                      scene = list(
                        xaxis = list(title = "<b>β<sub>1</sub></b>"),
                        yaxis = list(title = "<b>β<sub>2</sub></b>"),
                        zaxis = list(title = "t")
                      ))

# Mostrar o gráfico
fig3


# Criar o gráfico tridimensional
plot_ly(x = ~x, y = ~y, z = ~t3, type = "contour")%>% 
  layout(title = "Curvas de Nível",
         xaxis = list(title = "<b>β<sub>1</sub></b>"),
         yaxis = list(title = "<b>β<sub>2</sub></b>"))







# Definir uma sequência de valores para x e y
beta_1 <- seq(-10, 10, length.out = 100)
beta_2 <- seq(-10, 10, length.out = 100)


mcp_j<-function(beta_j, lambda,gamma){
  ifelse(abs(beta_j)<=gamma*lambda,lambda*abs(beta_j)-(beta_j^2)/(2*gamma),
         (1/2)*gamma*(lambda^2) )
}






# Criar uma grade de valores para beta_1 e beta_2
t4 <- outer(beta_1, beta_2, function(x, y) mcp_j(x,1,5) + mcp_j(y,1,5))#gamma>1
#Rodar variando gamma

#Aqui não estou avaliando a versão lagrangeana, então faço lambda=1. 
#Deixei com lambda (como objeto) ao invés de substituí-lo por 1 na função para ter correspondencia (explícita) com a versão lagrangeana dos livros

#Lembrar que lambda da versão lagrangeana tem relação com o t. Quanto menor t, maior lambda


# Criar o gráfico tridimensional
fig4 <- plot_ly(x = ~x, y = ~y, z = ~t4, type = "surface")

# Adicionar título e rótulos aos eixos usando expression
fig4 <- fig4 %>% layout(title = "Penalização",
                      scene = list(
                        xaxis = list(title = "<b>β<sub>1</sub></b>"),
                        yaxis = list(title = "<b>β<sub>2</sub></b>"),
                        zaxis = list(title = "t")
                      ))

# Mostrar o gráfico
fig4

# Criar o gráfico tridimensional
plot_ly(x = ~x, y = ~y, z = ~t4, type = "contour")%>% 
  layout(title = "Curvas de Nível",
         xaxis = list(title = "<b>β<sub>1</sub></b>"),
         yaxis = list(title = "<b>β<sub>2</sub></b>"))







