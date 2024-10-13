# MODELO ESTATISTICOS : AVALIACAO 02 -------------------------------------------
# SETUP ------------------------------------------------------------------------
library(faraway)
library(pROC)

rm(list = ls())

# GET DATA ---------------------------------------------------------------------
wbca <- wbca
str(wbca)


# WRANGLER DATA ----------------------------------------------------------------
wbca$Class <- factor(wbca$Class, levels = c('1', '0'))
str(wbca)

# Base de ajuste 
wbca_ajuste <- wbca[1:500, ]

# Base de validação
wbca_validacao <- wbca[501:681, ]

# MODELO
modelo <- glm(Class ~ Adhes + BNucl + Thick, 
              data = wbca_ajuste, 
              family = binomial)
summary(modelo)


# Previsão das probabilidades na base de validação
probabilidades <- predict(modelo, 
                          newdata = wbca_validacao, 
                          type = "response")
probabilidades

# Convertendo as probabilidades para classes (maligno ou benigno)
previsoes <- ifelse(probabilidades > 0.5, 0, 1)
previsoes

# Matriz de confusão
table(wbca_validacao$Class, previsoes)



# QUESTOES ---------------------------------------------------------------------

## Questão 01 ----
"""
Qual a chance estimada de tumor maligno para uma observação com as seguintes 
características:

Adhes = 4
BNucl = 7
Thick = 5

Escolha uma opção:
a. 5.50
b. 3.50
c. 7.50
d. 11.50
e. 9.50
"""

# Criar um novo data frame com as características fornecidas
nova_observacao <- data.frame(Adhes = 4, 
                              BNucl = 7, 
                              Thick = 5)

# Usar o modelo ajustado para prever a probabilidade
probabilidade_maligno <- predict(modelo, 
                                 newdata = nova_observacao, 
                                 type = "response")

# Calcular as odds associadas à probabilidade
odds <- probabilidade_maligno / (1 - probabilidade_maligno)

# Mostrar o resultado
odds



## Questão 02 ----
"""
Qual a probabilidade estimada de tumor maligno para uma observação com as 
seguintes características:

Adhes = 4
BNucl = 7
Thick = 5

Escolha uma opção:
a. 0.70
b. 0.90
c. 0.50
d. 0.80
e. 0.60
"""

# Criar um novo data frame com as características fornecidas
nova_observacao <- data.frame(Adhes = 4, 
                              BNucl = 7, 
                              Thick = 5)

# Usar o modelo ajustado para prever a probabilidade de malignidade
probabilidade_maligno <- predict(modelo, 
                                 newdata = nova_observacao, 
                                 type = "response")

# Mostrar o resultado
probabilidade_maligno


## Questão 03 ----
"""
Considere a seguinte conjectura:

Estima-se um que a chance de tumor maligno aumente K% para um aumento unitário 
em BNucl mantendo fixos Adhes e Thick.
Qual das alternativas abaixo apresenta o valor de K?

Escolha uma opção:
a. 88
b. 68
c. 48
d. 128
e. 108
"""

# Calcular o odds ratio
odds_ratio_bnucl <- exp(coef(modelo)["BNucl"])
# Calcular o aumento percentual K%
K <- (odds_ratio_bnucl - 1) * 100
K


## Questão 04 ----
"""
Considere a seguinte conjectura:

Estima-se um que a chance de tumor maligno aumente K% para um aumento de duas 
unidades em Adhes mantendo fixos BNucl e Thick.
Qual das alternativas abaixo apresenta o valor de K?

Escolha uma opção:
a. 224
b. 274
c. 124
d. 74
e. 174
"""

# Calcular o odds ratio para um aumento de 2 unidades em Adhes
odds_ratio_adhes_2 <- exp(2 * coef(modelo)["Adhes"])
# Calcular o aumento percentual K%
K <- (odds_ratio_adhes_2 - 1) * 100
K

## Questão 05 ----
"""
O número de variáveis explicativas que estão significativamente associadas ao 
tipo de tumor, ao nível de significância de 5%, é:

Escolha uma opção:
a. 1
b. 2
c. 4
d. 0
e. 3
"""


# p-value de cada coeficiente e contando quantos são menores que 0.05
coeficientes <- summary(modelo)$coefficients
p_values <- coeficientes[, 4]  # Pega a coluna de p-values
significativas <- sum(p_values < 0.05) - 1
significativas


## Questão 06 ----
"""
Qual das alternativas a seguir apresenta um intervalo de confiança (95%) para a 
chance estimada de tumor maligno para uma observação com as seguintes 
características:

Adhes = 4
BNucl = 7
Thick = 5

Escolha uma opção:
a. (3.98 ; 22.62)
b. (5.98 ; 20.62)
c. (4.98 ; 21.62)
d. (6.98 ; 19.62)
e. (7.98 ; 18.62)
"""


# Criar um novo data frame com as características fornecidas
nova_observacao <- data.frame(Adhes = 4, 
                              BNucl = 7, 
                              Thick = 5)

# Prever a log-odds e o erro padrão associado
log_odds_pred <- predict(modelo, 
                         newdata = nova_observacao, 
                         se.fit = TRUE)

# Valores das log-odds e erro padrão
log_odds <- log_odds_pred$fit
se_log_odds <- log_odds_pred$se.fit

# Calcular o intervalo de confiança para as log-odds (95% de confiança)
z_value <- qnorm(0.975)  # 2,5% para cada lado da distribuição
ci_log_odds_lower <- log_odds - z_value * se_log_odds
ci_log_odds_upper <- log_odds + z_value * se_log_odds

# Transformar para a escala das odds (chances)
ci_odds_lower <- exp(ci_log_odds_lower)
ci_odds_upper <- exp(ci_log_odds_upper)
ci_odds_lower
ci_odds_upper



## Questão 07 ----
"""
Qual das alternativas a seguir apresenta um intervalo de confiança (95%) para a 
probabilidade estimada de tumor maligno para uma observação com as seguintes 
características:

Adhes = 4
BNucl = 7
Thick = 5

Escolha uma opção:

a. (0.855 ; 0.945)
b. (0.837 ; 0.973)
c. (0.799 ; 0.957)
d. (0.888 ; 0.912)
e. (0.752 ; 0.987)
"""


# Criar um novo data frame com as características fornecidas
nova_observacao <- data.frame(Adhes = 4, 
                              BNucl = 7, 
                              Thick = 5)

# Prever a log-odds e o erro padrão associado
log_odds_pred <- predict(modelo, 
                         newdata = nova_observacao, 
                         se.fit = TRUE)

# Valores das log-odds e erro padrão
log_odds <- log_odds_pred$fit
se_log_odds <- log_odds_pred$se.fit

# Calcular o intervalo de confiança para as log-odds (95% de confiança)
z_value <- qnorm(0.975)  # Valor crítico para 95% de confiança
ci_log_odds_lower <- log_odds - z_value * se_log_odds
ci_log_odds_upper <- log_odds + z_value * se_log_odds

# Transformar as log-odds para a escala de probabilidades
prob_lower <- exp(ci_log_odds_lower) / (1 + exp(ci_log_odds_lower))
prob_upper <- exp(ci_log_odds_upper) / (1 + exp(ci_log_odds_upper))
prob_lower
prob_upper




## Questão 08 ----
"""
Com base na amostra de validação, a acurácia estimada do modelo, ao classificar 
como tumor maligno as observações com probabilidade estimada maior que 0.50, e 
como tumor benigno as observações com probabilidade estimada menor que 0.50, 
é igual a:

Escolha uma opção:
a. 0.94
b. 0.96
c. 1.00
d. 0.92
e. 0.98
"""


# Prever as probabilidades na base de validação
probabilidades_validacao <- predict(modelo, 
                                    newdata = wbca_validacao, 
                                    type = "response")

# Classificar como maligno (0) ou benigno (1) com base na probabilidade
previsoes_validacao <- ifelse(probabilidades_validacao > 0.5, 0, 1)

# Acurácia comparando previsões com a variável Class da base de validação
acuracia <- mean(previsoes_validacao == wbca_validacao$Class)
acuracia



## Questão 09 ----
"""
Com base na amostra de validação, a sensibilidade estimada do modelo, ao 
classificar como tumor maligno as observações com probabilidade estimada maior 
que 0.50, e como tumor benigno as observações com probabilidade estimada menor 
que 0.50, é igual a:

Escolha uma opção:
a. 0.90
b. 0.85
c. 1.00
d. 0.95
e. 0.80

"""


# Prever as probabilidades na base de validação
probabilidades_validacao <- predict(modelo, 
                                    newdata = wbca_validacao, 
                                    type = "response")

# Classificar como maligno (0) ou benigno (1) com base na probabilidade
previsoes_validacao <- ifelse(probabilidades_validacao > 0.5, 0, 1)

# Criar a matriz de confusão
matriz_confusao <- table(wbca_validacao$Class, previsoes_validacao)
matriz_confusao

# Extrair verdadeiros positivose e falsos negativos
# (malignos previstos corretamente) (malignos previstos incorretamente)
verdadeiros_positivos <- matriz_confusao[2, 1]  # Maligno previsto como maligno (0,0)
falsos_negativos <- matriz_confusao[2, 2]       # Maligno previsto como benigno (0,1)

# Calcular a sensibilidade
sensibilidade <- verdadeiros_positivos / (verdadeiros_positivos + falsos_negativos)
sensibilidade

## Questão 10 ----
"""
Com base na amostra de validação, a especificidade estimada do modelo, ao 
classificar como tumor maligno as observações com probabilidade estimada maior 
que 0.50, e como tumor benigno as observações com probabilidade estimada menor 
que 0.50, é igual a:
  
Escolha uma opção:
a. 0.85
b. 0.80
c. 0.95
d. 1.00
e. 0.90
"""
# Extrair verdadeiros negativos e falsos positivos
verdadeiros_negativos <- matriz_confusao[1, 2]  # Benigno previsto corretamente
falsos_positivos <- matriz_confusao[1, 1]       # Benigno previsto incorretamente como maligno (0)

# Calcular a especificidade
especificidade <- verdadeiros_negativos / (verdadeiros_negativos + falsos_positivos)
especificidade



## Questão 11 ----
"""
Com base na amostra de validação, a área sob a curva ROC produzida pelo modelo 
é igual a:

Escolha uma opção:
a. 0.9878
b. 0.9778
c. 0.9978
d. 0.9828
e. 0.9928
"""


# Prever as probabilidades na base de validação
probabilidades_validacao <- predict(modelo, 
                                    newdata = wbca_validacao, 
                                    type = "response")

# Gerar a curva ROC e calcular a AUC
roc_obj <- roc(wbca_validacao$Class, probabilidades_validacao)

# Exibir a AUC
auc(roc_obj)

## Questão 12 ----
"""
Com base na amostra de validação, e usando o método de Youden, a regra de 
classificação ótima ao se considerar as informações fornecidas na sequência 
consiste em classificar um tumor como maligno caso a probabilidade estimada 
seja superior a K.

Prevalência de tumor maligno igual a 0.20;
Custo de classificar um tumor positivo como negativo é três vezes o custo de 
classificar um tumor negativo como positivo.
Qual o valor de K?

Escolha uma opção:
a. 0.119
b. 0.169
c. 0.269
d. 0.219
e. 0.319
"""

# Prever as probabilidades na base de validação
probabilidades_validacao <- predict(modelo, 
                                    newdata = wbca_validacao, 
                                    type = "response")

# Gerar a curva ROC
roc_obj <- roc(wbca_validacao$Class, probabilidades_validacao)

# Aplicar o método de Youden para encontrar o limiar ótimo (threshold)
youden_threshold <- coords(roc_obj, "best", 
                           ret = "threshold", 
                           best.method = "youden")

# Parâmetros de prevalência e custo relativo
prevalencia <- 0.20
custo_falso_negativo <- 3
custo_falso_positivo <- 1

# Ajustar o valor de corte Youden considerando os custos assimétricos e a prevalência
# A fórmula ajusta o valor Youden com base nos custos relativos e prevalência
K <- youden_threshold * (custo_falso_negativo * prevalencia) / 
  (custo_falso_negativo * prevalencia + custo_falso_positivo * (1 - prevalencia))

# Mostrar o valor de K ajustado
K





