Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Dictionaries
# mutable , ordered , heterogeneous , dynamic
d = { }
type(d)
<class 'dict'>
d = {1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d = {}
d[1] = 1
d[12.3] = 1
d['str']=1
d[(1,2,3)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: unhashable type: 'list'
#list can be a key
d[{1,2,3}]=1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[{1,2,3}]=1
TypeError: unhashable type: 'set'
#set also
d[{1:2,2:3}]=1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[{1:2,2:3}]=1
TypeError: unhashable type: 'dict'
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
d[False]=1
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=2+3j
d[5]=True
d[6]=[1,2,3]
d[7]=(1,2,3)
d[8]={1,2,3}
d[9]=frozenset({1,2,3})
d[10]={1:1,2:2}
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
#values can be anything
d={}
d[1]=2
d
{1: 2}
d[1]=3 # key values are unique
d
{1: 3}
#we have only membership operation
data ={'name:'dinesh', 'course':'pfs','batch':65}
       
SyntaxError: unterminated string literal (detected at line 1)
data ={'name':'dinesh', 'course':'pfs','batch':65}
       
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65}
'dinesh in data
       
SyntaxError: unterminated string literal (detected at line 1)
'dinesh' in data
       
False
65 in data
       
False
'course' in data
       
True
data['name']
       
'dinesh'
data['batch']
       
65
data['age']
       
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('name')
       
'dinesh'
data.get('batch')
       
65
data.get('age')
       
d
       
{1: 3}
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65}
data.get('age','key is not present')
       
'key is not present'
data.get('batch','key is not presnt')
       
65
data['phnno']=1234567
       
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567}
id(data)
       
2243474286848
data.update({'email':'dinesh2gmail.com','py':2026})
       
d
       
{1: 3}
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
data['age']=22
       
id(data)
       
2243474286848
data.popitem()
       
('age', 22)
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
data.pop('course')
       
'pfs'
d
       
{1: 3}
data
       
{'name': 'dinesh', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
data.pop('age')
       
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    data.pop('age')
KeyError: 'age'
data.pop('py')
       
2026
data
       
{'name': 'dinesh', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com'}
data.clear()
       
data
       
{}
data = {'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
       
data
       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
len(data)
       
6
data.keys()
       
dict_keys(['name', 'course', 'batch', 'phnno', 'email', 'py'])
data.values()
       
dict_values(['dinesh', 'pfs', 65, 1234567, 'dinesh2gmail.com', 2026])
data.items()
       
dict_items([('name', 'dinesh'), ('course', 'pfs'), ('batch', 65), ('phnno', 1234567), ('email', 'dinesh2gmail.com'), ('py', 2026)])
sorted(data)
       
['batch', 'course', 'email', 'name', 'phnno', 'py']
max(data)
       
'py'
min(data)
       
'batch'
d = {1:1,2:2}
       
m = d
       
m[3]=3
       
m
       
{1: 1, 2: 2, 3: 3}
>>> d
...        
{1: 1, 2: 2, 3: 3}
>>> n = d.copy()
...        
>>> n[5]=5
...        
>>> n
...        
{1: 1, 2: 2, 3: 3, 5: 5}
>>> d
...        
{1: 1, 2: 2, 3: 3}
>>> data
...        
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
>>> data.get('py')
...        
2026
>>> data.setdefault('py':2026)
...        
SyntaxError: invalid syntax
>>> data.setdefault('py',2026)
...        
2026
>>> data
...        
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
>>> data.setdefault('name',2026)
...        
'dinesh'
>>> data
...        
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026}
>>> data.setdefault('email',2026)
...        
'dinesh2gmail.com'
>>> data.setdefault('key',2026)
...        
2026
>>> data
...        
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'phnno': 1234567, 'email': 'dinesh2gmail.com', 'py': 2026, 'key': 2026}
>>> dict.fromkeys(["python","mysql","java"],0)
...        
{'python': 0, 'mysql': 0, 'java': 0}
