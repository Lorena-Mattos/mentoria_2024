# arquivo test_weather.py
from weather import get_weather


def test_get_weather(mocker):
    # Simulando a resposta da requests.get
    mock_response = mocker.patch('requests.get')

    # Definindo o valor retornado pela simulação
    mock_response.return_value.json.return_value = {'temperature': 25}

    # Agora quando chamarmos get_weather, ele usará o valor simulado
    temperature = get_weather()

    assert temperature == 25  # Verificando se o valor foi o esperado
