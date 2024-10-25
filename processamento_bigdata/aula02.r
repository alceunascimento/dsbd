# Teste de db4free

# fiz o cadastro no site e entrei pelo phpadmin da pagina do db4free

# SETUP ----
library(RMySQL)

# DATA WAREHOUSE CONNECTTION ----
con <- dbConnect(MySQL(),
    host="db4free.net",
    user="aenascimento",
    password="Outros22@",
    dbname="dsbdaen2024")

# Defina os detalhes da conexão
host <- "db4free.net"
dbname <- "dsbdaen2024"
user <- "aenascimento"
password <- password
port <- 3306  # Porta padrão do MySQL


# Crie a conexão
con <- dbConnect(MySQL(),
                     dbname = dbname,
                     host = host,
                     port = port,
                     user = user,
                     password = password)


dbGetInfo(con)
dbListTables(con)

library(readr)

teste <- dbGetQuery(con, "SELECT * FROM teste")
rental <- dbGetQuery(con, "SELECT * FROM rental")


dbDisconnect(con)


