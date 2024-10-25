class Worker:
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