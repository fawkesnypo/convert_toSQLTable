from flask import Flask, request

app = Flask(__name__)

@app.route("/",)
def index():
    
    return '''Olá!\n
    Essa API tem como propósito pegar os dados de uma planilha (xls,xlsx,csv) e retornar\n
    o código para criar uma tabela SQL e também populá-la com as informações!
    '''

@app.route("/CREATE_TABLE",methods=['POST'])
def create_table():
    from functions.create_table import generate_table
    sql_create = generate_table(request.form.get('name'),request.form.get('file_dir'))
    return sql_create

    
if __name__ == "__main__":
    app.run(debug=False, port=8128, host="0.0.0.0")