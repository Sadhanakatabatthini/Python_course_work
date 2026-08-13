Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> type(a)
<class 'int'>
>>> b = 12.3
>>> type(b)
<class 'float'>
>>> c = 1+2j
>>> type(c)
<class 'complex'>
>>> #sequential data types - string list tuple
>>> s = 'codegnan'
>>> id(s)
2334963172784
>>> s += 'python'
>>> s
'codegnanpython'
>>> l = [1,2,3,4]
>>> type(l)
<class 'list'>
>>> t = (1,2,3,'v')
>>> type(t)
<class 'tuple'>
>>> s={1,2,4,3,5,45}
>>> type(s)
<class 'set'>
>>> d = {'productname':'abc','price':23,'stock':True}
>>> d
{'productname': 'abc', 'price': 23, 'stock': True}
>>> type(d)
<class 'dict'>
>>> s=frozenset({1,1,1,116,18})
>>> s
frozenset({1, 18, 116})
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> type(s)
<class 'frozenset'>
>>> s=None
>>> type(s)
<class 'NoneType'>
