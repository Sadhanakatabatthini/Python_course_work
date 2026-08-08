Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#python operators
'''
1. arithmetical operators  
2. comparison
3. assignment
3. relational
4. membership
5. identity
6. bitwise
'''
'\n1. arithmetical operators  \n2. comparison\n3. assignment\n3. relational\n4. membership\n5. identity\n6. bitwise\n'
a=10
b=5
a+b
15
a-b
5
a*b
50
9/2
4.5
9//2
4
10.2//2
5.0
a//2
5
a**3
1000
2**3
8
16**2
256
12%2
0
a<b
False
a>b
True
a<=b
False

a==b
False
a!=b
True
a>=10
True
a = 20
a = a+10
a
30
a = a+20
a
50
a +=10
a
60
a -=10
a
50
a *=20
a
1000
a //=2
a
500

a **=2
a
250000
a /=500
a
500.0
email = true
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    email = true
NameError: name 'true' is not defined. Did you mean: 'True'?
email = True
password = Flase
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    password = Flase
NameError: name 'Flase' is not defined. Did you mean: 'False'?
email = True
passwords = False
email and password
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    email and password
NameError: name 'password' is not defined. Did you mean: 'passwords'?
email and passwords
False
login = True
login = False
display_products = True
login or display_products
True
's' in ' aeiou
SyntaxError: unterminated string literal (detected at line 1)
's' in 'aeiou'
False
's' not in 'aeiou'
True
7%3 and 4%3
1
7%3==0 and 4%3==0
False
6%3==0 and 4%3==0
False
6%3==0 or 4%3==0
True
3%2==0
False
s = 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'a' in s
True
'program' in s
True
'program' not in s
False
l = [1,2,3,4]
3 in l
True
9 not in l
True
1 not in l
False
t = (20,30,40)
50 in t
False
30 in t
True
30 not in t
False
data = {'name' : ' frooti' , 'batch' :65, 'course' = 'pfs'}
SyntaxError: ':' expected after dictionary key
data = {'name' : ' frooti' , 'batch' :65, 'course' : 'pfs'}
frooti in data
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    frooti in data
NameError: name 'frooti' is not defined
'frooti' in data
False
'pen' not in data
True
'name' in data
True
65 in data
False
>>> 'course' in data
True
>>> # membership operators are only applicable for key ,not for values
>>> l = [1,2,3,4]
>>> m = [1,2,34]
>>> del m
>>> m = [1,2,3,4]
>>> id(l)
2159142386816
>>> id(m)
2159137137856
>>> l == m
True
>>> \
... 
...   f
...   
SyntaxError: unexpected indent
>>> l is m
False
>>> n = m
>>> n
[1, 2, 3, 4]
>>> id(n)
2159137137856
>>> m is n
True
>>> n is m
True
>>> n is l
False
>>> n is not l
True
>>> 11 & 8
8
>>> 11 | 8
11
>>> 11 ~ 7
SyntaxError: invalid syntax
>>> 11 ^ 7]
SyntaxError: unmatched ']'
>>> 11 ^ 7
12
>>> 16>>3
2
