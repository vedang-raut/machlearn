'''def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
    print("end")
    
    

show(5)






def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    

    



print(factorial(5))
   



def natural_sum(n):
    if n==0:
        return 0
    else:
        return natural_sum(n-1)+n
        print("end")
    
      
 
print(natural_sum(5)) 



def bmw(list,index=0):
    if index==len(list):
        return
    else:
        print(list[index])
        bmw(list, index+1)
    
cars=["venue","audi","hyundai","sonet","kia"]    
(bmw(cars))




def natural (n):
    if n==0:
        return 
    print(n)
    natural(n-1)
natural(5)
 



def natural(n):
    if n==0:
        return
    else:
        print (n)
        natural(n-1)
        print("end")

natural(9)




def factorial  (n):
    
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1)*n

    

print(factorial(3))
'''






def jans(list,index=0):
    if index==len(list):
        return
    else:
        print(list[index])
        jans(list,index+1)
cars=["venue","audi","hyundai","sonet","kia"]        
jans(cars)
