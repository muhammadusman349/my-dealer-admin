import os
import django

import django
# from openpyxl import Workbook
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_dealer_admin.settings')
django.setup()

from accounts.models import User,Member

# Check if Item is Exists

# mylist = ["apple","banana","cherry","orange", "kiwi", "melon"]
# if "apple" in mylist:
#     print("yes,apple is in the fruits list")
# print(mylist[2:])

# Change List items

# list = ["apple","banana","cherry"]
# list[1]= "blackcurrant"
# print(list)

#Change the second and third value by replacing it with one value:

# thislist = ["ali","hamza","bilal"]
# thislist[0:2] = ["raza"]
# print(thislist)

#Insert Items

# list1 =  ["apple","banana","orange"]
# list1.insert(2,"watermelon")
# print(list1)

# Append Items

# list2  = ["civic","Bmw","Sonata"]
# list2.append("Honda")
# print(list2)

# Extend List

# list3 = ["banana","orange","watermelon"]
# extend = ["mango","papaya","apple"]

# list3.extend(extend)

# print(list3)

# Remove List Items

# list4 = ["apple","banana","mango"]
# list4.remove("banana")
# print("Remove item",list4)

# # Pop list

# list5  = ["apple","banana","watermelon"]
# list5.pop(1)
# print("pop list item",list5)

# # del list

# dellist = ["a","b","c","d"]
# del dellist[0]
# print(dellist)

# # clear list

# clearlist = ["app","game","socail"]
# clearlist.clear()
# print(clearlist)

# loop lists

# loop = ["app","banana","cherry"]
# for x in loop:
#  print(x)

# Loop through the index numbers

# index = ["wali","ali","zayn"]
# for i in range(len(index)):
#  print(index[i])

# looping using list comprehension

# list6 = ["usman","abbas","afaq","zarar"]
# [print(x) for x in list6]

# name = ["usman","ali","zarar","afaq"]
# new = []

# for x in name :
#     if "q" in x:
#         new.append(x)
# print(new)

# newlist = [x for x in name if x != "ali"]
# print(newlist)

# Sort list 

# list7 = ["orange","mango","kiwi","apple","pineapple","banana"]
# list7.sort()
# print(list7)

# list8 = [100,290,50,64,300,44]
# list8.sort()
# print(list8)

# list9 = ["orange","mango","kiwi","pineapple","banana"]
# list9 = [100,290,50,64,300,44]
# list9.sort(reverse=True)

# print(list9)

# def myfunc(n):
#     return abs(n -20)

# list10 = [100,50,65,82,23]
# list10.sort(key = myfunc)
# print(list10)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
# thislist1.reverse()
# print(thislist1)

# list11 = ["ali","banana","app","apple"]
# mylist = list11.copy()
# print("copy list",mylist)

# thelist = ["apple","banana","cherry"]
# myl = list(thelist)
# print(myl) 


# Join Lists

# list01 = ["a","b","c"]
# list02 = [1,2,3]

# list01.extend(list02)
# for x in list02:
    # list01.append(x)
# list03 = list01 + list02

# print(list01)
 
#################   DICTIONARIES    ##################

# dict = {
#     "brand":"ford",
#     "model":"mustang",
#     "year" : 1965
# }

# print(dict["brand"])

# dict1 = {
#     "brand":"ford",
#     "model":"mustang",
#     "year":2030,
#     "year":2020

# }

# print(dict1)
# print(len(dict1))

# dict2 = {
#     "brand":"Honda",
#     "electric": False,
#     "year": 1973,
#     "colors":["red","black","white"]
# }
# print(dict2)

# # for i,k in dict2.items():
# #     print(i,k)


# dict3 = {
#     "brand":"VIVO",
#     "color":"Sky blue",
#     "Ram/Rom":"4/128",
#     "year":2020,
#     "fast charging":True
# }

# # x = dict3.get("Ram/Rom")
# x= dict3.keys()
# print(x)

# car = {
#     "brand":"civic",
#     "model":"honda",
#     "year":2018
# }

# x= car.keys()
# print(x)
# car["color"] = "white"

# print(x)


# man = {
#     "color":"white",
#     "language":"urdu",
#     "year":1999
# }

# x= man.values()
# print(x)
# man["year"] = 2000
# print(x)

# for x,y in man.items():
#     print(x,":",y)

################# NASTED DICTIONARIES ################

# School = {
#     "student1":{
#         "name":"Zarar",
#         "roll.no":3
#     },
#     "student2":{
#         "name":"Ali Abbas",
#         "roll.no":19
#     },
#     "student3":{
#         "name":"Afaq",
#         "roll.no":25
#     },
#     "student4":{
#         "name":"usman",
#         "roll.no":27
#     }
# }

# print(School["student1"]['name'])


# x = ('key1','key2','key3')
# y = 

# List = []
# print("blank list: ")
# print(List)


# List = [10,20,14]
# print("\nList of numbers: ")
# print(List)

# List = ["Epochs","IT","Solution"]
# print("\nList items: ")
# print(List[2])
# print(List[1])


dict1= {
    "brnd":"ford",
    "model":"mustang",
    "year":1987
}

# dict.update({"color":"red"})
# dict["color"] = "black"
# dict.pop("brnd")
# dict.popitem()
# del dict["brnd"]
# del dict1
# dict1.clear()
# print(dict1)

# for x in dict1:
    
    # print(x)
    # print(dict1[x])

# for x in dict1.values():
#     print(x)
# my = dict1.copy()
# my = dict(dict1)

# print(my)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# 0
# x = car.setdefault("model","red")

# print(x)

# newl =[n for n in range(10)]
# print(newl)  

# new = [n for n in range(50) if n % 2 == 0]
# print(new)



# def make_pretty(func):
#     def inner():
#         print("I got Triple ELemination")
#         func()
#     return inner
# @make_pretty
# def ordinary():
#     print("i am ordinary")
# ordinary()


# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner

# @star
# @percent
# def printer(msg):
#     print(msg)

# printer = star(percent(printer))
# printer("Hello")

# def my_gen():
#     n = 1
#     print("This is printed first")
#     yield n
#     n+=1
#     print("this is printed second")
#     yield n
#     n+=1
#     print("this is printed at last")
#     yield n

# for item in my_gen():
#     print(item)


## Fibonacci Sequence ##

# def gen_fibon(n):
#     a= 1
#     b= 1
#     for i in range(n):
#         yield(a)
#         a,b = b,a+b
# for number in gen_fibon(10):
#     print(number)
# g = gen_fibon(10)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# n = [1,3,5]
# e = [2,4,6]

# n.append(e)

# print(n)


# p = [11,3,7,5,2]
# p.sort(reverse=True)
# print(p)

# def takeSecond(elem):
#     return elem[1]

# ran=[(2,2),(3,4),(4,1),(1,3)]
# ran.sort(key=takeSecond)

# print(ran)

# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]

# def get_name(employees):
#     return employees.get('Name')

# employees.sort(key=get_name)

# print(employees)

# string = input("enter elements(space-separated): ")

# lst = string.split()

# print('the list is :',lst)

# m = []
# for i in range(5):
#     m.append([])
#     # print(m)
#     for j in range(5):
#         m[i].append(j)
# print(m)

# m = [[j for j in range(5)]for i in range(5)]

# print(m)

planets  = [['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
f_p = [planet for sublist in planets for planet in sublist if len(planet)<6]
print(f_p)


# f_p = []
# for sublist in planets :
    # print(sublist)
    # for planet in sublist:
        # print(planet)
        # if len(planet)>=7:
            # print(planet)
            # f_p.append(planet)
# print(f_p)