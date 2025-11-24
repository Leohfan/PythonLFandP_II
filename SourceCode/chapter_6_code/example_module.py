def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    # 只有在直接运行此模块时，以下代码才会执行
    print("This module is being run directly.")
    print(greet("World"))
else:
    print("This module has been imported.")