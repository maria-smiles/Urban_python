
def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

inner_function()


# Результат выполнения - ошибка "NameError: name 'inner_function' is not defined"
