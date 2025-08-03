# Логика калькулятора
from operations import OPERATIONS
from helpers import safe_eval

class CalculatorLogic:
    def __init__(self):
        self.last = ''

    def process(self, char, current):
        # Очистка
        if char == 'C':
            self.last = ''
            return '0'
        # Плюс-минус
        if char == '±':
            if current.startswith('-'):
                return current[1:]
            return '-' + current
        # Равно
        if char == '=':
            try:
                val = safe_eval(current)
                self.last = str(val)
                return self.last
            except Exception:
                return 'Ошибка'
        # Другие символы
        if char in OPERATIONS or char.isdigit() or char == '.':
            if current == '0' or current == 'Ошибка':
                return char
            return current + char
        return current