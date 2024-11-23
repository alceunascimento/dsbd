###############################################################################
#############   RIDGE E LASSO   ###############################################
###############################################################################

# NOTES

# A base de dados de próstata (PROS) provém de um estudo realizado em 97
# homens sobre os quais foram realizadas medições (clínicas e demográficas) de 8
# características diferentes. Tais informações pode ser utilizadas para modelar, através
# de um sistema linear, quantidades relacionadas a um antígeno chamado PSA
# (Prostate Specific Antigen), que é um fator de risco associado ao câncer de próstata.
# Quanto maior o valor do PSA, maior o risco de um indivíduo ter o câncer de
# próstata.


# Logaritmo do volume do câncer / lcavol
# Logaritmo do peso da próstata / lweight
# Idade / age
# Logaritmo da quantidade de hiperplasia prostática benigna / lbph
# Invasão da vesícula seminal / svi
# Logaritmo da penetração capsular / lcp
# Gleason score / gleason
# Percentual do Gleason score / pgg45
# Logaritmo do antígeno PSA / lPSA


# SETUP ---------
library(corrplot)
library(glmnet)
library(doSNOW)#progressbar

rm(list = ls())

# DATA ----------
dados  <- read.delim(file="~/dsbd/modelos_estatisticos/pedro/bases de dados/prostata/prostate.txt")

# WRANGLING DATA ----
str(dados)
names(dados)

# separa a variavel alvo
y <- dados[,"lpsa"]

# exclui do dataset as variaveia que nao serao usadas
dados <- dados[,-c(1,10,11)]
names(dados)

# tranforma em matrix
dados <- as.matrix(dados)
qr(dados)$rank
dim(dados)

## Separando em treinamento e teste a 20% ----
n_test <- round(0.20*dim(dados)[1])
n_train <- dim(dados)[1]-n_test
test_ind <- sample(c(rep("train",n_train),rep("test",n_test)))
dados_train <- dados[test_ind=="train",]
dados_test <- dados[test_ind=="test",]
y_train <- y[test_ind=="train"]
y_test <- y[test_ind=="test"]


dados_train_pad <- scale(dados_train)
media_pad <- attr(dados_train_pad, "scaled:center")
sd_pad <- attr(dados_train_pad, "scaled:scale")
dados_test_pad <- scale(dados_test,center = media_pad,scale = sd_pad)
#dados_test_pad <- t((t(dados_test)-media_pad)/sd_pad)
#dados_test_pad <- do.call(rbind,lapply(1:dim(dados_test)[1],function(i) (dados_test[i,]-media_pad)/sd_pad))


# Calcular a matriz de correlação
cor_matrix <- cor(dados)
cor_matrix
corrplot(cor_matrix, 
         method = "ellipse", 
         order = "hclust", 
         tl.col = "black", 
         tl.cex = 0.8, 
         cl.cex = 0.8, 
         type="upper")


## Para a validação cruzada ------
K <- 5
vc_ind <- sample(rep(1:K,length.out = nrow(dados_train_pad)))


# MODELS -----

## MODEL LINEAR REGRESSION -----
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





## LASSO -----
regularizador=seq(0,5,by=0.0025)
head(regularizador)
tail(regularizador)

# Ajustar o modelo de regressão com penalização elastic net
fit_LASSO <- cv.glmnet(dados_train_pad, 
                       y_train, 
                       family = "gaussian", 
                       alpha = 1,
                       lambda = regularizador,
                       nfolds = K,
                       foldid = vc_ind)#LASSO


str(fit_LASSO)
plot(fit_LASSO)
fit_LASSO$lambda.min                                       # lambda do menor MSE
fit_LASSO$cvm[fit_LASSO$lambda == fit_LASSO$lambda.min]    # menor MSE
coef(fit_LASSO, s = "lambda.min")
coef(fit_LASSO, s = fit_LASSO$lambda.min)
coef(fit_LASSO)
coef(fit_LASSO, s=fit_LASSO$lambda.1se)
table(as.numeric(coef(fit_LASSO)[-1])==0)#5 variáveis zeradas (com fit_LASSO$lambda.1se)
plot(as.numeric(coef(fit_LASSO)[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes
plot(fit_LASSO$glmnet.fit, xvar = "lambda", label = TRUE)
# Prevê a resposta usando o modelo ajustado e calcula o MSE nos dados de teste
# O modelo é ajustado sobre todos os dados de treinamento com fit_LASSO$lambda.min e testado nos dados de teste
predictions = predict(fit_LASSO, newx = dados_test_pad, s=fit_LASSO$lambda.min)
MSE_min_LASSO_test = mean((y_test-predictions)^2)



# RIDGE
regularizador=seq(0,5,by=0.0025)
head(regularizador)
tail(regularizador)


fit_RIDGE <- cv.glmnet(dados_train_pad, 
                       y_train, 
                       family = "gaussian", 
                       alpha = 0,
                       #lambda = regularizador,
                       nfolds = K,
                       foldid = vc_ind)#RIDGE



str(fit_RIDGE)
fit_RIDGE$cvm
min(fit_RIDGE$cvm)
fit_RIDGE$glmnet.fit$beta

View(as.matrix(fit_RIDGE$glmnet.fit$beta))

plot(fit_RIDGE)
fit_RIDGE$lambda.min#lambda do menor MSE
fit_RIDGE$cvm[fit_RIDGE$lambda == fit_RIDGE$lambda.min]#menor MSE 

coef(fit_RIDGE, s = "lambda.min")


table(as.numeric(coef(fit_RIDGE)[-1])==0)#(com fit_RIDGE$lambda.1se)
plot(as.numeric(coef(fit_RIDGE)[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes 
plot(fit_RIDGE$glmnet.fit, 
     xvar = "lambda", 
     label = TRUE)

# Prevê a resposta usando o modelo ajustado e calcula o MSE nos dados de teste
predictions = predict(fit_RIDGE, 
                      newx = dados_test_pad, 
                      s = fit_RIDGE$lambda.min)
MSE_min_RIDGE_test = mean((y_test-predictions)^2)




## EN -----
regularizador=seq(0,5,by=0.0025)
head(regularizador)
tail(regularizador)


fit_EN  <- cv.glmnet(dados_train_pad, 
                     y_train, 
                     family = "gaussian", 
                     alpha = 0.9,
                     lambda = regularizador,
                     nfolds = K,
                     foldid = vc_ind)



str(fit_EN)
plot(fit_EN)
fit_EN$lambda.min#lambda do menor MSE
fit_EN$cvm[fit_EN$lambda == fit_EN$lambda.min]#menor MSE 
table(as.numeric(coef(fit_EN)[-1])==0)#4 variáveis zeradas (com fit_EN$lambda.1se)
plot(as.numeric(coef(fit_EN)[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes 
plot(fit_EN$glmnet.fit, xvar = "lambda", label = TRUE)
# Prevê a resposta usando o modelo ajustado e calcula o MSE nos dados de teste
predictions = predict(fit_EN, newx = dados_test_pad, s=fit_EN$lambda.min)
MSE_min_EN_test = mean((y_test-predictions)^2)




cor_matrix2 = cor(dados[,as.numeric(coef(fit_LASSO)[-1])!=0])
corrplot(cor_matrix2, 
         method = "color", 
         order = "hclust", 
         addrect = 2, 
         tl.col = "black", 
         tl.cex = 0.8, 
         cl.cex = 0.8)

cor_matrix2 = cor(dados[,as.numeric(coef(fit_EN)[-1])!=0])
corrplot(cor_matrix2, 
         method = "color", 
         order = "hclust", 
         addrect = 2, 
         tl.col = "black", 
         tl.cex = 0.8, 
         cl.cex = 0.8)






###############################################################################
###############################################################################
##############################       LASSO E RIDGE (GLMNET)      ##############
###############################################################################
###############################################################################

###############################################
########### Validação cruzada RIDGE ###########
###############################################
EQM_CV_RIDGE=vector()
EQM_CV_LASSO=vector()
sd_EQM_CV_RIDGE=vector()
sd_EQM_CV_LASSO=vector()

regularizador=seq(0,5,by=0.0025)
pb = txtProgressBar(min = 1,max = length(regularizador),style = 3)

for(i in 1:length(regularizador)){
  setTxtProgressBar(pb,i)
  
  EQMridge=vector()
  EQMLasso=vector()
  for(fold in 1:5){
    dados_train_CV=dados_train_pad[vc_ind!=fold,]
    dados_valid_CV=dados_train_pad[vc_ind==fold,]
    y_train_CV=y_train[vc_ind!=fold]
    y_valid_CV=y_train[vc_ind==fold]
    
    
    
    beta_RIDGE=glmnet(dados_train_CV,y_train_CV,alpha = 0,lambda = regularizador[i])
    predictions = predict(beta_RIDGE, newx = dados_valid_CV, s = regularizador[i])
    EQMridge[fold]= mean((predictions-y_valid_CV)^2)
    # beta_RIDGE=coefficients(beta_RIDGE)[-1]#desconsidera intercepto
    # EQMridge[fold]=mean((as.matrix(dados_valid_CV)%*%beta_RIDGE+mean(y)-y_valid_CV)^2)
    
    beta_LASSO=glmnet(dados_train_CV,y_train_CV,alpha = 1,lambda = regularizador[i])
    predictions = predict(beta_LASSO, newx = dados_valid_CV, s = regularizador[i])
    EQMLasso[fold]= mean((predictions-y_valid_CV)^2)
    # beta_LASSO=coefficients(beta_LASSO)[-1]#desconsidera intercepto
    # EQMLasso[fold]=mean((as.matrix(dados_valid_CV)%*%beta_LASSO+mean(y)-y_valid_CV)^2)
    
    
    
  }
  EQM_CV_RIDGE[i]=mean(EQMridge)
  EQM_CV_LASSO[i]=mean(EQMLasso)
  
  sd_EQM_CV_RIDGE[i]=sd(EQMridge)
  sd_EQM_CV_LASSO[i]=sd(EQMLasso)
}


plot(fit_LASSO)
lines(log(regularizador),EQM_CV_LASSO,type="l",col=4,lwd=3)
lines(log(regularizador),EQM_CV_LASSO+sd_EQM_CV_LASSO/sqrt(K))#quanto maior K, mais apertado o intervalo
lines(log(regularizador),EQM_CV_LASSO-sd_EQM_CV_LASSO/sqrt(K))


plot(fit_RIDGE)
lines(log(regularizador),EQM_CV_RIDGE,ylim = c(0.5,1),type="l",col=4,lwd=3)
lines(log(regularizador),EQM_CV_RIDGE+sd_EQM_CV_RIDGE/sqrt(K))
lines(log(regularizador),EQM_CV_RIDGE-sd_EQM_CV_RIDGE/sqrt(K))



regularizador[which.min(EQM_CV_LASSO)]
fit_LASSO$lambda.min
regularizador[which.min(EQM_CV_RIDGE)]
fit_RIDGE$lambda.min

EQM_CV_RIDGE[which.min(EQM_CV_RIDGE)]
fit_RIDGE$cvm[fit_RIDGE$lambda == fit_RIDGE$lambda.min]
EQM_CV_LASSO[which.min(EQM_CV_LASSO)]
fit_LASSO$cvm[fit_LASSO$lambda == fit_LASSO$lambda.min]
###########################################

###############################################

plot(log(regularizador),EQM_CV_LASSO,type="l",ylim=c(0.5,0.9))
lines(log(regularizador),EQM_CV_RIDGE,col=4)






###############################################################################
###############################################################################
# COEFICIENTES DO MODELO COM O MELHOR LAMBDA
###############################################################################
###############################################################################

LASSO=glmnet(dados_train_pad,y_train,alpha = 1,lambda = regularizador[which.min(EQM_CV_LASSO)])
betaLASSO=as.numeric(coef(LASSO)[-1])
# Prevê a resposta usando o modelo ajustado e calcula o MSE nos dados de teste
predictions = predict(LASSO, newx = dados_test_pad)
mean((y_test-predictions)^2)

plot(y_test, predictions, main="Previsões vs Valores Reais",
     xlab="Valores Reais", ylab="Previsões",
     pch=16, col=rgb(0, 0, 1, 0.5),ylim=c(0,4))
abline(a = 0, b = 1, col = "red")



RIDGE=glmnet(dados_train_pad,y_train,alpha = 0,lambda = regularizador[which.min(EQM_CV_RIDGE)])
betaRIDGE=as.numeric(coef(RIDGE)[-1])
# Prevê a resposta usando o modelo ajustado e calcula o MSE nos dados de teste
predictions = predict(RIDGE, newx = dados_test_pad)
mean((y_test-predictions)^2)

plot(y_test, predictions, main="Previsões vs Valores Reais",
     xlab="Valores Reais", ylab="Previsões",
     pch=16, col=rgb(0, 0, 1, 0.5),,ylim=c(0,4))
abline(a = 0, b = 1, col = "red")




betaLM=lm(y_train~.,data=as.data.frame(dados_train_pad))
betaLM=coef(betaLM)
mean(y_train)#quando as covariáveis estão padronizadas, o intercepto é a média da var resposta
###############################################################################
###############################################################################

