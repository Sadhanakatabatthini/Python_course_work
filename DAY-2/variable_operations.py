Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================================================== RESTART: C:/Users/sadha/OneDrive/Desktop/Python Course-work/DAY-2/keywords.py ====================================================
Traceback (most recent call last):
  File "C:/Users/sadha/OneDrive/Desktop/Python Course-work/DAY-2/keywords.py", line 1, in <module>
    import keywords
  File "C:\Users/sadha/OneDrive/Desktop/Python Course-work/DAY-2\keywords.py", line 3, in <module>
    print(keyword.kwlist)
NameError: name 'keyword' is not defined. Did you mean: 'keywords'? Or did you forget to import 'keyword'?
>>> 
===================================================== RESTART: C:/Users/sadha/OneDrive/Desktop/Python Course-work/DAY-2/keywords.py ====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
===================================================== RESTART: C:/Users/sadha/OneDrive/Desktop/Python Course-work/DAY-2/keywords.py ====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a = 10
>>> a
10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c =10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a , b = b, a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a
NameError: name 'a' is not defined
