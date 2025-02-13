#String
#single quotation marks, or double quotation marks.

name = "Niggle, Nandu "
a= 5
print(name[2]) #g
print(len(name)) #14
print("l" in name)  #True
print("l" not in name) #Flase
print(name[2:4]) #gg
print(name.upper()) #NIGGLE, NANDU
print(name.strip()) #remove white space frm beginning or end
print(name.replace("Niggle, Nandu",  "Nandu"))
print(name.split(",")) #['Niggle', ' Nandu ']
print("Hello " + name) #concat


#loop 
for x in name:
    print(x)