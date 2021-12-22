"""
Хабибрахманова Валерия КИ21-16/1Б
вариант 9. Жирный и курсив
"""
import sys
from module_check import check_input
from module_font import bold, itallic


def main():
    """
    Основная программа
    """
    while True:
        print('1.Продолжить работу \n'
              '2.Выход из программы')
        menu = check_input('Введите номер пункта меню: ')
        if menu == 1:
            my_str = input('Введите вашу строку: ')
            k = 0
            j = 0
            for i in range(0, len(my_str), 1):
                if my_str[i] == '*':
                    k += 1
                else:
                    break
            for i in range(len(my_str)-1, -1, -1):
                if my_str[i] == '*':
                    j += 1
                else:
                    break
            k = k - abs(k-j)
            if k >= 2:
                ost = (k-2) % 2
                my_str = my_str[(k-ost-2):(len(my_str)-j+ost+2)]
            my_str_b = bold(my_str)
            if my_str_b == my_str:
                print(itallic(my_str))
            else:
                print(my_str_b)
        elif menu == 2:
            sys.exit()


if __name__ == '__main__':
    main()
