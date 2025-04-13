import colorama
import inspect

attributes = dir(colorama)

important_attributes = []
important_methods = []

for attribute_name in attributes:
    attribute = getattr(colorama, attribute_name)
    if not attribute_name.startswith('_'):  
        if inspect.ismodule(attribute):
            print(f"Модуль: {attribute_name}")
        elif inspect.isclass(attribute):
            print(f"Класс: {attribute_name}")
        elif inspect.isfunction(attribute):
            print(f"Функция: {attribute_name}")
            important_methods.append(attribute_name)
        else:
            print(f"Атрибут: {attribute_name}")
            important_attributes.append(attribute_name)

print("\nДокументация для важных методов:")
for method_name in important_methods:
    method = getattr(colorama, method_name)
    print(f"\nМетод: {method_name}")
    print(inspect.getdoc(method))