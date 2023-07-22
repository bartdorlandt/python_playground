class NameDescriptor:
    # pass
    def __get__(self, instance, owner):
        return f"{instance.first} {instance.last}"


class Person:
    name = NameDescriptor()
    def __init__(self, first, last):
        self.first = first
        self.last = last

john = Person("John", "Doe")
print(john.name)
