'''
budget=int(input("Enter Budget: "))
if budget>10000:
    print("Trip")
elif budget>5000:
    print("Resort Stay")
elif budget>3000:
    print("Movie and dinner")
elif budget>1000:
    print("Cafe and Shopping")
elif budget>500:
    print("Street food and Park Visit")
else:
    print("Stay Home")


hr = int(input("enter the time:"))
if 5<=hr<=11:
    print("Good morning")
elif 12<=hr<=16:
    print("Good Afternoon")
elif 17<=hr<=20:
    print("Good Evening")
elif 21<=hr<24:
    print("Good Night")
else:
    print("Midnight sleep well")
'''
budget=int(input("enter budget:"))
if budget>10000:
    print("Cloud Hosting")
elif budget>5000:
    print("Business Hosting")
elif budget>2000:
    print("Preminum Hosting")
else:
    print("Single Hosting")
