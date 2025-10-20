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


'''
f=open("demo.txt","at")
data=f.write("\n this is append")
print(data)
