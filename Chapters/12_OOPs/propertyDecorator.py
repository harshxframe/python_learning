class Student:
    def __init__(self):
        self._name = None  # 👈 internal variable

    @property
    def name(self):        # 👈 safe getter
        return self._name

    @name.setter
    def name(self, value):  # 👈 safe setter
        if len(value) < 3:
            print("Name too short!")
        else:
            self._name = value


stu = Student()
stu.name = "sh"

print(stu.name)
