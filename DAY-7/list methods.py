Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list methods
>>> l = []
>>> l = list()
>>> type(l)
<class 'list'>
>>> l = [1,12.3,"str,True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8i]
...      
SyntaxError: unterminated string literal (detected at line 1)
>>> l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8i]
...      
SyntaxError: invalid decimal literal
>>> l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
...      
>>> l
...      
[1, 12.3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
>>> l = [1,1,1,1]
...      
>>> l
...      
[1, 1, 1, 1]
>>> a =[1,2,3]
...      
>>> b = [4,5,6]
...      
>>> a+b
...      
[1, 2, 3, 4, 5, 6]
>>> a*3
...      
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a = [567,76,13,134,,234]
...      
SyntaxError: invalid syntax
>>> a = [567,76,13,134,234]
...      
>>> a
...      
[567, 76, 13, 134, 234]
>>> a[1]
...      
76
>>> a[3]
...      
134
a[5]
     
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[5]
IndexError: list index out of range
a[4]
     
234
a[-1]
     
234
a[-4]
     
76
a[-5]
     
567
a[1:4]
     
[76, 13, 134]
a[::-1]
     
[234, 134, 13, 76, 567]
a[1::2]
     
[76, 134]
a[::2]
     
[567, 13, 234]
76 in a
     
True
2345 in a
     
False
13 not in a
     
False
234 in a
     
True
l
     
[1, 1, 1, 1]
a
     
[567, 76, 13, 134, 234]
max(a)
     
567
min(a)
     
13
sorted(a)
     
[13, 76, 134, 234, 567]
len(a)
     
5
id(a)
     
1890038332672
a[0]=56
     
a
     
[56, 76, 13, 134, 234]
a[3]=43
     
a
     
[56, 76, 13, 43, 234]
a[-2]=32
     
a
     
[56, 76, 13, 32, 234]
a[-1]=23
     
a
     
[56, 76, 13, 32, 23]
id(a)
     
1890038332672
a.append(50)
     
a
     
[56, 76, 13, 32, 23, 50]
a.append(60)
     
a
     
[56, 76, 13, 32, 23, 50, 60]
a.insert(2,40)
     
a
     
[56, 76, 40, 13, 32, 23, 50, 60]
a.extend([1,2,3])
     
a
     
[56, 76, 40, 13, 32, 23, 50, 60, 1, 2, 3]
a.pop()
     
3
a
     
[56, 76, 40, 13, 32, 23, 50, 60, 1, 2]
a.pop()
     
2
a.pop(0)
     
56
a.pop(3)
     
32
a.remove(23)
     
a
     
[76, 40, 13, 50, 60, 1]
del a[1]
     
a
     
[76, 13, 50, 60, 1]
a.clear()
     
a
     
[]
id(a)
     
1890038332672
1890038332672
     
1890038332672

