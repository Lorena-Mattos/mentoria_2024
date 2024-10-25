class Worker:  
    def __init__(self, client):  
        self.client = client  

    def transform(self, value, convert_to):  
        """  
        Método que converte o valor de entrada para o tipo especificado.  

        Args:  
            value (str): O valor a ser convertido.  
            convert_to (str): O tipo de conversão desejado ('int', 'float', etc).  

        Returns:  
            O valor convertido.  
        """  
        if convert_to == 'int':  
            return int(float(value))  
        elif convert_to == 'float':  
            return float(value)  
        else:  
            raise ValueError(f"Tipo de conversão '{convert_to}' não suportado.")  

    def table_exists(self, database_name):  
        """  
        Verifica se uma tabela existe no banco de dados.  

        Args:  
            database_name (str): O nome do banco de dados.  

        Returns:  
            bool: True se a tabela existe, False caso contrário.  
        """  
        result = self.client.query(f"SELECT * FROM {database_name} LIMIT 1")  
        return bool(result)  

    def get_file_content_to_file(self, file_name):  
        """  
        Obtém o conteúdo de um arquivo blob e salva em um arquivo local.  

        Args:  
            file_name (str): O nome do arquivo blob a ser obtido.  
        """  
        blob_content = self.client.get_blob({'blob_name': file_name})  
        with open(file_name, 'wb') as file:  
            file.write(blob_content)