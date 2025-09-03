# create a class with a class attribute a: create an object from it and set 'a'
# directly using object.a = o, Does this change the class attribute.


class MyClass:
    a = 0

    def pri(self):
        print(self.a)



obj = MyClass()
obj.a = 23
obj.pri()
print(MyClass.a)