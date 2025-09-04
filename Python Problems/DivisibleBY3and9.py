l = []

for i in range(10):
    x = int(input("Enter a number: "))
    l.append(x)

    
for i in range(10):
    if (l[i]%3==0&l[i]%9==0):
        print(l[i])
