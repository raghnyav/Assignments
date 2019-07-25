"""Program to print fibonacci series of given number"""
"""inputting the number"""

n= int(input("\n Enter: "))

"""Initializing First and Second Values of a Series"""
i = 0
First = 0
Second = 1
           
""" Find & Displaying Fibonacci series"""
while(i < n):
           if(i <= 1):
                      Next = i
           else:
                      Next = First + Second
                      First = Second
                      Second = Next
           print(Next)
           i = i + 1