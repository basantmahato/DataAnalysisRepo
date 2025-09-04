l=[]


sum=0
mul=1

for i in range(10):
    x = int(input("Enter A number"))
    l.append(x)
    

    if x%2==0:
        sum = sum + x

    if x%2!=0:
        mul = mul * x

print(sum)
print(mul)









