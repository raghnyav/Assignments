n= int(input())
a = 1
b = 1
temp = b
x = [a,b]
while a < n: 
    temp = a+b
    a = b
    b = temp
    if temp > n:
        break
    x.append(temp)
print("Fibo series : {} ".format(x))