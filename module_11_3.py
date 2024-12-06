from pprint import pprint
import inspect


def introspection_info(obj):
    try:
        print(f"Name of object:{obj.__name__}")
    except Exception:
        pass
    print(f"Type of object: {type(obj)}")
    print("Attributes and methods:")
    pprint(dir(obj))
    print(f"Check for attribute 1 with hasattr: {hasattr(obj, 'attribute_1')}")
    print(
        f"Trying to get an attribute with getattr:{getattr(obj, 'attribute_1', 
                                                             'No such attribute, have you even seen hasattr result?!' )}"
    )
    print(f"Checkig if it's a callable oject: {callable(obj)}")
    print(f"Checkig if it's a number: {isinstance(obj, int)}")
    pprint(f"Getting all members of the object: {inspect.getmembers(obj)}")
    print(f"Checkig if it's a module: {inspect.ismodule(obj)}")
    print(f"Checkig if it's a class: {inspect.isclass(obj)}")
    print(f"Checkig if it's a function: {inspect.isfunction(obj)}")
    print(f"Checkig if it's a built-in: {inspect.isbuiltin(obj)}")


class RandomObject:
    def __init__(self):
        self.attribute_1 = 1000

    def hello(self):
        print("Hello, world!")

    def blob(self):
        print("Blob!")

    def divide_by_2(self):
        self.attribute_1 = self.attribute_1 // 2


number_info = introspection_info(42)
object = RandomObject()
object_info = introspection_info(object)

