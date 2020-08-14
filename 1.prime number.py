n=int(input("enter a number"))
count=0
for i in range(1, n+1):
     if n%i==0:
          count+=1
if count==2:
     print(n, 'prime')
else:
     print(n, 'not prime')         
                                      
          
          
          
          MODEL 2 
n =int(input("enter a number"))
for num in range (1,n+1):
      if num>1:
           for num in range (2,num):
                 if num%i==0:
                    break
           else:
              print(num,"prime number")
