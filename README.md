# convert_toSQLTable
Código que converte planilhas(xls,xlsx,csv) para Table do SQL

------------------------------------------------------------------
Para instalar as dependências: pip install -r requirements.txt

------------------------------------------------------------------

Subir API:

-linux: python3 main.py

-windows: python main.py


Buildar imagem docker:
-Comando: docker build . -t nome_da_imagem

docker build. -t "convert_table"

Subir container com imagem criada:
-Comando: docker run -p porta_externa:porta_interna --name nome_do_container -d nome_da_imagem

Subindo docker-compose:
-Comando: docker-compose up 