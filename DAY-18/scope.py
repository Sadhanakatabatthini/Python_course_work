#Global Scope - A variable created outside all functions has global scope. It can be accessed inside and outside functions.
'''
def display():
    print("Inside function:",n)

n=10
display()
print("Outside function",n)

#local variables -A variable created inside a function has local scope. It can be used only inside that function.
def display():
    n=10
    print("Inside function:",n)

display()
print("Outside function",n)

#to make local variable a global access
def display():
    global n
    n=10
    print("Inside function:",n)

display()
print("Outside function",n)



def display():
    global n
    n+=10
    print("Inside function:",n)
n=10
display()
print("Outside function",n)



def display():
    course = "PFS"
    def update():
        nonlocal course
        course = "JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display



def display():
    course = "PFS"
    def update():
        course = "JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()



l = [1,2,3,4,5]   
print(sum(l))

sum = 20
print(sum(l))   # if we use built in functions as variables it losses its functionality



l = [1,2,3,4,5]
print(max(l))

print = 20
print(max)


'''