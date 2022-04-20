from flask import Flask

app = Flask(__name__)

@app.route("/",)
def index():
    
    return '''Olá!\n
    Essa API tem como propósito pegar os dados de uma planilha (xls,xlsx,csv) e retornar\n
    o código para criar uma tabela SQL e também populá-la com as informações!
    '''
    
if __name__ == "__main__":
    app.run(debug=False, port=8128, host="0.0.0.0")