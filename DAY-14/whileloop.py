'''
i=1
while i<=10:
    print(i)
    i+=1

i = 10
while i<=0:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

i = 5
while i<=50:
    print(i)
    i+=5

s = 'while loop'
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1

l=[2345,5467,9876,3578]
i=0
while i<len(l):
    print(l[i])
    i+=1


n = int(input("Enter a number: "))
while n!=0:
    a=n%10
    n=n//10
    print(a)

n = int(input("Enter a number: "))
sum=1
while n!=0:
    a=n%10
    n=n//10
    sum*=a
print(sum)

n = int(input("Enter a number: "))
while n!=0:
    a=n%10
    n=n//10
    print(a,end="")

n = int(input("Enter a number: "))
res = 0
while n > 0:
    rem = n%10
    res=res*10+rem
    n//=10
print(res)

n = int(input("Enter a number: "))
res = 0
while n > 0:
    rem = n%10
    if rem%2==0:
        res += rem
    n//=10
print(res)


l = [7,9,23,0,0,0,12,0,13,0,1,0,4,0,1,0,0,1,4,5,6,6,13,0]
while 0 in l:
    l.remove(0)
print(l)
'''

l = [1,2,3,4,5,6,7,8,9]
i=0
j=len(l)-1
while i<=j:
    if i == j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
