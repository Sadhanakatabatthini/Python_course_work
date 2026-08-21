data = {
    'rice' : 1000,
    'dal' : 50,
    'sugar' : 45,
    'tea podwer' : 20,
    'kaju': 500,
    'badam' : 656,
    'eggs' : 60,
    'masala powder': 75,
    'bread': 90,
    'cornflour':87
}
for i in data:
    print(i.ljust(20),data[i])

prods = input("enter the products: ").split()
print("--------------bill--------------")
bill = 0
for i in prods:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total bill".ljust(20),bill)