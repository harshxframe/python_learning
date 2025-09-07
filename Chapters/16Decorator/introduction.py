# Suppose we have multiple function and every function does separate jobs
from functools import wraps


# e.g

def testDemo(func):
    @wraps(func)
    def wrapper():
        print("Before function run")
        func()
        print("After function runs")
    return wrapper


@testDemo
def great():
    print("Hello from decorator call")


great()

print(great.__name__)