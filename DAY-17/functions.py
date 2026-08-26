'''
syntax:

def functionname(arguments):
    #statements
    return -----(optional)


def gst(price):
    print("Original price: ",price)
    print("Final Price: ",price+price*0.18)

gst(1000)
gst(500)
gst(3545)
gst(10000)
gst(5000)



def table(n):
    print(f'{n}-Table')
    print("--------------------------------")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)



def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(isleap(2004))
print(isleap(2014))
print(isleap(2016))


def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not a prime")
            break
        else:
            print("Prime")
            break

isprime(18)




def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "not a Prime number"

    return "Prime"

print(isprime(11))

#types of arguments
-positional arguments : Values are passed according to their position/order.

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('admin','admin@gmail.com','admin@123')
display('admin@gmail.com','admin','admin@123')
display('admin@123','admin','admin@gmail.com')


#Keyword argument - Values are passed using the parameter name.

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='admin',email='admin@gmail.com',pwd='admin@123')
display(email='admin@gmail.com',name='admin',pwd='admin@123')
display(pwd='admin@123',name='admin',email='admin@gmail.com')


#default arguments - A parameter is given a default value while defining the function.

def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('admin','admin@gmail.com')
display('admin@gmail.com','admin','admin@123')
display('admin@123','admin','admin@gmail.com')


#Variable-Length Arguments - Used when we don't know how many arguments will be passed.

def display(*names):
    print(names)

display('dinesh')
display('dinesh','vishnu')
display('dinesh','vishnu','sadhana')
display('dinesh','vishnu','sadhana','laxmi')

'''
def display(**names):
    print(names)

display(n1='dinesh')
display(n1='dinesh',n2='vishnu')
display(n1='dinesh',n2='vishnu',n3='sadhana')
