Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Trimming methods
>>> s = '       Hello     world      '
>>> s.strip()
'Hello     world'
>>> s.rstrip()
'       Hello     world'
>>> s.lstrip()
'Hello     world      '
>>> s.replace(' ','')
'Helloworld'
>>> s = 'java-python-flask-mysql-fastapi-c'
>>> s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
>>> s.rsplit('-',2)
['java-python-flask-mysql', 'fastapi', 'c']
>>> l = '''python'''
>>> l = '''python
... java
... mysql
... flask
... '''
>>> l
'python\njava\nmysql\nflask\n'
>>> l.splitlines()
['python', 'java', 'mysql', 'flask']
>>> c = ['python', 'java', 'mysql', 'flask']
>>> ''.join(c)
'pythonjavamysqlflask'
>>> ' '.join(c)
'python java mysql flask'
>>> '@'.join(c)
'python@java@mysql@flask'
>>> '-'.join(('1','2','3'))
'1-2-3'
>>> '-'.join({'1','2','3'})
'2-3-1'
>>> a = "strings.py"
>>> a.partition('.')
('strings', '.', 'py')
>>> a.rpartition(',')
('', '', 'strings.py')
>>> a = 'strind.py'
>>> a.startswith('str')
True
>>> a.startswith('list')
False
a.startswith('.py')
False
a.endswith('.png')
False
'python.13'.islower()
True
'Python.13'.isupper()
False
"WERT".isupper()
True
"123asfg".isalpha()
False
"asdfghj".isalpha()
True
"1234567".isnum()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    "1234567".isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
123456.isnum()
SyntaxError: invalid syntax
"123456".isalnum()
True
'qwe1234'.isalnum()
True
'     '.isspace()
True
'    hello',isspace()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    '    hello',isspace()
NameError: name 'isspace' is not defined
'    hello'.isspace()
False
'Hel Wor'.istitle()
True
'HEL wor'istitle()
SyntaxError: invalid syntax
'HEL wor'.istitle()
False
'my_var'.isidentifier()
True
'my@var'.isidentifier()
False
False
False
'123456'.isdecimal()
True
'QWER2345'.isdecimal()
False
'12345'.isdigit()
True
'2345'.isnumeric()
True
