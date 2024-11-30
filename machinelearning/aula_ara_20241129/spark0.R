


# SETUP -----
library(dplyr)
library(sparklyr)
library(ggplot2)

# SET SPARK ----
sc <- spark_connect(master="local")
spark_version(sc)


GET DATA ----
setwd("~/Documentos/data/")


df_acpt <- spark_read_csv(sc,
                          "accepted_2007_to_2018Q4.csv",
                          memory = FALSE,
                          delim =",",
                          dec =".")

df_rjct <- spark_read_csv(sc,
                          "rejected_2007_to_2018Q4.csv",
                          memory = FALSE,
                          delim =",",
                          dec =".")


# ANALYSIS ----

## tests and learning ----
df_acpt %>% count()

n_re <- df_rjct %>% count()
n_re


n_re <- df_rjct %>% count() |> collect()
n_re
n_re+1

df_rjct |> sdf_ncol()
sdf_ncol(df_rjct)

class(df_rjct)
glimpse(df_rjct)

df_rjct |> summarise(m=mean(Amount_Requested))

require(dbplot)

df_rjct |> filter(Amount_Requested <= 100000) |> 
  dbplot_histogram(Amount_Requested, bins = 10) +
  labs(title= "Amount Requested up to US$ 100.000") +
  theme_bw()


##    -------


