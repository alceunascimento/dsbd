
library(ISLR)
library(fastDummies)
library(grpreg)

cred=Credit
y=cred$Balance
cred=cred[,-c(1,12)]#retira ID e Balance
str(cred)

# Gerando variáveis dummy para a variável 'gender'
data_with_dummies <- dummy_cols(cred, select_columns = c("Gender","Student","Married","Ethnicity"), remove_first_dummy = T)
X=data_with_dummies[,-c(7:10)]




# Ajustar o modelo group lasso
names(X)
gr=c(1,2,3,4,5,6,7,8,9,10,10)




# Separando em treinamento e teste 
n_test=round(0.20*dim(X)[1])
n_train=dim(X)[1]-n_test
test_ind=sample(c(rep("train",n_train),rep("test",n_test)))

dados_train=X[test_ind=="train",]
dados_test=X[test_ind=="test",]
y_train=y[test_ind=="train"]
y_test=y[test_ind=="test"]

#####
str(X)
numericas_train_pad=scale(dados_train[,1:6])
dados_train_pad=cbind(numericas_train_pad,dados_train[,7:11])#não padronizo dummys

numericas_train_media_pad=attr(numericas_train_pad, "scaled:center")
numericas_train_sd_pad=attr(numericas_train_pad, "scaled:scale")
dados_test_pad=cbind(scale(dados_test[,1:6], center = numericas_train_media_pad, scale = numericas_train_sd_pad),dados_test[,7:11])

#com a função grpreg
fit0 <- grpreg(dados_train_pad, y_train, group=gr, penalty="grLasso")
plot(fit0)



#com a função cv.grpreg
regularizador= 0.01 * exp(0.1 * (0:(100-1)))
K=5#Para a validação cruzada
vc_ind=sample(rep(1:K,length.out=nrow(dados_train_pad)))#Para a validação cruzada

fit.grpreg <- cv.grpreg(dados_train_pad, y_train, group=gr, penalty="grLasso",lambda=regularizador,nfolds = K,fold = vc_ind)
# Estrutura do objeto do modelo
str(fit.grpreg)
# Plotar o caminho dos coeficientes
plot(fit.grpreg)
# Coefs. com lambda que retorna o menor EQM (EQM é um caso particular de cve)
coef(fit.grpreg)[-1]

#o modelo aponta que todas as variáveis são importantes
#Comparando os coefs com o lm
summary(lm(y_train~.,data=dados_train_pad))


#rodar sem especificação de lambda e ver a diferença entre o melhor cve e o cve para um lambda que exclui vars 
fit.grpreg$cve[fit.grpreg$min]
fit.grpreg$cve[67]

str(fit.grpreg$fit)
log(fit.grpreg$fit$lambda)
fit.grpreg$fit$beta[,fit.grpreg$min]# mesmo que coef(fit.grpreg)
fit.grpreg$fit$beta[,67]#esse modelo tem habilidade preditiva similar, mas é mais parcimonioso

#EQM nos dados de teste
pred_test=predict(fit.grpreg, X = as.matrix(dados_test_pad),lambda = fit.grpreg$lambda.min)
mean((y_test-pred_test)^2)

pred_test2=predict(fit.grpreg, X = as.matrix(dados_test_pad),lambda = fit.grpreg$fit$lambda[67])
mean((y_test-pred_test2)^2)




# R2 (essa métrica não penaliza o excesso de parâmetros)(o ideal seria o R2_ajustado)
sqr=sum((y_test-pred_test2)^2)
SQT=sum((y_test-mean(y_test))^2)
1-sqr/SQT


summary(y_test-pred_test2)
plot(density(y))


# Plotar previsões versus valores reais
plot(y_test, pred_test2, main="Previsões vs Valores Reais",
     xlab="Valores Reais", ylab="Previsões",
     pch=16, col=rgb(0, 0, 1, 0.5))
abline(a = 0, b = 1, col = "red")

#temos um erro de especificação do modelo (a resposta só assume valores positivos)
plot(table(y),col=2)#inflação de zeros


################################################################################
################################################################################
##########                      SEM os 0's na resposta                ##########                           
################################################################################
################################################################################

#primeiro, apague todos os objetos do R
library(ISLR)
library(fastDummies)
library(grpreg)


cred=Credit
y=cred$Balance
cred=cred[,-c(1,12)]#retira ID e Balance
str(cred)
class(cred)

ind= (y!=0)
y=y[ind]
cred=cred[ind,]#verifique oq aconteceria aqui se eu colocasse y!=0

# Gerando variáveis dummy para a variável 'gender'
data_with_dummies <- dummy_cols(cred, select_columns = c("Gender","Student","Married","Ethnicity"), remove_first_dummy = T)
X=data_with_dummies[,-c(7:10)]




# Ajustar o modelo group lasso
names(X)
gr=c(1,2,3,4,5,6,7,8,9,10,10)




# Separando em treinamento e teste 
n_test=round(0.20*dim(X)[1])
n_train=dim(X)[1]-n_test
test_ind=sample(c(rep("train",n_train),rep("test",n_test)))

dados_train=X[test_ind=="train",]
dados_test=X[test_ind=="test",]
y_train=y[test_ind=="train"]
y_test=y[test_ind=="test"]

#####
str(X)
numericas_train_pad=scale(dados_train[,1:6])
dados_train_pad=cbind(numericas_train_pad,dados_train[,7:11])#não padronizo dummys

numericas_train_media_pad=attr(numericas_train_pad, "scaled:center")
numericas_train_sd_pad=attr(numericas_train_pad, "scaled:scale")
dados_test_pad=cbind(scale(dados_test[,1:6], center = numericas_train_media_pad, scale = numericas_train_sd_pad),dados_test[,7:11])


#Para a validação cruzada
K=5
vc_ind=sample(rep(1:K,length.out=nrow(dados_train_pad)))


regularizador= 0.01 * exp(0.1 * (0:(100-1)))
fit.grpreg <- cv.grpreg(dados_train_pad, y_train, group=gr, penalty="grLasso",lambda=regularizador,nfolds = K,fold = vc_ind)

plot(fit.grpreg)
str(fit.grpreg$fit)
log(fit.grpreg$fit$lambda)
fit.grpreg$fit$beta[,fit.grpreg$min]# mesmo que coef(fit.grpreg)
fit.grpreg$fit$beta[,37]#esse modelo tem habilidade preditiva similar, mas é mais parcimonioso

#EQM nos dados de teste
pred_test=predict(fit.grpreg, X = as.matrix(dados_test_pad),lambda = fit.grpreg$lambda.min)
mean((y_test-pred_test)^2)

pred_test2=predict(fit.grpreg, X = as.matrix(dados_test_pad),lambda = fit.grpreg$fit$lambda[37])
mean((y_test-pred_test2)^2)




# R2 (essa métrica não penaliza o excesso de parâmetros)(o ideal seria o R2_ajustado)
sqr=sum((y_test-pred_test2)^2)
SQT=sum((y_test-mean(y_test))^2)
1-sqr/SQT


# Plotar previsões versus valores reais
plot(y_test, pred_test2, main="Previsões vs Valores Reais",
     xlab="Valores Reais", ylab="Previsões",
     pch=16, col=rgb(0, 0, 1, 0.5))
abline(a = 0, b = 1, col = "red")
#o ajuste fica melhor sem padronizar y.




