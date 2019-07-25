"""Program for Palidrome"""

n= int(input())
a = 1     """intial inputs"""
b = 1
temp = b
x = [a,b]
while a < n:   """check until n"""
    temp = a+b
    a = b
    b = temp
    if temp > n:
        break
    x.append(temp)    """Adds the number to the list"""
print("Fibo series : {} ".format(x))