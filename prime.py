
"""Program to check whether prime or not"""

n = int(input("Enter a number: "))

"""All prime numbers are greater than 1 """

if n > 1:
   """checking factors"""
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
       
else:
   print(n,"is not a prime number")