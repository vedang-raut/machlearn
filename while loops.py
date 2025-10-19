#Basic code for while loops
'''
count= 1
while count<=5:
    print("Apnacollege",count)
    count=count+1
'''
#2.The code for printing the number 1 to 10
'''
i=1
while i<=10:
    print(i)
    i=i+1'''

#3.The code to print the reverese of the sequence
'''
i=10
while i>=1:
    print(i)
    i=i-1'''

#4.lets understand by the loop loops
'''
count=1
while count<=5:
    print(count)
    count=count-1
practice questions
1. To print the numbers from 1 to 100.

count= 1
while count<=100:
    print("count time:",count)
    count=count+1


practice question 2: print the numbers from 100 to 1

count=100
while count>=1:
    print(count)
    count=count-1



n=int(input("the table of:"))
count=1
store=0
while count<=10:
    store=n*count
    print(store)
    count=count+1


To print the square fo number from 1 to 10

count=0
store=0
while count <=10:
    store=count*count
    count=count+1
    print(store)
print ("the condition has ended with the sqaure")


storage=(1,4,9,16,25,36,49,64,81,100)
count=0
while count<len(storage):
    print(storage[count])
    count=1+count




storage=(4,1,9,16,25,36,49,64,81,100)
count=0
x=4
while count<len(storage):
    if storage[count]==x:
        print(count)
    count=count+1



cars=("fronx","taisor","sonet","venue","creta","mustang")
count=0
while count<len(cars):
    print(cars[count])
    count=count+1

cars=("fronx","taisor","sonet","venue","creta","mustang")
count=0
x=input("Enter the name of car")
while count<len(cars):
    if (x==cars[count]):
        print(cars[count],"at index",count)
    count=count+1 
'''



cars=("venue","audi","hyundai","sonet","kia")
count=0
while count<len(cars):
    print(cars[count])
    count=count+1
