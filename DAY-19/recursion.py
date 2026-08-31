'''
def display(n):     #print 10 to 1 with display(1)
    if n == 11:
        return
    
    display(n+1)
    print(n)
display(1)

def display(s,i):
    if i==len(s):
        return
    
    display(s,i+1)
    print(s[i],end=' ')

display("codegnan",0)



def display(s,ind,w):
    if len(s)-w+1 == ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)

s = input("Enter a String: ")
w = int(input("Enter width: "))
display(s,0,w)




def display(n):
    if len(n)==0:
        return

n = input().split()
display(n,0)


def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)

l = list(map(int,input("Enter a list: ").split()))
print(display(l,0))


def display(n):
    if n == 0:
        return 0
    return (n%10) + display(n//10)

n = int(input("Enter a number: "))
print(display(n))


def display(n):
    if n == 0:
        return 1
    return (n%10) * display(n//10)

n = int(input("Enter a number: "))
print(display(n))


def display(n):         #imp
    if n == 0:
        return 1
    return n * display(n-1)

n = int(input("Enter a number: "))
print(display(n))

'''

def display(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return display(n-1) +  display(n-2)
r = int(input("Enter the range: "))
for i in range(r):
    print(display(i),end=' ')