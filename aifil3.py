# coding=utf-8
"""
Напишите простую реализацию функции для разбора параметров командной строки (getopt).
Полагаем, что нам требуется структура данных, содержащая заранее известный допустимый набор параметров различного типа -
строки, целые, числа с плавающей точкой и т. д., а также признак, является ли этот параметр обязательным.

Полагаем, что параметры могут передаваться только в "длинном" формате с обязательным "--" перед именем параметра
(то есть "--my-option-name my-option-val", "--my-option-name=my-option-val", "--my-boolean-option").
Параметров может быть несколько.

Функция должна обязательно уметь обрабатывать параметр "--help" (если он указан в списке параметров при вызове функции),
выводящий пример использования (необязательные параметры должны выводиться в квадратных скобках).
"""


import sys

PARAMS = {
    '--string': False,  # Если True, то параметр обязательный
    '--integer': True,
    '--float': True,
}


def help_output(filename):
    print 'Options:'
    msg = ' '
    for key, required in PARAMS.items():
        if required:
            msg += key + ' '
            print key + ' is required parameter'
        else:
            msg += '[{}] '.format(key)
            print key + ' is optional parameter'

    return '\nUsage: ' + filename + msg


def split_params_with_values(p):
    """
    Возвращает dict с приведенными типами переданных параметров.
    Параметры без присвоенных значений игнорируются.
    """
    d = {}
    for item in p:
        key = item.split('=')[0]
        if item.split('=')[1:]:  # Если переданный параметр имеет значение
            value = item.split('=')[1:][0]
            if key == '--string':
                d[key] = value
            if key == '--integer':
                try:
                    d[key] = int(value)
                except ValueError:
                    print 'Invalid value for --integer parameter!'
                    sys.exit(2)
            if key == '--float':
                try:
                    d[key] = float(value)
                except ValueError:
                    print 'Invalid value for --float parameter!'
                    sys.exit(2)
    return d


def getopt():
    """
    Проверяет переданные параметры и возвращает dict с приведенными типами переданных параметров,
    если не было ошибок при парсинге параметров.

    Если строка вызова содержит "--help" либо не содержит параметров - показывается справка.
    """
    if len(sys.argv) == 1 or '--help' in sys.argv:
        return help_output(sys.argv[0])

    else:
        splited_params = split_params_with_values(sys.argv[1:])

        for param in splited_params.keys():
            if param not in PARAMS.keys():
                print '{} unknown parameter provided!'.format(param)
                sys.exit(2)

        for param, required in PARAMS.items():
            if required and param not in splited_params.keys():
                print '{} required parameter is not provided!'.format(param)
                sys.exit(2)

        return splited_params


if __name__ == '__main__':
    print getopt()
