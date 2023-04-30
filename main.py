def merge_dicts(a: dict, b: dict):
    return {**a, **b}


def list_compr(a: list):
    return [elem for sublist in a for elem in sublist]


def repeat_func(a: str):
    print(a)
    return repeat_func
    # use: repeat_func('A')('B')('C')


def bool_check(a: bool, b: bool, c: bool, d: bool):
    reqs = [a, b, c, d]
    return all(reqs), any(reqs)


def list_check(a: int, b: int, c: int):
    li = [a, b, c]
    return any(n > 0 for n in li), all(n > 0 for n in li)


def strings():
    import string
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.punctuation)
    print(string.printable)
    return 0


# from python 3.10
def union(a: int):
    var: int | None = a
    print(type(int | None))
    return var


def random_from_list(a: list):
    import random
    return random.choice(a)


def randoms_from_list(a: list):
    import random
    return random.choices(a, k=3)


def copy(a: list):
    from copy import deepcopy
    return deepcopy(a)


def zipp(a: list, b: list):
    return [(c, d) for c, d in zip(a, b)]


def stand_text(a: str):
    return a.casefold()


def lam(a: int, b: int):
    return lambda x: a * x + b


def dic_item(a: dict):
    return a.get('X', 'Not found')


# final var
from typing import Final
VAR: Final[bool] = False


def hide_input():
    import pwinput as pin
    password = pin.pwinput('Enter password: ', '*')
    print('Password: ', password)
    return


def mult_check(a: int, b: int, c: int):
    return a == b == c


def unique(a: list):
    b = {el for el in a}
    return b


def func1():
    ...


def func2():
    ...


def func3(a: bool):
    return func1() if a else func2()