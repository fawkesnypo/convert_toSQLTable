def populate_table(name,file) -> str:

    from functions.read_file import read_file
    rf = read_file(file)

    columns = rf.get_columns_values()
    lista_column_name = []
    counter = 1

    for column in columns:

        if columns.__len__() == counter:
            lista_column_name.append(f'{column})\n')
        
        else:
            lista_column_name.append(f'{column}, ')
        
        counter+=1


    insert = f'''INSERT INTO {name}('''

    for item in lista_column_name:

        insert += item
    
    lista_values = []
    counter = 0

    keys = list(columns.keys())

    for count in range(columns[keys[0]].__len__()):

        values = '''VALUES ('''

        counter_2 = 1
        for key in keys:

            if columns.__len__() == counter_2:

                if type(columns[key][counter]) != int:
                    if str.isalnum(columns[key][counter]):
                        values += f"""'{columns[key][counter]}'),\n"""
                    
                    elif str.isnumeric(columns[key][counter]):
                        values += f'{int(columns[key][counter])}),\n'
                    
                elif type(columns[key][counter]) == int:
                    values += f'{columns[key][counter]}),\n '
            
            elif type(columns[key][counter]) != int:
                if str.isalnum(columns[key][counter]):
                    values += f"""'{columns[key][counter]}', """
                
                elif str.isnumeric(columns[key][counter]):
                    values += f'{int(columns[key][counter])}, '

            elif type(columns[key][counter]) == int:
                values += f'{columns[key][counter]}, '

            counter_2 +=1

        lista_values.append(values)
        counter +=1


    for value in lista_values:

        insert += value

    return insert