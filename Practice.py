Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
num1 = 5
num2 = 6
print(num1+num2)
11
name = (input())
maria
print ("Hello", name)
Hello maria
a = int (input())
10
b = int (input())
2
print(a+b, a-b, a*b, a/b, sep = "@")
12@8@20@5.0
name = input("Put your name: ")
Put your name: Maria
print(f"Hello, " {name}! Welcome to Python!)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
Print (f"Hello, {name}! Welcome to Python!")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Print (f"Hello, {name}! Welcome to Python!")
NameError: name 'Print' is not defined. Did you mean: 'print'?
print (f"Hello, {name}! Welcome to Python!")
Hello, Maria! Welcome to Python!
age = input("Put your age: ")
Put your age: 29
print(f"Hello, my name is {name}! I am {age} years old!")
Hello, my name is Maria! I am 29 years old!
date = int(input())
1
month = int(input())
2
year = int(input())
1996
print(date, month, year, sep="-")
1-2-1996
hour = int(input())
12
minutes = int(input())
49
seconds = int(input())
25
print(hour, minutes, seconds, sep=":")
12:49:25
name = (input())
maria
print(f"hello, {name}", end = "!")
hello, maria!
12:49:25
SyntaxError: illegal target for annotation
a = int(input())
b = int(input())
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'b = int(input())'
a = int(input())
7
b = int(input())
30
x = a*60
y = b*1
print(x+y)
450
450
450

length = float(input("Put the length: "))
Put the length: 15
width = float(input("Put the width: "))
Put the width: 20
perimeter = 2 * (length + width)
area = length + width
print(f"Perimeter: {perimeter}")
Perimeter: 70.0
print(f"Area: {area}")
Area: 35.0
Area: 35.0
length = int(input("Put the length: "))
Put the length: 289
width = int(input("Put the width: "))
Put the width: 98
perimeter = 2 * (length + width)
area = length * width
print(f"Perimeter: {perimeter}")
Perimeter: 774
area = lenght*width
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    area = lenght*width
NameError: name 'lenght' is not defined. Did you mean: 'length'?
>>> area = lenght * width
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    area = lenght * width
NameError: name 'lenght' is not defined. Did you mean: 'length'?
>>> print(f"The area is {area}")
The area is 28322
>>> S = int(inpur())
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    S = int(inpur())
NameError: name 'inpur' is not defined. Did you mean: 'input'?
>>> S = int(input())
s = S // 1000
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    S = int(input())
ValueError: invalid literal for int() with base 10: 's = S // 1000'
>>> S = int(input())
1500
>>> s = S // 1000
>>> print(s)
1
>>> n = int(input())
3
>>> k = int(input())
14
>>> s= k // n
>>> v = k % n
>>> print (s,v)
4 2
>>> rubels = float(input("Put amount in rubels: "))
Put amount in rubels: 500000
>>> exchange_rate = float(input("Put euro exchange rate: "))
Put euro exchange rate: 92.98
>>> euros = rubels / exchange_rate
>>> print(f"{rubels} RUB = {euros:.2f} USD")
500000.0 RUB = 5377.50 USD
>>> print(f"{rubels} RUB = {euros:.2f} EUR")
500000.0 RUB = 5377.50 EUR
>>> num1 = float(input("Первое число: "))
Первое число: 765.98
>>> num2 = float(input("Первое число: "))
Первое число: 87654,789
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    num2 = float(input("Первое число: "))
ValueError: could not convert string to float: '87654,789'
>>> num2 = float(input("The second num: "))
The second num: 72215.12
>>> num3 = float(input("The third num: "))
... The second num: 98251.09
SyntaxError: multiple statements found while compiling a single statement
>>> num3 = float(input("The third num: "))
... The third num: 98251.09
SyntaxError: multiple statements found while compiling a single statement
>>> num3 = float(input("The third num: "))
... The second num: 98251.5
SyntaxError: multiple statements found while compiling a single statement
>>> num3 = float(input("The third number: "))
The third number: 453.76
>>> avarage = (num1 + num2 + num3) //3
>>> print(f"The avarage number is {avarage}")
The avarage number is 24478.0
