"""
Модуль проверки входного значения
"""


def check_input(input_message):
    """
    Принимает строку, возвращает число, если данные корректны
    :param input_message: Сообщение для вывода на экран при считывании
    :return: Число типа integer
    """
    while not ((number := input(input_message)) and number.isdigit()):
        print("Данные некорректны, повторите попытку и введите число")
    return int(number)
