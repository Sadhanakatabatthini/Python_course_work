Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "codegnan"
s
'codegnan'
type(s)
<class 'str'>
s = ''
s
''
a = 'python'
b = ' programming'
a+b
'python programming'
fname = 'sowmya'
lname = 'thummala'
fname+lname
'sowmyathummala'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
s = 'codegna'
s = 'codegnan'
s[0]
'c'
s[4]
'g'
s[1]
'o'
s[3]
'e'
s[2]
'd'
s[-1]
'n'
s[-3]
'n'
s[-6]
'd'
names = {'kalyani' , 'vishnupriya' , 'lakshmi' , 'mounasri' , 'lohitha' , 'usharani'}
names
{'kalyani', 'lohitha', 'lakshmi', 'vishnupriya', 'mounasri', 'usharani'}
names = {'kalyani', 'vishnupriya', 'lakshmi', 'mounasri', 'lohitha', 'usharani'}
names
{'kalyani', 'lohitha', 'lakshmi', 'vishnupriya', 'mounasri', 'usharani'}
names[8:9]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    names[8:9]
TypeError: 'set' object is not subscriptable
del names
n = 'kalyani usha sadhana'
n
'kalyani usha sadhana'
n[:7:]
'kalyani'
n[8:12:]
'usha'
n[13:20:]
'sadhana'
n[-1:-8:]
''
n[-1:-8:-1]
'anahdas'
n[::-1]
'anahdas ahsu inaylak'
n[-1:-9:1]
''
n
'kalyani usha sadhana'
kalyani in n
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    kalyani in n
NameError: name 'kalyani' is not defined
'kalyani' in n
True
'lohitha' not in n
True
'a' not in n
False
'usha' in n
True
len(n)
20
ord(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 6 found
ord('a')
97
ord('v')
118
chr(100)
'd'
chr(40)
'('
chr('40')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    chr('40')
TypeError: 'str' object cannot be interpreted as an integer
sorted(n)
[' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'd', 'h', 'h', 'i', 'k', 'l', 'n', 'n', 's', 's', 'u', 'y']
min(n)
' '
max(n)
'y'
s = 'python programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.capitalize()
'Python programming language'
s.swapcase()
'PYTHON PROGRAMMING LANGUAGE'
s.title()
'Python Programming Language'
s.center(50,'-') # making string at center
'-----------python programming language------------'
s.center(50,'.')
'...........python programming language............'
s.rjust(40,'.')
'.............python programming language'
s.ljust(40,'.')
'python programming language.............'
'123'.zfill(5)
'00123'
s.zfill(100)
'0000000000000000000000000000000000000000000000000000000000000000000000000python programming language'
'1234'.zfill(2)
'1234'
s
'python programming language'
s.find(python)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.find(python)
NameError: name 'python' is not defined
s.find('python')
0
s.find('g')
10
s.find('p)
       
SyntaxError: unterminated string literal (detected at line 1)
s.find('p')
       
0
s.rfind('g')
       
25
s.rfind('a')
       
24
s.find('z')
       
-1
s.index('p')
       
0
s.index('z') #this raises an error
       
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.index('z') #this raises an error
ValueError: substring not found
>>> s.rindex('g')
...        
25
>>> s.lindex('g')
...        
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.lindex('g')
AttributeError: 'str' object has no attribute 'lindex'. Did you mean: 'index'?
>>> s.count('a')
...        
3
>>> s.count('g')
...        
4
>>> s
...        
'python programming language'
>>> s.replace('o' , '1')
...        
'pyth1n pr1gramming language'
>>> s.replace('python','java')
...        
'java programming language'
>>> s.maketrans('aeiou' , '#@$&*')
...        
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.s.maketrans('aeiou' , '#@$&*'))
...        
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.translate(s.s.maketrans('aeiou' , '#@$&*'))
AttributeError: 'str' object has no attribute 's'
>>> s.translate(s.maketrans('aeiou' , '#@$&*'))
...        
'pyth&n pr&gr#mm$ng l#ng*#g@'
>>> text = "hello"
...        
>>> text.encode()
...        
b'hello'
>>> b'hello'.decode()
...        
'hello'
