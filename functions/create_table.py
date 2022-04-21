def generate_table(name,file) -> str:

    from functions.read_file import read_file
    rf = read_file(file)

    columns_info = rf.get_columns_info()
    lista = []
    counter = 1
    for column_name in columns_info:

        if columns_info.get(column_name) == 'int64':
            item = f'''    {column_name} INT,\n'''
            lista.append(item)
        
        elif columns_info.get(column_name) == 'O':
            item = f'''    {column_name} VARCHAR(255),\n'''
            lista.append(item)
        
        if columns_info.__len__() == counter:
            value:str = lista[-1]
            lista.pop(-1)
            lista.append(value.replace(',\n',',\nPRIMARY KEY (ID)\n)'))

        counter+=1

    create = f'''CREATE TABLE {name} (
    ID INT NOT NULL AUTO_INCREMENT,\n'''

    for item in lista:

        create += item
    
    return create