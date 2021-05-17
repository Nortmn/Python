class MyZeroDivisionError(Exception):
    text = "Деление на ноль!!!"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDivisionError

        return Number(float(self) / float(other))


while True:
    try:
        dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
        print(dividend / divider)
    except MyZeroDivisionError as d:
        print(d)
    except ValueError as d:
        print(d)
        break

# class DivisionByNull:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return divider / denominator
#         except:
#             return f"Деление на ноль недопустимо"
#
#
# div = DivisionByNull(10, 10)
# print(DivisionByNull.divide_by_null(10, 0))
# print(DivisionByNull.divide_by_null(10, 0.1))
# print(div.divide_by_null(10, 0))
# print(div.divide_by_null(10, 5))
