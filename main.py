def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = obj.__module__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'num_attributes': len(attributes),
        'num_methods': len(methods)
    }

    return info

class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        return f"The {self.model} is driving."

# Тестирование функции
car_object = Car("Toyota")
car_info = introspection_info(car_object)

print("Introspection of Car object:")
print(car_info)
