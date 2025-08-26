Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
a = int(input())
10
b = int(input())
7
print(a+b,a*b, sep+",")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a+b,a*b, sep+",")
NameError: name 'sep' is not defined. Did you mean: 'set'?
print(a+b,a*b, sep=",")
17,70
S = int(input())
2654
L = int(input())
245
F = int(input())
524
Print(S-L-F)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Print(S-L-F)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(S-L-F)
1885
a = int(input())
15
b = int(input())
8
>>> area = (a*b) / 2
>>> print(f"The area is equal {area}")
The area is equal 60.0
>>> print(f"To be\nor not\nto be")
To be
or not
to be
>>> print(f""Life is what happens\n\twhen\n\t\tyou are busy making other plans"\n\t\t\t\t\t\t\t\t\t\tJohn Lennon")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f"“Life is what happens\n\twhen\n\t\tyou’re busy making other plans”\n\t\t\t\t\t\t\t\t\t\tJohn Lennon.")
“Life is what happens
	when
		you’re busy making other plans”
										John Lennon.
>>> print(f"“Life is what happens\n\twhen\n\t\tyou’re busy making other plans”\n\t\t\t\t\t\t\t\tJohn Lennon.")
“Life is what happens
	when
		you’re busy making other plans”
								John Lennon.
>>> John Lennon.
SyntaxError: invalid syntax
>>> a = (input())
1
>>> b = (input())
5
>>> c = (input())
7
>>> print(a+b+c)
157
>>> num = input("Put the four digit number: ")
Put the four digit number: 1342
>>> a = int(number[0])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = int(number[0])
NameError: name 'number' is not defined
>>> a = int(num[0])
>>> b = int(num[1])
>>> c = int(num[2])
>>> d = int(num[3])
>>> result = a*c*b*d
>>> print(a, "*", b, "*", c, "*", d, "=", result)
1 * 3 * 4 * 2 = 24
>>> base = input("Put the base value: ")
Put the base value: 15
>>> height = input("Put the height value: ")
Put the height value: 9
>>> area = (base*result) // 2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    area = (base*result) // 2
TypeError: unsupported operand type(s) for //: 'str' and 'int'
>>> a = int(base)
>>> b = int(height)
>>> area = (a*b)//2
>>> print("The area of a triangle is ", area)
The area of a triangle is  67
>>> num = input("Put the four digit number: ")
Put the four digit number: 3671
>>> a = num[0]
>>> b = num[1]
>>> c = num[2]
>>> d = num[3]
>>> result = d+c+b+a
>>> print(result)
1763
