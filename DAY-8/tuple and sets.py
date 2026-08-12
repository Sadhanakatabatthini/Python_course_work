Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
t = ()
t = (1,2,3,4,5

     )
t
(1, 2, 3, 4, 5)
t = (1)
t
1
t = (1,) # we need to add , when there is a single element
t
(1,)
t = (1,1,1,1) # allows duplicates
t = (1,23.4,{1,2,3},[1,2]) # heterogeneous
t
(1, 23.4, {1, 2, 3}, [1, 2])
type(t)
<class 'tuple'>
#tuple operations
t = (1,23.4,"str" , [1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1] # accessing particular elements through index
23.4
t[-1]
True
t(5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t(5)
TypeError: 'tuple' object is not callable
t[5]
{1, 2, 3}
t[3:7] # accessing pair of elements through slicing
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t[::-1]
(True, {1: 1, 2: 2}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.4, 1)
23.4 in t # checking whether element present or not using membership function
True
5 in t
False
true in t
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    true in t
NameError: name 'true' is not defined. Did you mean: 'True'?
True in t
True
t = (23,34,45,56,67,78,89,90)
t
(23, 34, 45, 56, 67, 78, 89, 90)
sorted(t)
[23, 34, 45, 56, 67, 78, 89, 90]
t[::-1]
(90, 89, 78, 67, 56, 45, 34, 23)
max(t)
90
min(t)
23
len(t)
8
t.index(34)
1
t.count(32)
0
t.count(56)
1
1
1
t = (1,2,3,4,[1,2,3],5)
t
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
[1, 2, 3]
t[4].append
<built-in method append of list object at 0x00000175E37B1300>
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t=(1,2,34,4)
sum(t)
41
# set properties
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,123456,124,312}
s
{123456, 1, 2, 3, 4, 5, 6, 312, 124}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add("str")
s
{1, 'str', 12.3}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
# only immutable elements are allowed to add into the set
s.add(False)
s
{False, 1, 'str', 12.3}
s.add((1,2,3))
s
{False, 1, (1, 2, 3), 12.3, 'str'}
s.add(True)
s
{False, 1, (1, 2, 3), 12.3, 'str'}
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a #membership operation
True
a | b #union operation
{1, 2, 3, 4, 5, 7, 8, 9}
a & b # intersection
{3, 5}
a - b # minus
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
[1]<=a # subset
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    [1]<=a # subset
TypeError: '<=' not supported between instances of 'list' and 'set'
{1} <= a
True
{1,2,3} <= a
True
a >= {1,2}
True
a >= {15,16}
False
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a = {12,23,54,5,24,1289}
sorted(a)
[5, 12, 23, 24, 54, 1289]
max(a)
1289
min(a)
5
len(a)
6
a.index(a)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
# because the set is unordered , index does not work
a.count(23)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.count(23)
AttributeError: 'set' object has no attribute 'count'
# set has only unique elements
all(54,24,5,1289)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    all(54,24,5,1289)
TypeError: all() takes exactly one argument (4 given)
KeyboardInterrupt
all({54,24,5,1289})
True
any({5,34,54,14})
True
sum(a)
1407
a
{5, 54, 23, 24, 1289, 12}
a = {1,2,3}
b = a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c = a.copy()
c
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a.add(40)
>>> a
{1, 2, 3, 4, 40}
>>> a.add(100)
>>> a
{1, 2, 3, 4, 100, 40}
>>> a.add({10,20,30,40})
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.add({10,20,30,40})
TypeError: unhashable type: 'set'
>>> a.update({10,20,30,40})
>>> a
{1, 2, 3, 4, 100, 40, 10, 20, 30}
>>> a.pop()
1
>>> a.pop()
2
>>> a
{3, 4, 100, 40, 10, 20, 30}
>>> a.pop()
3
>>> a
{4, 100, 40, 10, 20, 30}
>>> a.remove(100)
>>> a
{4, 40, 10, 20, 30}
>>> a.remove(100) # does not handle exception
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.remove(100) # does not handle exception
KeyError: 100
>>> a.discard(100) # handles exceptions
>>> a
{4, 40, 10, 20, 30}
>>> a.clear()
>>> a
set()
>>> a = frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
