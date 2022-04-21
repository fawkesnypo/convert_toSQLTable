import pandas as pd

class read_file:

    def __init__(self,file_dir:str) -> None:
        
        if file_dir.endswith('.csv'):
            self.data = pd.read_csv(file_dir)

        elif file_dir.endswith('xls') or file_dir.endswith('xlsx'):
            self.data = pd.read_excel(file_dir)

    #Função que retorna informações das colunas(nome,tipo)
    def get_columns_info(self) -> dict:
            
        columns_list = self.data.columns.values.tolist()

        collumns_info = {collumn: self.data.dtypes[collumn] for collumn in columns_list}

        return collumns_info
    
    def get_columns_values(self) -> dict:

        columns_list = self.data.columns.values.tolist()
        
        columns_values = {}
        for column_name in columns_list:

            columns_values_list = self.data[column_name].values.tolist()

            columns_values[column_name] = columns_values_list
        
        return columns_values