# 4 basic data types str,int,float,bool

name = "priyo"
print(type(name))  # <class 'str'>
print("stock owner >> " + name)

num = 10000
print(type(num))  # <class 'int'>
print("current stock value " + str(num))

num = 10.9223
print(type(num))  # <class 'float'>
print("Incremental value of stock " + str(num))

num2 = num * 10000
print(num2)
print(type(num2))

isAvl = True
print(type(isAvl))
print("stock avl status: "+str(isAvl))



