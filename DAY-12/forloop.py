''' 
for var in seq:
    #stmts

----------------------------------------------------

s = "Python Programming"
for i in s:
    print(i)

l=[1,2,3,4,5]
for i in l:
    print(i)

prices = (923,45,345,567)
for price in prices:
    print(price)

names = {'sadhana','ramya','vishwa'}
for name in names:
    print(name)

d = {1:2,2:4,3:6,5:6}
for i in d:
    print(i)

# range function
range(start,end+1,step)

for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

s="Python Programming"
for i in range(len(s)):
    print(i,s[i])

s = [1,2,3,4]
for i in range(len(s)):
    print(i,s[i])

s = (1,2,3,4)
for i in range(len(s)):
    print(i,s[i])

s = {1,2,3,4}            #not works for set because it doesnot have index
for i in range(len(s)):
    print(i,s[i])

#enumerate function
s = [234,345,657,987]
for i in enumerate(s):
    print(i[0],i[1])

d = {1:2,2:4,3:6,5:6}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

    
l = [12,13,14,15,16,18,19]
n = 15
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")


pin = 1234
for i in range(5):
    epin=int(input("enter the pin: "))
    if epin==pin:
        print("unlock phone")
        break
    else:
        print("invalid pin")
else:
    print("try after 30 seconds")
'''
#prime number
n = int(input("Enter a number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("Prime number")
