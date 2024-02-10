"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: int) -> [int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [arg ** 2 for arg in args]


# filter types
ODD = "odd"  # нечетный
EVEN = "even"  # четный
PRIME = "prime"  # простой


def filter_odd_numbers(num: int) -> bool:
    return num % 2


def filter_even_numbers(num: int) -> bool:
    return not num % 2


def filter_prime_numbers(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True


def filter_numbers(int_list: [int], filter_type: str) -> [int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type not in [ODD, EVEN, PRIME]:
        error = f"Указан не верный тип фильтра {filter_type}. Фильтр может принимать одно из значений ({ODD}, {EVEN}, {PRIME})"
        raise Exception(error)
    f = []
    if filter_type == ODD:
        f = filter(filter_odd_numbers, int_list)
    elif filter_type == EVEN:
        f = filter(filter_even_numbers, int_list)
    elif filter_type == PRIME:
        f = filter(filter_prime_numbers, int_list)

    return list(f)

if __name__ == '__main__':
    t = filter_numbers([1, 2, 3], ODD)
    print (t)
