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


if __name__ == "__main__":
    print(get_str_length("dfgh"))

    print(concat_strings("asd", "fgh"))

    print(square_pow(3))

    print(sum_numbers(1, 2))

    print(divide_numbers(5, 2))
