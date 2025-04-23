# def suresh():
#     print("this is function")
# suresh()    

# #single parameter function
# def suresh(aa):
#     print("this is function",aa)     
# suresh(12)    

# #multiple parameter function
# def suresh(aa,b,c):
#     print("this is function",aa,b,c)
# suresh(12,34,56)   

# def suresh(a,b):
#     print(a+b)
# suresh(15,20)  
# suresh(30,25)  

# def lakshmi(name):
#     print("hii",name)
# n=input("enter your name")    
# lakshmi(n)

# #orbitary argument-more arguments to one parameter
# def lakshmi(*name):
#     print("hii",name)
# lakshmi(1,2,3,4,5,6,7,8,9)

# #key word arguments
# def lakshmi(**name):
#     print("hii",name)
# lakshmi(name='ram',age=25)    

# #nested function
# def outer_function():
#     print("this is outer function")
#     def inner_function():
#         print("this is inner function")
#     inner_function()
# outer_function()

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)    
def mul(a,b):
    print(a*b)     

#lambda -lambda function is small anonymous function, can take any number of argument but
#can only have one expression
# x=lambda a,b,c : a+b+c
# print(x(5,2,3))

# l1=[2,3,54,6,56]
# l2=[]
# for i in l1:
#     t=lambda a : a+1
#     l2.append(t(i))
# print(l2)    

#filter() -filters the given sequence with a function which tests each element to be true
# ages=[5,12,14,18,23,34]
# def myfunction(x):
#     if x<18:
#         return False
#     else:
#        return True
# adults=filter(myfunction,ages)        
# print(list(adults))

# #map()
# def caluclateaddition(n):
#     return n+n
# numbers=(1,2,3,40)
# result=map(caluclateaddition,numbers)
# print(list(result))

#reduce()
# from functools import reduce
# d=reduce(lambda a,b:a+b,[23,21,34,21])
# print(d)

# #Generator function()
# def simplegeneratorfun():
#     yield 1
#     yield 2
#     yield 3
# x=simplegeneratorfun()

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


#return()
# def aa():
#     return 1+1
# print(aa())

nums=[11,32,22,44,54]
def even(x):
    if x%2==0:
      print(x)

map=list(map(lambda x:x**2,nums))      
print(list(map))
filter=list(filter(lambda x: x%2==0,nums))
print(list(filter))