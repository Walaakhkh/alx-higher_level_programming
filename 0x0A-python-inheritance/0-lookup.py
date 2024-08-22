#!/usr/bin/python3
def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object whose attributes and methods are to be listed.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)


# Test with built-in types
print(lookup(int))       # Should list int methods and attributes
print(lookup(float))     # Should list float methods and attributes
print(lookup(list))      # Should list list methods and attributes


# Test with a class with a custom __dir__ method
class MyClass:
    def __dir__(self):
        return ["my_class", "is", "empty"]


print(lookup(MyClass()))  # Should list ["my_class", "is", "empty"]


# Test with a basic class
class MyClass:
    pass


print(lookup(MyClass))    # Should list default attributes and methods


# Test with a class with one attribute
class MyClass:
    one_attribute = 89


print(lookup(MyClass))    # Should include 'one_attribute'


# Test with a class with one method
class MyClass:
    def one_meth(self):
        pass


print(lookup(MyClass))    # Should include 'one_meth'
