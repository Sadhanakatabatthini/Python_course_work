'''
var = lambda arg: exp


wish = lambda name: f"Welcome to the course {name}"
print(wish("dipak"))
print(wish("kittu"))

gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(1,2,3))
print(avg(4,5,6))

iseven = lambda a: "Even" if a % 2 == 0 else "Odd"
print(iseven(5))
print(iseven(4))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(2,3,4))
print(largest(6,1,9))

isvowel = lambda a : "vowel" if a in "aeiouAEIOU" else "Cons"
print(isvowel("a"))
print(isvowel("b"))


l = [1,2,3,4,5,6,7]
update = list(map(lambda i: i+10,l))
print(update)

t = (2344,5474,9875,3256,3656)
discount = list(map(lambda i:i-i*0.3,t))
print(discount)



l = [1,2,3,4,5,6,7]
update = list(filter(lambda i: i%2!=0,l))
print(update)

t = (2344,5474,9875,3256,3656)
discount = list(filter(lambda i:i>1000,t))
print(discount)

l = ["sowmya@codegnan.com","sowmya@ahoo.com","sowmya@gmail.com","sowmya@outlook.com"]
res = list(map(lambda i: i.split('@')[-1],l))
print(res)



from functools import reduce

l = [4,2,4,64,75,2,2345,8]

res = reduce(lambda sum,i: sum+i,l)
print(res)

res1 = reduce(lambda prod,i: prod*i,l)
print(res1)

'''
seats = {
    's1':True,
    's2':False,
    's3':False,
    's4':False,
    's5':True,
    's6':True
    }

avail_seats = list(filter(lambda i: seats[i]!=True,seats))
print(avail_seats)

products = {
    'eggs':80,
    'sugar':60,
    'salt': 30,
    'butter':40,
    'milk': 25
}

res = list(filter(lambda i: products[i]>50,products))
print(res)

print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))

