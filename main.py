from flask import Flask, request, redirect,url_for

app = Flask(__name__)

@app.route("/",)
def index():
    
    n = open('./index.html')
    html = n.read()
    return html

@app.route("/CREATE_TABLE",methods=['POST'])
def create_table():
    from functions.create_table import generate_table
    sql_create = generate_table(request.form.get('name'),request.form.get('file_dir'))
    
    import datetime
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    
    file = f'create_{date.year+date.month+date.day}.sql'
    with open(f"./static/{file}",'w',encoding = 'utf-8') as file:
        file.write(sql_create)

    return redirect(url_for('static', filename=file))

@app.route("/INSERT_TABLE",methods=['POST'])
def insert_table():
    from functions.populate_table import populate_table
    sql_insert = populate_table(request.form.get('name'),request.form.get('file_dir'))
    
    import datetime
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    
    file = f'insert_{date.year+date.month+date.day}.sql'
    with open(f"./static/{file}",'w',encoding = 'utf-8') as file:
        file.write(sql_insert)

    return redirect(url_for('static', filename=file))

@app.route("/CREATE_AND_POPULATE",methods=['POST'])
def create_and_populate():
    from functions.create_table import generate_table
    from functions.populate_table import populate_table

    sql_create = generate_table(request.form.get('name'),request.form.get('file_dir'))
    sql_insert = populate_table(request.form.get('name'),request.form.get('file_dir'))

    import datetime
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    
    file = f'cap_{date.year+date.month+date.day}.sql'
    with open(f"./static/{file}",'w',encoding = 'utf-8') as file:
        file.write(sql_create)
        file.write(sql_insert)

    return redirect(url_for('static', filename=file))
    
if __name__ == "__main__":
    app.run(debug=False, port=8128, host="0.0.0.0")