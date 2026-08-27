#int float complex str list tuple set dict bool

#list dict set
'''
Pass by Value: - A copy of the value is passed to the function. Changes inside the function don't affect the original variable.

Pass by Reference: - The reference/address of the original object is passed. Changes inside the function can affect the original object.

def display(n):
    n.append(5)
    print("Inside the function:",n)

n=[1,2,3,4]
display(n)
print("Outside the function:",n)


def display(n):
    n.add(5)
    print("Inside the function:",n)

n={1,2,3,4}
display(n)
print("Outside the function:",n)

def display(n):
    n+=10
    print("Inside the function:",n)

n=10
display(n)
print("Outside the function:",n)

def display(n):
    n+=10.3
    print("Inside the function:",n)

n=10.3
display(n)
print("Outside the function:",n)


def display(n):
    n+=10
    print("Inside the function:",n)

n=3+5j
display(n)
print("Outside the function:",n)


def display(n):
    n+=" language"
    print("Inside the function:",n)

n="Python"
display(n)
print("Outside the function:",n)


def display(n):
    n+=(5,6)
    print("Inside the function:",n)

n=(1,2,3,4)
display(n)
print("Outside the function:",n)

def display(n):
    n=True
    print("Inside the function:",n)

n=False
display(n)
print("Outside the function:",n)

def display(n):
    n[5] = 6
    print("Inside the function:",n)

n={1:2,3:4}
display(n)
print("Outside the function:",n)


'''