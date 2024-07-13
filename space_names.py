# Пространство имен


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# Вызовем inner_function вне функции test_function и убедимся что имя внутренней
# функции неопределено в этой зоне видимости
inner_function()
