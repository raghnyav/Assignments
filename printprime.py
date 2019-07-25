# -*- coding: utf-8 -*-

"""PRINT THE PRIME NUMBERS"""
def primes(n):
 
    for i in range(2,n+1):
        count=0
        for j in range(1,i):
            if i%j==0:
                count=count+1
        if count==1:
            print(i)
primes(7)