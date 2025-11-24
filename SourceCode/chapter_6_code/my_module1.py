# my_module1.py
"""
This module demonstrates the use of built-in module attributes.
"""
def example_function():
    return "This is a function in my_module."

if __name__ == "__main__":
    print(f"Module name: {__name__}")
    print(f"File location: {__file__}")
    print(f"Docstring: {__doc__}")
    print(f"Package: {__package__}")