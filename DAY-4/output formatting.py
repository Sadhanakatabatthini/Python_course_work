Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# output formatting
print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(a,b,c)
NameError: name 'a' is not defined
a = 10
b = 12.3
c = 'codegnan'
print(a,b,c)
10 12.3 codegnan
print( "a=" ,a, "b=" ,b, "c=" ,c)
a= 10 b= 12.3 c= codegnan
>>> print( "a=" ,a, "b=" ,b, "c=" ,c , sep= ' ')
a= 10 b= 12.3 c= codegnan
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='')
a=10b=12.3c=codegnan
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\n')
a=
10
b=
12.3
c=
codegnan
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\t')
a=	10	b=	12.3	c=	codegnan
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\t' ,end='\n\n')
a=	10	b=	12.3	c=	codegnan

>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\t' , end=@)
SyntaxError: invalid syntax
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\n','@')
SyntaxError: positional argument follows keyword argument
>>> print( "a=" ,a, "b=" ,b, "c=" ,c,sep='\n', end ='@')
a=
10
b=
12.3
c=
codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.300000 c=codegnan
>>> print('a={} b={} c={}' .format(a,b,c))
a=10 b=12.3 c=codegnan
>>> print('a={0} b={0} c={2}' .format(a,b,c))
a=10 b=10 c=codegnan
>>> print('a={} b={} c={}' .format(d,c,a))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('a={} b={} c={}' .format(d,c,a))
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> print('a={} b={} c={}' .format(b,c,a))
a=12.3 b=codegnan c=10
>>> print('a={2} b={0} c={1}' .format(a,b,c))
a=codegnan b=10 c=12.3
>>> print('a={2} b={0} c={1}' .format(a,b,c))
a=codegnan b=10 c=12.3
