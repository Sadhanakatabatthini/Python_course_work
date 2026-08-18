'''
fa = eval(input("follows account:"))
if fa:
    cf = eval(input("Close friend:"))
    if cf:
        print("story visible")
    else:
        print("not in Close friend list")
else:
    print("follow the account first")

reg=eval(input("Registered:"))
if reg:
    fee=eval(input("Fee Paid:"))
    if fee:
        print("tournament entry confirmed")
    else:
        print("entry fee pending")
else:
    print("registration required")

link=eval(input("Link Status:"))
if link:
    per_gran=eval(input("Permission Granted:"))
    if per_gran:
        print("File opened Succesfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
'''

data = {
    'sadhana':{'status':True,'python':90,'mysql':93,'flask':89},
    'ramya':{'status':True,'python':98,'mysql':92,'flask':99},
    'chaitanya':{'status':False,'python':None,'mysql':None,'flask':None},
    'vaibhav':{'status':True,'python':80,'mysql':83,'flask':89},
    'navaneeth':{'status':True,'python':70,'mysql':73,'flask':79}
}
name =  input("Enter the name")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f'Hello {name}!!!!')
        print(f"your Avg score is {avg}")
        if avg>=90:
            print("Outstanding Performance")
        elif avg>=80:
            print("Very Good")
        elif avg>=70:
            print("Good,work hard")
        elif avg>=35:
            print("better luck next time")
        else:
            print("you failed the exam,try hard")
    else:
        print(f'{name} did not write the exam,bring your parents')

else:
    print(f'{name} not found in data')