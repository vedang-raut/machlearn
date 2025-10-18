'''count=0
store=0
while count<=10:
    store=count+store
    count=count+1
    if count==11:
        print(store)
'''
store=1
for i in range(10,1,-1):
    store=store*i
    print(store)
print(store)