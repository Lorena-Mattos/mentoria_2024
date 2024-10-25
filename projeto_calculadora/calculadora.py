import sys


class Calculadora:
    def calculo(self):
        operacao = input("Qual operação deseja efetuar (soma, subtração, multiplicação, divisão)? ")

        if operacao in ["soma", "subtração", "multiplicação", "divisão"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == "soma":
                resultado = self.soma(num1, num2)
            elif operacao == "divisão":
                resultado = self.divisao(num1, num2)
                if resultado is None:  # Se resultado for None, retorne
                    return None
            elif operacao == "subtração":
                resultado = self.subtracao(num1, num2)
            elif operacao == "multiplicação":
                resultado = self.multiplicacao(num1, num2)
            else:
                print("Operação desconhecida")
                return None

            resultado = round(resultado, 2)

            if resultado.is_integer():
                resultado = int(resultado)

            print(f"Resultado: {resultado}")
            return resultado
        else:
            print("Operação desconhecida")
            sys.exit()

    def soma(self, a, b):
        return a + b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b
