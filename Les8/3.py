class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = float(input('Введите значение:'))
                self.my_list.append(val)
                print(f'Текущий список : {self.my_list} \n ')
                y_or_n = input(f'Продолжить ? Y/N ')

                if y_or_n == 'N' or y_or_n == 'n':
                    return f'Конечный список : {self.my_list}'
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Продолжить ? Y/N ')

                if y_or_n == 'N' or y_or_n == 'n':
                    return f'Конечный список : {self.my_list}'


try_except = Error(1)
print(try_except.my_input())
