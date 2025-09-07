from functools import wraps


def testDemo(func):
    @wraps(func)
    def wrapper(*args, **keywords):
        print("Before function run")
        result = func(*args, **keywords)
        return result
    return wrapper



@testDemo
def great(type):
    print("Hello from decorator call"+type)

great("Rose")



