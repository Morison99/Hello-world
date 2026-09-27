# from abc import ABC, abstractmethod


# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):
#     def sound(self):
#         return "woof!"


# dog = Dog()
# print(dog.sound())


def even_numbers():
    for i in range(0, 11, 2):
        yield i


evens = even_numbers()

# for number in evens:
#     print(number)
print(25*"*")
while True:
    try:
        print(next(evens))
    except StopIteration:
        print("StopIterration")
        break
# print(next(evens))
# print(next(evens))
