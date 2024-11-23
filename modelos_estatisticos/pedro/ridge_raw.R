# Modelo ridge na mao

# SETUP -----

rm(list = ls())

# GET DATA -------
dados  <- read.delim(file="~/dsbd/modelos_estatisticos/pedro/bases de dados/prostata/prostate.txt")


# CHECK DATA ----------
names(dados)

# separa a variavel alvo
y <- dados[,"lpsa"]

# exclui do dataset as variaveia que nao serao usadas
dados <- dados[,-c(1,10,11)]
names(dados)

# tranforma em matrix
X <- as.matrix(dados)
qr(dados)$rank
dim(dados)


# MODEL LM
lm <- lm(y ~., dados)
summary(lm)
# MODEL RIDGE --------


X <- as.matrix(dados)
# lambda
lambda <- 0.5

# estimando beta 
beta <- solve( t(X) %*% X + diag(lambda, nrow = dim(dados)[2]) ) %*% t(X) %*% y

# Y estimado
predictions <- X%*%beta

# plot
plot(y, predictions, main = "Previsão vs Valores reais",
     xlab= "valores reais", 
     ylab = "previsoes",
     pch=16,
     col=rgb(0,0,1,0.5),
     ylim = c(0,6))
abline(a = 0, b =1, col = "red")

# EQM
EQM=(1/dim(X)[1])*sum((y-predictions)^2)
EQM


# RIDGE 2-----
ajuste_basico <- glmnet(dados, y, alpha = 0, intercept = F)
plot(ajuste_basico)

