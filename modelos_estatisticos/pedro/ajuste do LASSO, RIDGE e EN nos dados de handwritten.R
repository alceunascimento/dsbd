library(corrplot)
library(glmnet)
library(grpreg)
library(pROC)
setwd("D:/Users/pedro/Documents/MEGA/Documentos/trabalho/5-Professor Classe A - UFPR/06-especialização/aula_regl/bases de dados/handwritten")

# Hand-Written Digits: Base que possui 200 observações e 256 variáveis. Cada
# observação representa uma imagem 16x16 de um número escrito a mão. 
# 
# Cada linha da matriz de dados é uma imagem, enquanto as colunas são os pixels desta
# imagem, representados por um número que provém de uma escala de cinzas.
# 
# cada variável representa um valor na escala de cinzas para o respectivo pixel.
# 
# A variável resposta contém duas classes: dígitos 5 e 6 de tal forma que os rótulos são -1 e 1, respectivamente.



let=read.table("uspsdata.txt")
dim(let)
clet=read.table("uspscl.txt")
y=as.numeric(as.matrix(clet))
str(y)
table(y)
y[y==-1]=0

apply(let, 2, range)
dados=as.data.frame(let)


# Separando em treinamento e validação 
n_test=round(0.20*dim(dados)[1])
n_train=dim(dados)[1]-n_test
test_ind=sample(c(rep("train",n_train),rep("test",n_test)))

dados_train=dados[test_ind=="train",]
dados_test=dados[test_ind=="test",]
y_train=y[test_ind=="train"]
y_test=y[test_ind=="test"]


dados_train_pad=scale(dados_train)
media_pad=attr(dados_train_pad, "scaled:center")
sd_pad=attr(dados_train_pad, "scaled:scale")
dados_test_pad=scale(dados_test,center = media_pad,scale = sd_pad)




# Calcular a matriz de correlação
cor_matrix = cor(dados)
# corrplot(cor_matrix, method = "ellipse", order = "hclust", tl.col = "black", tl.cex = 0.8, cl.cex = 0.8, type="upper")
# corrplot(cor_matrix, method = "color", order = "hclust", addrect = 2, tl.col = "black", tl.cex = 0.8, cl.cex = 0.8)

# Calcular submatriz com todas as covs que têm ao menos uma correlação maior do que 0.95 
diag(cor_matrix) = NA
upper_tri_values = cor_matrix[upper.tri(cor_matrix, diag = FALSE)]
top_indices = which(abs(cor_matrix)>= 0.95, arr.ind = TRUE)
top_vars = unique(as.numeric(top_indices))
sub_cor_matrix = cor_matrix[top_vars, top_vars]
diag(sub_cor_matrix)=1
corrplot(sub_cor_matrix, method = "color", order = "hclust", addrect = 2, tl.col = "black", tl.cex = 0.8, cl.cex = 0.8)
dim(sub_cor_matrix)# 94 variáveis têm pelo menos uma correlação maior do que 0.95





# Ajustar o modelo logístico com penalização elastic net
# family = "binomial" para regressão logística
fit_LASSO  = cv.glmnet(dados_train_pad, y_train, family = "binomial", alpha = 1,type.measure = "class")#LASSO
fit_RIDGE = cv.glmnet(dados_train_pad, y_train, family = "binomial", alpha = 0,type.measure = "class")#RIDGE
fit_EN = cv.glmnet(dados_train_pad, y_train, family = "binomial", alpha = 0.5,type.measure = "class")



str(fit_LASSO)
plot(fit_LASSO)
fit_LASSO$lambda.min
fit_LASSO$cvm[fit_LASSO$lambda == fit_LASSO$lambda.min]
table(as.numeric(coef(fit_LASSO, s = "lambda.min")[-1])==0)
plot(as.numeric(coef(fit_LASSO, s = "lambda.min")[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes
plot(fit_LASSO$glmnet.fit, xvar = "lambda", label = TRUE)
# Prevê as classes usando o modelo ajustado e calcula a matriz de confusão
predictions1 = predict(fit_LASSO, newx = dados_test_pad, s=fit_LASSO$lambda.min, type = "class")
# predictions1 = ifelse(predictions1 > 0.5, 1, 0)#só se type="response"
confusion_matrix = table(Predicted = predictions1, Actual = y_test)
# Calcular a curva ROC
predictions1_roc = predict(fit_LASSO, newx = dados_test_pad, s=fit_LASSO$lambda.min, type = "response")
roc_curve1 = roc(y_test, as.numeric(predictions1_roc))
plot(roc_curve1, main = "Curva ROC", col = "blue")
# Calcular a área sob a curva ROC (AUC-ROC)
auc(roc_curve1)




str(fit_RIDGE)
plot(fit_RIDGE)
fit_RIDGE$lambda.min
fit_RIDGE$cvm[fit_RIDGE$lambda == fit_RIDGE$lambda.min]
table(as.numeric(coef(fit_RIDGE, s = "lambda.min")[-1])==0)
plot(as.numeric(coef(fit_RIDGE, s = "lambda.min")[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes
plot(fit_RIDGE$glmnet.fit, xvar = "lambda", label = TRUE)
# Prevê as classes usando o modelo ajustado e calcula a matriz de confusão
predictions2 = predict(fit_RIDGE, newx = dados_test_pad, s=fit_RIDGE$lambda.min, type = "class")
# predictions2 = ifelse(predictions2 > 0.5, 1, 0)#só se type="response"
confusion_matrix = table(Predicted = predictions2, Actual = y_test)
# Calcular a curva ROC
predictions2_roc = predict(fit_RIDGE, newx = dados_test_pad, s=fit_RIDGE$lambda.min, type = "response")
roc_curve2 = roc(y_test, as.numeric(predictions2_roc))
plot(roc_curve2, main = "Curva ROC", col = "blue")
# Calcular a área sob a curva ROC (AUC-ROC)
auc(roc_curve2)




str(fit_EN)
plot(fit_EN)
fit_EN$lambda.min
fit_EN$cvm[fit_EN$lambda == fit_EN$lambda.min]
table(as.numeric(coef(fit_EN, s = "lambda.min")[-1])==0)
plot(as.numeric(coef(fit_EN, s = "lambda.min")[-1]),type="h",col=2)
# Plotar a evolução dos coeficientes
plot(fit_EN$glmnet.fit, xvar = "lambda", label = TRUE)
# Prevê as classes usando o modelo ajustado e calcula a matriz de confusão
predictions3 = predict(fit_EN, newx = dados_test_pad, s=fit_EN$lambda.min, type = "class")
# predictions3 = ifelse(predictions3 > 0.5, 1, 0)#só se type="response"
confusion_matrix = table(Predicted = predictions3, Actual = y_test)

# Calcular a curva ROC
predictions3_roc = predict(fit_EN, newx = dados_test_pad, s=fit_EN$lambda.min, type = "response")
roc_curve3 = roc(y_test, as.numeric(predictions3_roc))
plot(roc_curve3, main = "Curva ROC", col = "blue")
# Calcular a área sob a curva ROC (AUC-ROC)
auc(roc_curve3)









cor_matrix2 = cor(dados[,as.numeric(coef(fit_LASSO)[-1])!=0])
corrplot(cor_matrix2, method = "color", order = "hclust", addrect = 2, tl.col = "black", tl.cex = 0.8, cl.cex = 0.8)
cor_matrix2 = cor(dados[,as.numeric(coef(fit_EN)[-1])!=0])
corrplot(cor_matrix2, method = "color", order = "hclust", addrect = 2, tl.col = "black", tl.cex = 0.8, cl.cex = 0.8)




















