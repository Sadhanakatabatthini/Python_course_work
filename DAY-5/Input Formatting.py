Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#input formatting
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("enter the value: ")
enter the value: 123445
a
'123445'
marks = input("enter the marks: ")
enter the marks: 89
marks
'89'
marks = int(input("enter the marks: "))
enter the marks: 89
marks
89
price = float(input("enter the price: "))
enter the price: 123.4
price
123.4
cgpa = float(input("enter cgpa: "))
enter cgpa: 8.9
cgpa
8.9
# Splitting strings
names.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names = input()
sadhana vishnu laxmi
names
'sadhana vishnu laxmi'
names.split()
['sadhana', 'vishnu', 'laxmi']
names.split(',')
['sadhana vishnu laxmi']
courses = 'python-java-c++-flask
SyntaxError: unterminated string literal (detected at line 1)
courses = 'python-java-c++-flask'
courses
'python-java-c++-flask'
courses.split()
['python-java-c++-flask']
courses.split(',')
['python-java-c++-flask']
courses.split('-')
['python', 'java', 'c++', 'flask']
names = input("enter names: ").split
enter names: sadhana vishnu laxmi
names
<built-in method split of str object at 0x00000219DB9ABA30>
names = input("enter names: ").split())
SyntaxError: unmatched ')'
names = input("enter names: ").split()
enter names: sadhana vishnu laxmi
names
['sadhana', 'vishnu', 'laxmi']
names = tuple(input("enter names: ").split())
enter names: sadhana vishnu laxmi
names
('sadhana', 'vishnu', 'laxmi')
names = set(input("enter names: ").split())
enter names: sadhana vishnu laxmi
names
{'laxmi', 'vishnu', 'sadhana'}
names = tuple(input("enter names: ").split())
enter names: sadhana, vishnu, laxmi
names
('sadhana,', 'vishnu,', 'laxmi')
names = tuple(input("enter names: ").split(','))
enter names: sadhana, vishnu, laxmi
names
('sadhana', ' vishnu', ' laxmi')
marks = input().split()
12 34 45 67 
marks
['12', '34', '45', '67']
map
<class 'map'>
map(int,marks)
<map object at 0x00000219DB99A1D0>
list(map(map(int,marks))
     marks
     
SyntaxError: '(' was never closed
list(map(map(int,marks)))
     
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list(map(map(int,marks)))
TypeError: map() must have at least two arguments.
list(map(int,marks))
     
[12, 34, 45, 67]
marks = list(map(int,input("Enter the marks: ").split()))
     
Enter the marks: 12 45 98
marks
     
[12, 45, 98]
marks = tuple(map(int,input("Enter the marks: ").split()))
     
Enter the marks: 12 45 567
marks
     
(12, 45, 567)
marks = set(map(int,input("Enter the marks: ").split()))
     
Enter the marks: 134 567 2345
marks
     
{2345, 134, 567}
marks = set(map(float,input("Enter the marks: ").split()))
     
Enter the marks: 12.3 1.3 12.5
marks
     
{1.3, 12.3, 12.5}
a , b = [1,2]
     
a
     
1
b
     
2
a,b,c=(1,12.3,"str")
     
a
     
1
b
...      
12.3
>>> c
...      
'str'
>>> email,password = input("enter email and password: ").split()
...      
enter email and password: sadha@gmail.com 234456
>>> email
...      
'sadha@gmail.com'
>>> passwors
...      
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    passwors
NameError: name 'passwors' is not defined. Did you mean: 'password'?
>>> password
...      
'234456'
>>> name,marks = input("enter the name and marks: ").split()
...      
enter the name and marks: raj 78
>>> name
...      
'raj'
>>> marks
...      
'78'
>>> int(marks)
...      
78
>>> status = eval(input())
...      
status
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'status' is not defined
status = input()
     
True
status = eval(input())
     
status
status
     
'True'
type(status)
     
<class 'str'>
status = eval(input())
     
True
type(status)
     
<class 'bool'>
status = eval(input())
     
2+3j
status
     
(2+3j)
type(status)
     
<class 'complex'>
status = eval(input())
     
(1,2,3,4)
status
     
(1, 2, 3, 4)
type(status)
     
<class 'tuple'>
