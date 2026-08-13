Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#typeconversions
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f=1.2
int(f)
1
complex(f)
(1.2+0j)
str(f)
'1.2'
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
c=1+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(c)
True
str(c)
'(1+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s='codegnan'
i='1234'
int(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(i)
1234
float(i)
1234.0
bool(s)
True
bool(i)
True
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
list(i)
['1', '2', '3', '4']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(i)
{'3', '2', '4', '1'}
set(s)
{'c', 'a', 'o', 'g', 'd', 'e', 'n'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(i)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict(i)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l = [1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
>>> str(l)
'[1, 2, 3, 4]'
>>> bool(l)
True
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> t=(1,2,3,'v')
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(t)
"(1, 2, 3, 'v')"
>>> bool(t)
True
>>> list(t)
[1, 2, 3, 'v']
>>> set(t)
{1, 2, 3, 'v'}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
