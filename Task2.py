"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class My_Exception():

    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        self.run_div()

    def run_div(self):
        tmp = False
        try:
            result = self.param_1 / self.param_2
            tmp = True
            print(result)
        except ZeroDivisionError:
            print("Деление на ноль недопустимо")
        finally:
            if not tmp:
                usr_input = float(input('Geben Sie bitte eine Zahl ein: '))
                self.param_2 = usr_input
                self.run_div()


my = My_Exception(20, 0)