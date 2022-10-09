# #                                              -- LEARNING PYTHON
# -dir
# -help
# ctrl+alt+l
# ctrl+/
# ctrl+.
# ctrl+d  --  ctrl+y
# shift+f6
# if __name__ == '__main__':

# # 1) - PRINT
# print("print number", 5+5, max(7, 10, -3), end=" ")
# print("print number", 5*5, min(7, 10, -3), sep="|")

# # 2) - VAR
# number = 10  # int
# boolean = True  # bool
# digit = 4.5  # float
# word = "Hello"  # string
# print(number, digit, word, boolean)
# print(word + str(digit + number))
# del number
#
# a = int(input("Insert first number "))
# b = int(input("Insert second number "))
# a += 5
# print("Sum:", a + b)
# print("Dif:", a - b)
# print("Prod:", a * b)
# print("Div:", a / b)
# print("Div int:", a // b)
# print("Div round+:", round(a / b))
# print("Pow:", pow(a, b))
#
# word = "Shit"
# print(word*2)

# # 3) - IF-ELSE
# user_age = int(input("Insert your age: "))
# user_Mood = str(input("Are you happy? "))
# count = 0
# user_mood = False

# 1.
# if user_Mood == "yes":
#    user_mood = True
# if user_age >= 20:
#     print("You are not a teen:(", end=" ")
#     count -= 1
# else:
#     print("You're a teen!", end=" ")
#     count += 1
# if user_mood:
#     if count > 0:
#         print("And you are happy!")
#     else:
#         print("But you are happy! You're so cool, man")
# else:
#     if count > 0:
#         print("But you're unhappy...Weakling! It won't be better, dear")
#     else:
#         print("And you're unhappy:( Can understand, homie!")

# 2.
# if user_Mood == "yes":
#    user_mood = True
# if user_age >= 20 and user_mood:
#     print("You're not a teen, but you're still happy!")
# elif user_age >= 20 and not user_mood:
#     print("You're not a teen, and you're unhappy :(")
# elif user_mood:
#     print("You're a teen, and you're happy")
# else:
#     print("You're a teen, but you're unhappy...Are you kidding???")
#
# data = input("Insert the number: ")
# num = 5 if data == "five" else 0  # - ternary operator
# print(num)

# # 4) - FOR-WHILE
# for i in range(1, 6, 2):  # [1;6), где шаг = 2
#     print(i, end=" ")

# i = 5
# while i < 15:
#     print(i)
#     i += 2

# 1. FOR - count the number of repetitions of all the text's unique characters in a same text
# count = 0
# n = 0
# text = input("Insert your data: ")
# Mass = []
# for i in text:
#     for elem in Mass:
#         if i == elem:
#             n = 1
#     if n == 1:
#         continue  # transition to the next iteration, BREAK - cycle completion
#     for j in text:
#         if i == j:
#             count += 1
#     Mass.append(i)
#     print("the symbol \"", i, "\" appears", count, "times")
#     count = 0

# 2. FOR - is there the symbol in a text?
# sym = input("Insert your symbol: ")
# text = input("Insert your text: ")
# mark = None
# for elem in text:
#     if elem == sym:
#         mark = True
#         break
# else:
#     mark = False
# print(mark)

# # 5) - LISTS - can use negative indices - [-2]
# print("FIRST")
# first = [1, 2, 3, True, "Hi", 1.2]
# print(first)
# first[3] = 6
# print(first, first[-1])
#
# # methods
# second = [7, 5, 6, True]
# first.append(second)
# print(first, "- adding an element(SECOND) to the end")
# first.insert(6, False)
# print(first, "- inserting an element at the position(6), with offset")
# first.extend(["No", "No", "No"])
# print(first, "- adding elements to the end")
#
# print("SECOND")
# second.sort()
# print(second, "- sort ascending")
# second.remove(True)
# print(second, "- deleting by value")
# second.pop(0)
# print(second, "- deleting by index OR deleting the last element - pop()")
# print(second.count(6), "- number of repetitions of an element(6)")
# print(len(second), "- list power")
# first.clear()
# second.clear()
#
# print("THIRD")
# print("enter list items or \"STOP\"")
# third = []
# data = 0
# while data != "Stop":
#     data = input()
#     third.append(data)
# print("Your list: ", third)

# # 6) - STRINGS
# # ABOUT STRINGS
# # string = symbol list
# # can use list methods for string and special string methods
#
# # EXAMPLES OF STRINGS/METHODS
# string = input("Enter your string: ")
# print("Length: ", len(string))
# print("Upper case: ", string.upper())
# print("Lower case: ", string.lower())
# print("Capitalize: ", string.capitalize())
# substring = input("Enter your substring: ")
# print("Substring search: ", string.find(substring))
# string2 = "Day, Month, Year"
# print("String2: ", string2)
# split_string2 = string2.split(',')
# print("Split by symbol(,): ", split_string2)
# string2 = ','.join(split_string2)
# print("Join: ", string2)
# print("Slice[0:4:2]: ", string2[0:4:2])  # 0 - first element, 4 - last element, 2 - step
# print("Slice[::-1]: ", string2[::-1])

# # 7) - Tuples
# # ABOUT TUPLES
# # tuple = immutable list
# # tuple weight < list weight
#
# # EXAMPLES OF TUPLES/ METHODS
# data = (2, True, "Can")  # (2, True, "Can") == 2, True, "Can" == tuple # (2,) == 2, == tuple != (2)
# print("Tuple:", data)
# for i in range(0, len(data)):
#     print("Elem №", i, "=", data[i])
# for el in data:
#     print(el)
#
# List = [0, 1, 3]
# print("List: ", List)
# Tuple = tuple(List)  # conversion to tuple
# print("List to tuple: ", Tuple)
# String = 'Hi, John!'
# print("String: ", String)
# Tuple = tuple(String)
# print("String to tuple: ", Tuple)

# # 8) - DICT
# # ABOUT DICT
# # dict == {key: data}, key != list
# # dict == dict(key=data), key == string(only)
#
# # EXAMPLES OF DICTS/METHODS
# student = {"name": "Alex", "studying": True, "year": 2, "achievement": "excellent"}
# print("Dic: ", student.items())
# print("Name:", student["name"])  # student["name"] == student.get("name")
# print("Year:", student.get("year"))
# for key, data in student.items():
#     print(key, "-", data)
#
# print("\nOnly keys: ", student.keys())
# print("Only values: ", student.values())
#
# print("\nDeleting")
# student.pop("name")
# print("by key: ", student)
# student.popitem()
# print("last item: ", student)
# student.clear()
# print("all: ", student)
#
# # EXAMPLE OF NEST
# print("\nNesting")
# students = {
#     'A': {
#         'name': ('Alis', 'Carla', 'Mark'),
#         'date': ('11.10.02', '13.02.02', '05.12.02'),
#         'marks': {
#             'maths': {
#                 'Alis': 5,
#                 'Carla': 4,
#                 'Mark': 5
#             },
#             'physics': {
#                 'Alis': 2,
#                 'Carla': 5,
#                 'Mark': 3
#             }
#         }
#     },
#     'B': {
#         'name': ('Kenny', 'Token', 'Stan'),
#         'date': ('11.10.02', '13.02.02', '05.12.02'),
#         'marks': {
#             'maths': {
#                 'Kenny': 5,
#                 'Token': 4,
#                 'Stan': 5
#             },
#             'physics': {
#                 'Kenny': 2,
#                 'Token': 5,
#                 'Stan': 3
#             }
#         }
#     }
# }
# print(students.items())
# print("Grade B, maths: ", students['B']['marks']['maths'])

# # 9) - SET-FROZENSET
# # ABOUT SETS
# # set == list, where elements are not repeated + in random order
# # set('hello') == {'h','l','l','o'} == set
# # can't access by index!
#
# # EXAMPLES OF SETS/METHODS
# Set = {5, 2, 3, 4, 2}
# print(Set)
# Set.add(1)  # (only one element)  TRUE == 1, FALSE == 0  - so TRUE/FALSE wouldn't be added if you have 1/0 in your set
# print(Set)
# Set.update([4, 'hope', False, True])  # (NOT only one element)
# print(Set)
# Set.remove(True)  # removing one element by value
# print(Set)
# Set.pop()  # removing first element
# print(Set)
# Set.clear()  # removing all elements
# print(Set)
#
# # fast removing repeated elements from the list
# List = [1, 4, 4, 5, 5, True, 7, 9, 0, 0, False, 'hi']
# List = set(List)
# print(List)
#
# # ABOUT FROZENSET
# # frozenset == set + tuple == set, which can`t be updated
# List = [1, 4, 4, 5, 5, True, 7, 9, 0, 0, False, 'hi']
# print(List)
# FrozenSet = frozenset(List)  # frozenset(List) == frozenset([1, 4, 4, 5, 5, True, 7, 9, 0, 0, False, 'hi'])
# print(FrozenSet)

# # 10) - FUNCTION
# # function without arguments
# def fun():  # function definition
#     pass
#
#
# fun()  # function call
#
#
# # function with arguments
# def nums(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# result = {'even': 0, 'odd': 0}
# stop_word = input('Enter your stop word: ')
# mark = None
# print('Ok, now enter your numbers')
# t = input()
# while t != stop_word:
#     mark = nums(int(t))
#     if mark:
#         t = result.get('even')
#         result.update({'even': t + 1})
#     else:
#         t = result.get('odd')
#         result.update({'odd': t + 1})
#     t = input()
# print(result.items())
#
#
# # anonymous function - lambda arguments : expression
# f = lambda x, y: x * y
# print(f(3, 5))

# # 11) - FILES
# # file = open(name, mode)  --  file.close()  --  as an everywhere
# file = open('text.txt', 'a')
# data = input('Enter your data: ')
# file.write(data+'\n')
# file.close()
#
# file = open('text.txt', 'r')
# # read line by line
# for line in file:
#     print(line, end='')
# # read everything
# print(file.read())
# # file wasn't closed, the pointer is at the end of the file after the first read - remember that
# file.close()
#
# # example of deleting
# # importing the os Library
# import os
# # checking if file exist or not
# if (os.path.isfile("text.txt")):
#     os.remove("text.txt")
#     print("File Deleted successfully")
# else:
#     print("File does not exist")
#
# # ABOUT explicit pointer
# # file_name.tell() - get pointer position
# # file_name.seek(offset, [from]) - changes the current file position
# # OFFSET - the number of bytes to be moved. FROM - the reference position from where the bytes are to be moved


# # 12) - TRY-FINALLY - exception handler
# # 1. error + error
# try:
#     print('10'+10)
#     print(1/0)
# except (TypeError, ZeroDivisionError):
#     print('Invalid input')
#
# # 2. except + except
# try:
#     print('1'+1)
#     print(sum)
#     print(1/0)
# except NameError:
#     print("Sum doesn't exist")
# except ZeroDivisionError:
#     print("Division by zero")
# except:
#     print("Something is wrong...")
#
# # 3. finally
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Division by zero")
# finally:
#     print("Finally - works anyway")
#
# # 4. raise
# raise ValueError('Invalid value')  # - throws a specific exception (with your comment)
# try:
#     print('1'+1)
# except:
#     raise  # - throws the exception that happened
#
# # 5. assert
# # assert condition, message - condition check (with your comment)
#
# # 6. example
# try:
#     x = 5/1
#     x = int(input('Enter: '))
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ValueError:
#     print('ValueError')
# else:
#     print('Else')
# finally:
#     print('Finally')

# # 13) - WITH-AS - context manager
# # ABOUT CONTEXT MANAGER - https://peps.python.org/pep-0343/
# # statement WITH adds to make it possible to factor out standard uses of TRY-FINALLY statements
# # context managers provide ENTER and EXIT methods that are invoked on entry to and exit from the body of the WITH statement
# # WITH-AS guarantees the execution of the final code in any case
# # "with" expression ["as" target] ("," expression ["as" target])* ":"
# #     suite
# # EXAMPLE (file)
# # 1
# try:
#     file = open('test.txt', 'w+')
#     file.write('r')
#     print('File is open')
#     file.seek(0)
#     print('text: ', file.read())
# except FileNotFoundError:
#     print('There is no file with that name')
# except:
#     print('Shit...')
# finally:
#     file.close()
#     print('Closed')
# # 2
# try:
#     with open('text.txt', 'w+', encoding='utf-8') as file:
#         file.write("YEAH")
#         file.seek(0)
#         print(file.read())
# except:
#     print('There is a problem...')
#
# import os
# if (os.path.isfile("test.txt")):
#     os.remove("test.txt")
#     print("File Deleted successfully")
# else:
#     print("File does not exist")

# # 14) - MODULES
# # ABOUT MODULES - https://docs.python.org/3/tutorial/modules.html  -  https://pythonworld.ru/moduli
# # module - a separate file with code that can be reused in other programs
#
# # EXAMPLES
# # 1. built-in
# import time
# time.sleep(1)
# print('time')
# import datetime as dt
# print('datetime: ', dt.datetime.now())
# import sys, os, platform
# print('sys: ', sys.path)
# print('os: ', os.name)
# print('platform: ', platform.system())
# # 2. partial import - FROM
# from math import sqrt as s, ceil
# print('math.sqrt/ceil: ', ceil(s(125)))
# # 3. module creation (my_module.py)
# import my_module as my
# print(my.actor)
# f = open('text.txt', 'w')
# f.close()
# print(my.del_file(f.name))
# # 4. install - https://pypi.org/
# import cowsay
# cowsay.cow("I don't recommend installing libraries through the terminal")

# # TYPE ANNOTATIONS - you should use it!
# # 1.
# name: str = 'Tommy'
# age: int = 24
# height_in_meters: float = 1.7
# colleagues: list[str] = ['Alicia', 'John']  # otherwise in earlier versions
#
# def calc(a: int, b: int) -> int:
#     return a + b
#
# # 2. special types: Union = two, Optional = None + Union, Any, Literal, TypedDict, NoReturn = void(C++), Final = no redefine
# from typing import Union, Optional, Any
#
#
# def calc(a: Optional[int, float], b: Union[int, float]) -> Any:
#     return a + b

# # 15) - OOP-1
# from typing import NoReturn
#
#
# class Cat:
#     class_name = 'Cat'  # static attribute
#
#     def data_set(self, breed: str, age: int, wool: bool) -> NoReturn:
#         self.breed = breed
#         self.age = age
#         self.wool = wool
#
#     def output(self) -> NoReturn:
#         print(Cat.class_name)
#         print('Breed -', self.breed)
#         print('Age -', self.age)
#         print('Wool -', self.wool)
#
#
# Tom = Cat()  # default constructor / Python has only one constructor / constructor Python != constructor C++ / __new__ - constructor, __init__ - initializer
# Tom.breed = 'asian'
# Tom.wool = True
# Tom.age = 5
# Mouse = Cat()
# Mouse.data_set('himalayan', 4, False)
# Mouse.output()
# Tom.output()
#
# from math import sqrt
#
#
# # can refer to the methods declared below
# class Point:
#     InstancesCount = 0  # static attribute
#
#     def __init__(self, x: float = 0, y: float = 0) -> NoReturn:  # initializer
#         self.x = x
#         self.y = y
#         Point.InstancesCount = Point.InstancesCount + 1
#
#     def data_set(self, x: float, y: float) -> NoReturn:
#         self.x = x
#         self.y = y
#
#     def output(self, name: str) -> NoReturn:
#         print(name, ':  X =', self.x, 'Y =', self.y)
#
#     def seg_len(self, p2) -> float:
#         length = sqrt((pow((p2.x - self.x), 2)) + (pow((p2.y - self.y), 2)))
#         return length
#
#     def area_coordinates(self, p2, p3) -> float:  # triangle area by vertex coordinates
#         t1 = (p2.x - self.x) * (p3.y - self.y)
#         t2 = (p3.x - self.x) * (p2.y - self.y)
#         s = (abs(t1 - t2)) / 2
#         return s
#
#     def area_heron(self, p2, p3) -> float:  # triangle area according to Heron's formula
#         ab = self.seg_len(p2)
#         bc = p2.seg_len(p3)
#         ac = self.seg_len(p3)
#         p = (ab + bc + ac) / 2
#         s = sqrt(p * (p - ab) * (p - bc) * (p - ac))
#         return s
#
#     def area(self, p2, p3) -> NoReturn:
#         first = self.area_coordinates(p2, p3)
#         second = self.area_heron(p2, p3)
#         print('Heron\'s formula: ', second)
#         print('Vertex coordinates: ', first)
#
#
# a = Point(4, 3)
# b = Point()
# c = Point(0, 1)
# a.output('a')
# b.output('b')
# c.output('c')
# print('Amount of points:', Point.InstancesCount)
# a.area(b, c)

# # 16) - OOP-2-Encapsulation
# Encapsulation in python doesn't involve hiding data - all data is available for viewing and changing
# Python doesn't take tools away from the user, it warns them

# Инкапсуляция:
# 1. сбор данных и методов для работы с ними в одно место(класс)
# 2. предоставление публичного интерфейса(API) для работы с ними

# В питоне применяется нижнее подчеркивание _ для пометки внутренней реализации,
# то есть атрибутов не относящихся к публичному интерфейсу.

# Одно подчеркивание (protected) - это всего лишь сигнал,
# интерпретатор относится к таким атрибутам как к обычным.

# Два подчеркивания (private) - включает механизм подмены имени Name Mangling,
# который предназначен не для сокрытия данных.

