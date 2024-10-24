# testes/test_project.py
from button import Button


def test_button_activation():
    # Cria uma instância do botão
    button = Button()

    # Verifica se o botão está inicialmente desativado
    assert not button.is_enabled(), "O botão deveria estar desativado inicialmente."

    # Simula o clique no botão
    button.click()

    # Verifica se o botão foi ativado após o clique
    assert button.is_enabled(), "O botão deveria estar ativado após o clique."
