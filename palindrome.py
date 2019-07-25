def palin(n):
    temp=n
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
      
        n=int(n/10)
    print(rev)
    if(temp==rev):
        print("is palindrome")
    else:
        print("not a palindrom")
        
palin(131)
