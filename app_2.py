# Напишите функцию принимающую на вход только ключевые параметры(kwargs)
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def kwargs_to_dict(**kwargs):
    """Function returns a dictionary of kwargs key parameters"""
    result_dict = {}

    for key, value in kwargs.items():
        if hashable(value):
            result_dict[value] = key
        else:
            result_dict[str(value)] = key

    return result_dict


def hashable(obj):
    """Function checks the key for hashing"""
    try:
        hash(obj)
        return True
    except TypeError:
        return False


args_dict = kwargs_to_dict(a=33, b='world', c=[1, 2, 3])
print(args_dict)
