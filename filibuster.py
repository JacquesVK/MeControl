x=0
t=0
p=0
while x<100:
    x=x+1
    if x % 3>0:
        p=p+1
        print(x)
    else:
        print("fuck you!!!")
        t=t+1


print("Числа без остатка: ", t)
print("Числа с остатком: ", p)