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


# dict1= {
#     "brnd":"ford",
#     "model":"mustang",
#     "year":1987
# }

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

# planets  = [['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
# f_p = [planet for sublist in planets for planet in sublist if len(planet)<6]


# f_p = []
# for sublist in planets :
    # print(sublist)
    # for planet in sublist:
        # print(planet)
        # if len(planet)>=7:
            # print(planet)
            # f_p.append(planet)
# print(f_p)

# odd_square =[x**2 for x in range(1,11) if x % 2==1]
# print(odd_square)

# dic = {
#     "name":"usman",
#     "class":"BSSE",
#     "roll_no":27
# }
# dic.keys()
# print(dic)
# dic.update({"mobile":"vivo"})
# print(dic)
# dic["roll_no"]=23
# print(dic)
# for i,v in dic.items():
#     print(i,v)

# def hello_decorator(func):
#     def inner1(*args,**kwargs):
#         print("before Execution")
#         returned_value=func(*args,**kwargs)
#         print("after Execution")
#         return returned_value
#     return inner1

# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
 
# a, b = 1, 2
# print("Sum =", sum_two_numbers(a, b))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# 
# x=car.popitem()
# 
# print(x)

# y = [['vegas','London'],['US','UK']]

# for x in y:
#     for a in x:
#         print(a)
# for myList in [[10,13,17],[3,5,1],[13,11,12]]:
#     for item in myList:
#         print(item)

# lis = ["apple","banana","cherry","orange","kiwi","mango"]
# lis[2:4] = ["blackcurrant","watermelon"]
# print(lis)

# lis.clear()

# print(lis)

# l={
#    "even1":"d",
#    "odd1":"D",
#    'even12':"ds",
#    'odd':"S",
#    "even":"SD"
#    }
# for i,v in l.items():
#     print(i,v)


# n = [1,2,3,4,5,6,7]
# s = []

# for i in n:
#     s.append(i*i)

# print(s)

# ls= [n for n in range(5)]

# print(ls)

# lis = [n*2 for n in range(5)]
# print(lis)

# fa_lang_char_upper = [letter.upper() for  letter in "MuhammadUsman"]
# print(fa_lang_char_upper)

# lists = ["usman","ali","ahmed","majid","bakar khan hussain","mirza khurram","will you m"]
# l = []

# for i in lists:
#     if "h" in i:
#         l.append(i)
# print(l)

# class Computer:

#     def __init__(self):
#         self.__maxprice = 900
    
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
    
#     def setMaxPrice(self,price):
#         self.__maxprice = price
# c = Computer()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxPrice(1000)
# c.sell()


# class Polygon:
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     def render(self):
#         print("Rendering Circle...")

# s1 = Square()
# s1.render()

# c1 = Circle()
# c1.render()

# a= {
#     "name":"usman",
#     "age":24,
#     "city":"Rawalpindi"
# }
# # a["color"]= "blue"
# # a.update({"color":"red"})

# print(a)


# num = 21
# p = num

# lis= []
# sum1 = 0
# while(num>0):
#     x=num%10
#     lis.append(x)
#     print(lis)
#     num= num//10
# sum1 = sum(lis)
# print(sum1)
# if (p%sum1==0):
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")

# def printDivisors(n, factors) :
#     i = 1
#     while i <= n :
#         if (n % i==0) :
#             factors.append(i)
#         i = i + 1
#     return sum(factors) - n



# if __name__ == "__main__": 
#   number1, number2 = 6, 28
#   if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
#     print("Friendly pair")
#   else:
#     print("Not a Friendly Pair")


# class Parent():
#     def show(self):
#         print("Inside parent")

# class Child(Parent):
#     def show(self):
#        Parent.show(self)
#        print("INSIDE CHILD")

# obj = Child()
# obj.show()


# myList = [
# 	{
# 		'first name':"muhammad",
# 		'last name':"usman"
# 	},
# 	{
# 		'age':24,
# 		'mobile':"vivo"
# 	},
# 	{
# 		'Height':5.9,
# 		'weight':55
# 	}
# ]

# myList.append({"color":"red"})
# print(type(myList))
# j=[]
# for i in myList:
#     print(i)



# mydict = {
#     "Name":{
#         "first name":"M",
#         "last name":"usman"
#     },
#     "Dob":{
#         "dob" :5-26-1999,
#         "age":24
#     },
#     "personal":{
#         "Height":5.9,
#         "Weight":55
#     },
# }

# # del mydict
# print(mydict)

# u = [
#    [
#         'usman','ali','hamza'
#     ],
#    [
#         1,2,3
#     ]
# ]

# u.append(a)
# print(u)


# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive!") 

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model = model
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza","Touring 20")
# plane1 = Plane("Boeing","747")

# for x in (car1,boat1,plane1):
#     x.move()


# myDict = {
# 	'foo': {
# 		'a':10,
# 		'b':11
# 	},
# 	'bar': {
# 		'c':12,
# 		'd':13
# 	},
# 	'moo': {
# 		'e':14,
# 		'f':15
# 	},
# }

# print(myDict['moo']['f'])
# print(myDict['bar']['d'])

# Function to take multiple arguments
# def sum_number(*args):
    # variable to store the sum of numbers    
    # result = 0
    
    # accessing the arguments
    # for num in args:
    #     result += num
    
    # Output
    # print("Sum : ", result)

    
# Driver Code
# if(__name__ == "__main__"):
#     print("Similar to Method Overloading\n")
#     print("Single Argument    ->", end = " ")
#     sum_number(10)

#     print("Two Arguments      ->", end = " ")
#     sum_number(30, 2)

#     print("Multiple Arguments ->", end = " ")
#     sum_number(1, 2, 3, 4, 5)
# import abc
# from abc import ABC, abstractmethod    
# class Color(ABC):
#     @abstractmethod
#     def print_color(self):
#         pass
# class Red(Color):
#     def print_color(self):
#         print()




# l=[{'value': 'apple', 'blah': 2}, 
#  {'value': 'banana', 'blah': 3} , 
#  {'value': 'cars', 'blah': 4}]

# [d['value'] for d in l]
# [d['value'] for d in a if 'value' in d]

# print(d)


# data = [
#     {"claim_number": "TX1048-22024-C639", "total_paid": 278.29, "card_paid": 228.29},
#     {"claim_number": "TX1048-22086-C647", "total_paid": 161.81, "card_paid": 261.81},
#     {"claim_number": "TX1048-22081-C648", "total_paid": 261.81, "card_paid": 386.81},
#     {"claim_number": "TX1048-22024-C639", "total_paid": 318.29, "card_paid": 468.29},
#     {"claim_number": "TX1048-22081-C648", "total_paid": 318.29, "card_paid": 418.29},
#     {"claim_number": "TX1048-22086-C647", "total_paid": 0.0,    "card_paid": 10.0},
#     {"claim_number": "TX1048-22024-C639", "total_paid": 10.0,   "card_paid": 20.0}
# ]




# tempJson = {}
# finalList = []

# for eachScopeJson in data:
#     if eachScopeJson['claim_number'] in tempJson:
#         tempJson[eachScopeJson['claim_number']]['total_paid'] = tempJson[eachScopeJson['claim_number']]['total_paid'] + eachScopeJson['total_paid']
#         tempJson[eachScopeJson['claim_number']]['card_paid'] = tempJson[eachScopeJson['claim_number']]['card_paid'] + eachScopeJson['card_paid']
#     else:
#         tempJson[eachScopeJson['claim_number']]['claim_number'] = {}
#         tempJson[eachScopeJson['claim_number']]['total_paid'] = 0 + eachScopeJson['total_paid']
#         tempJson[eachScopeJson['claim_number']]['card_paid'] = 0 + eachScopeJson['card_paid']
#         tempJson[eachScopeJson['claim_number']]['difference']= eachScopeJson['total_paid'] - eachScopeJson['card_paid']


# for eachKey in tempJson:
#     finalList.append({'claim_number':eachKey,'total_paid':tempJson[eachKey]['total_paid'],'card_paid':tempJson[eachKey]['card_paid']})


# print (tempJson)

