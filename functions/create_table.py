def generate_table(name,file) -> str:

    from functions.read_file import read_file
    rf = read_file(file)

    columns_info = rf.get_collumns_info()
    lista = []
    counter = 1
    for i in columns_info:

        if columns_info.get(i) == 'int64':
            item = f'''    {i} INT,\n'''
            lista.append(item)
        
        elif columns_info.get(i) == 'O':
            item = f'''    {i} VARCHAR(255),\n'''
            lista.append(item)
        
        if columns_info.__len__() == counter:
            value:str = lista[-1]
            lista.pop(-1)
            lista.append(value.replace(',\n','\n)'))

        counter+=1

    create = f'''CREATE TABLE {name} (
    ID INT NOT NULL AUTO_INCREMENT,\n'''

    for i in lista:

        create += i
    
    return create