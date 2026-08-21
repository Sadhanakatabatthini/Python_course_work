''''
n = int(input("enter the input: "))
result = [ ]
for i in range(1,n+1):
    if n%i==0:
        result.append(i)
print(f'Factors of {n} = {result}')

s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
s = input("enter a string: ")
count = 1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res+=s[i]+str(count)
        count=1
print(res+s[i]+str(count))