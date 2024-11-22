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


dados=read.delim(file="D:/Users/pedro/Documents/MEGA/Documentos/trabalho/5-Professor Classe A - UFPR/06-especialização/aula_regl/bases de dados/prostata/prostate.txt")
names(dados)
y=dados[,"lpsa"]
dados=dados[,-c(1,10,11)]
names(dados)
mydata=dados



# Modelo nulo (sem preditores)
model_null <- lm(y ~ 1, data = mydata)
# Modelo completo (com todos os preditores)
model_full <- lm(y ~ ., data = mydata)
summary(model_full)

# Seleção Forward
forward_model <- step(model_null, 
                      scope = list(lower = model_null, upper = model_full), 
                      direction = "forward")
# Step:  AIC=-63.72
# y ~ lcavol + lweight + svi + lbph + age

# Seleção Backward
backward_model <- step(model_full,
                       scope = list(lower = model_null, upper = model_full),
                       direction = "backward")
# Step:  AIC=-63.72
# y ~ lcavol + lweight + age + lbph + svi

# Seleção Stepwise
stepwise_model <- step(model_null, 
                       scope = list(lower = model_null, upper = model_full), 
                       direction = "both")
# Step:  AIC=-63.72
# y ~ lcavol + lweight + svi + lbph + age

stepwise_model <- step(model_full, 
                       scope = list(lower = model_null, upper = model_full), 
                       direction = "both")
# Step:  AIC=-63.72
# y ~ lcavol + lweight + age + lbph + svi



summary(stepwise_model)



