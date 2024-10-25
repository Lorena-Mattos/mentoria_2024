from unittest import mock
import pytest
from projeto_calculadora.calculadora import Calculadora


def test_operacao_desconhecida():
    calc = Calculadora()
    with mock.patch('builtins.input', return_value='desconhecida'):
        with pytest.raises(SystemExit):  # Se sua função usa exit() para encerrar
            calc.calculo()


def test_soma():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['soma', '2', '3']):
        resultado = calc.calculo()
        assert resultado == 5


def test_subtracao():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['subtração', '5', '3']):
        resultado = calc.calculo()
        assert resultado == 2


def test_multiplicacao():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['multiplicação', '4', '3']):
        resultado = calc.calculo()
        assert resultado == 12


def test_divisao():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['divisão', '6', '2']):
        resultado = calc.calculo()
        assert resultado == 3


def test_divisao_por_zero():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['divisão', '6', '0']):
        resultado = calc.calculo()
        assert resultado is None  # Verifica que o resultado é None para divisão por zero


def test_resultado_inteiro():
    calc = Calculadora()
    with mock.patch('builtins.input', side_effect=['soma', '2', '2']):
        resultado = calc.calculo()
        assert resultado == 4  # Verifica que o resultado inteiro retorna como int
