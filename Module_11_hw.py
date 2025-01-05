import inspect

class AClass:

    def __init__(self):
        self.attribute = 30

    def a_class_method(self, value):
        self.attribute = value
        print(self.attribute)

def introspection_info(obj):
    print(f'Тип объекта: {type(obj)}')
    print(f'Методы и атрибуты объекта: {dir(obj)}')
    print(f'Модуль, которому принадлежит объект: {inspect.getmodule(obj)}')

an_object = AClass()
info = introspection_info(an_object)
print(info)