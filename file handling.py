''' f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()



# lets understand the default mode that is read "r" and text "t" mode.



file=open("demo.txt","rt")  #Default mode that is read and text
data=file.read()
print(data)
print(type(data))
file.close




diwali=open("demo.txt","rt")
data=diwali.readline()
print(data)
diwali.close()



hang=open('demo.txt',"wt")
data=hang.write("I have rewritten all the text")
print(data)



f=open("demo.txt","at")
data=f.write("\n this is append")
print(data)



f=open("demo.txt","w+")
data=f.write("sanika")
print(data)



f=open("demo.txt","r+")
data=f.write("they print in the front, as the cursor is ended")
vedang=f.write("\n now i")
sanika=f.write("doctor hai bhai voh")

print(data)
print(vedang)





f=open("demo.txt","a+")
datas=f.read()
data=f.write("vedang")
datas=f.read()

print(data)
print(datas)



with open("vedang.txt","x") as f:
    print(f.read())


f=open("sample.txt","w")
print(f.write("this will be deleted"))

import os
os.remove("sample.txt")





with open("reagaltos.txt", 'x') as f:
    f.write("vx")

'''

with open("practice.txt","r") as f:
    data=f.read()
newdata=data.replace("java","python")
print(newdata)  


with open("practice.txt","w") as f:
    f.write(newdata)



   
    