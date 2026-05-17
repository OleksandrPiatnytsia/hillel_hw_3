# 1.1 Напишіть функцію, яка приймає рядок і повертає його довжину.
def get_str_length(inc_string: str) -> int:
    return len(inc_string)


# 1.2 Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок
def concat_strings(string1: str, string2: str) -> str:
    return string1 + string2


# 2.1 Реалізуйте функцію, яка приймає число і повертає його квадрат.
def square_pow(x: int) -> int:
    return x**2


# 2.2 Створіть функцію, яка приймає два числа і повертає їхню суму.
def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2


# 2.3 Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає цілу частину і залишок
def divide_numbers(num1: int, num2: int) -> tuple[int, int]:
    return num1 // num2, num1 % num2


# 3.1 Напишіть функцію для обчислення середнього значення списку чисел.
def mean(digits: list[int]) -> float:

    return sum(digits) / len(digits)


# 3.2 Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків
def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    return list(set(list1) & set(list2))


# 4.1 Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
def get_dict_keys(_dict: dict[str, int]) -> None:
    for k in _dict.keys():
        print(k)


# 4.2 Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників
def dict_union(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    return dict1 | dict2


if __name__ == "__main__":
    print(get_str_length("dfgh"))

    print(concat_strings("asd", "fgh"))

    print(square_pow(3))

    print(sum_numbers(1, 2))

    print(divide_numbers(5, 2))

    print(concat_strings("asd", "fgh"))

    print(mean([1, 2, 3]))

    print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6]))

    get_dict_keys({"key1": 1, "key2": 2})

    print(dict_union({"key1": 1, "key2": 2}, {"key3": 3, "key4": 4, "key1": 5}))
