# button.py

class Button:
    def __init__(self):
        self.enabled = False  # O botão começa desativado

    def click(self):
        if not self.enabled:  # Se o botão estiver desativado, ative-o
            self.enabled = True

    def is_enabled(self):
        return self.enabled  # Verifica se o botão está ativado ou desativado
