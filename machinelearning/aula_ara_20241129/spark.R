# SETUP

library(ggplot2)
library(dplyr)
library(sparklyr)
library(dbplot)

# SET SPARK ----
sc <- spark_connect(master = "local")
spark_version(sc)

# GET DATA
setwd("~/Documentos/data/")


df_ac <- spark_read_csv(
          sc,
          name = "accepted_data",
          path = "accepted_2007_to_2018Q4.csv",
          memory = FALSE,
          delim = ",",
          dec = "."
  )

glimpse(df_ac)

df_rj <- spark_read_csv(
          sc,
          name = "rejected_data",
          path = "rejected_2007_to_2018Q4.csv",
          memory = FALSE,
          delim = ",",
          dec = "."
)
glimpse(df_rj)

# ANALYS ----

df_rj |> count()
df_ac |> count()


df_ac |>
  select(loan_amnt, int_rate) |> 
  

df_rj |> filter(Amount_Requested <= 100000) |> 
  dbplot


df_ac |> select(loan_amnt, int_rate) |> 
  dbplot_raster(loan_amnt, int_rate) +
  scale_fill_gradient(low = "blue",
                      high = "red") +
  theme_bw()+
  theme(legend.position = "botton")
  
## retirando uma amosta de dados do objeto ----

df_ac_sample <- df_ac |> 
  sample_n(3000) |>  
  collect()

glimpse(df_ac_sample)  


df_ac_sample |> 
  ggplot(aes(x=loan_amnt, y=int_rate)) + 
    geom_point(alpha=0.15)+
    theme_bw()
  
## correlacao ----
library(corrr)

df_ac |> colnames()

df_ac |> 
  select(loan_amnt, int_rate, installment) |> 
  na.omit() |> 
  correlate()

ml_linear_regression(df_rj, Risk_Score ~ DebtToIncome_Ratio)  

