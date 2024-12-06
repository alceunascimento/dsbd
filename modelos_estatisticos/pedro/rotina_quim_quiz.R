
# A base de dados de origem química (QUIM), contém 1267 observações e 228
# preditores. Dentre os preditores, 208 são atributos binários que indicam a presença
# ou não de subestruturas químicas específicas, 16 são atributos de contagem e os 4
# restantes são atributos contínuos. Tais informações serão utilizadas para prever a
# solubilidade de uma determinada substância química.


library(corrplot)
library(glmnet)

# Altere o diretório de acordo com a localização do arquivo QUIM.csv no seu computador 
dados=read.csv2(file="~/dsbd/modelos_estatisticos/pedro/bases de dados/quimiometria/QUIM.csv",header = T)
set.seed(1234)
names(dados)
str(dados)
y=as.numeric(dados$Y)
dados=apply(dados[,-1],2,as.numeric)






# Separando em treinamento e teste 
n_test=round(0.20*dim(dados)[1])
n_train=dim(dados)[1]-n_test
test_ind=sample(c(rep("train",n_train),rep("test",n_test)))

dados_train=dados[test_ind=="train",]
dados_test=dados[test_ind=="test",]
y_train=y[test_ind=="train"]
y_test=y[test_ind=="test"]


#####
numericas_train_pad=scale(dados_train[,209:228])
dados_train_pad=cbind(dados_train[,1:208],numericas_train_pad)#não padronizo binárias

numericas_train_media_pad=attr(numericas_train_pad, "scaled:center")
numericas_train_sd_pad=attr(numericas_train_pad, "scaled:scale")
dados_test_pad=cbind(dados_test[,1:208], scale(dados_test[,209:228], center = numericas_train_media_pad, scale = numericas_train_sd_pad))


# Calcular a matriz de correlação para as numéricas
cor_matrix = cor(dados[,209:228])
corrplot(cor_matrix, 
         method = "ellipse", 
         order = "hclust", 
         tl.col = "black", 
         tl.cex = 0.8, 
         cl.cex = 0.8, 
         type="upper")


#Para a validação cruzada
K=5
vc_ind=sample(rep(1:K,length.out=nrow(dados_train_pad)))

regularizador=seq(0,5,by=0.0025)

# Ajustar o modelo de regressão com penalização elastic net

fit_LASSO  = cv.glmnet(dados_train_pad, y_train, family = "gaussian", alpha = 1,lambda = regularizador,nfolds = K,foldid = vc_ind)#LASSO
fit_RIDGE = cv.glmnet(dados_train_pad, y_train, family = "gaussian", alpha = 0,lambda = regularizador,nfolds = K,foldid = vc_ind)#RIDGE
fit_EN = cv.glmnet(dados_train_pad, y_train, family = "gaussian", alpha = 0.1,lambda = regularizador,nfolds = K,foldid = vc_ind)

