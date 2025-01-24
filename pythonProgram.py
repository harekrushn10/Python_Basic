## '#' is used to comment anything in python
# #------------------------------------------------------------------ Variable---------------------------------------------------------------------
# name = "hari"
# age = 21
# print(name)
# print(age)

# # Override variable
# name = "harekrushn"
# # Float datatype
# age = 20.0

# # Boolean datta type
# is_adult = False

# print(name)
# print(age)
# # ------------------------------------------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------ exercise -----------------------------------------------------------------------

# fname = "Tony "
# lname = "Stark"
# # Concat String
# name = fname + lname
# age = 51
# print(name)
# print(age)

# is_genius = True
# # For print multiple thing with varible
# print(f"{name} is genius.")
# print(is_genius)

# # ------------------------------------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------User input-----------------------------------------------------------------------

# name = input("What is your name? ")
# print("Hello " +name)

# # ------------------------------------------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------- exercise ----------------------------------------------------------------------

# sname = input("Tony , What is your superhero name? ")
# print("your superhero name is "+sname)

# # ------------------------------------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------Type conversion--------------------------------------------------------------------
# this code prints new age by adding 2 in entered age
# Old_age = input("Enter your old age: ")
# new_Age = int(Old_age) + 2
# print(new_Age)

# num = 18
# print(float(num))
# print(str(num))
# print(bool(num))

# # ------------------------------------------------------------------------------------------------------------------------------------------------
# # ------------------------------------------------------------Code for sum of two number ---------------------------------------------------------

# n1 = input("Enter first number : ")
# n2 = input("Enter second number : ")

# add = int(n1) + int(n2)
# print("The sum is: "+ str(add)) 

# # ----------------------------------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------python String-------------------------------------------------------------------

# name = "Tony Stark"
# print(name.upper())   # .Upper() method is converts whole string in Upper case
# print(name.lower())   # .lower() method is converts whole string in lower case
# print(name)

# print(name.find('S')) # .find() method is find particular index and prints index of it 
# print(name.find('stark'))  # This print -1 because of in Stark we find for small 's'.

# print(name.replace("Tony Stark", "Ironman"))  # This methood only replace fiven name with declared once not permenantly 
# print(name) # It prints "Tony Stark" declared once is not change by relace method 

# print(name.replace("T","M"))

# # -----------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------keywords => print , input etc....----------------------------------------------------------

# name = "Tony Stark"  #Text
# print("T" in name) # in function returns True or false based on there is present which we want to find or not 

# # -------------------------------------------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------Arithmetic Operators (+,-,*,/,%,//,**)------------------------------------------------------------
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) #It print only integer value rather than decimal value
# print(a%b) # prints reminder
# print(a**b) # print power of a given by b

# # Shortcuts

# i = 5 
# i = i +2
# i += 2
# i -= 2
# i *= 2 

# #-------------------------------------------------------------------------------------------------------------------------------------------------
# #---------------------------------------------------Operator Precendence in Python  [1st(* & /) ,2nd( + & -)]----------------------------------------------------

# result = 2 + 3 * 5
# print(result)   # 17     

# result = 2 + 3 / 5
# print(result)   #2.6

# result = 2 - 3 * 5
# print(result)   #-13

# result = 2 - 3 / 5
# print(result)   #1.4 

# #---------------------------------------------------------------------------------------------------------------------------------------------------
# # ------------------------------------------------------Comparison operator (< , > , <= , >= , == , !=)----------------------------------------------------

# print(3 < 2) #False => less then
# print(3 > 2) #True  => grater than
# print(3 <= 2) #False => less than equal to
# print(3 >= 2) #True =>greater than equal to
# print(3 == 2) #False => equal to
# print(3 != 2) #True => Not equal to

# # -------------------------------------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------Logical operator(or , and , not)-------------------------------------------------------------

# print(2>3 or 2>1)  #True => if one of the condition is true then true otherwise it false
# print(1>2 or 0>1) #False
# print(2>3 and 3>1) #False
# print(3>2 and  4>1) #True => Both true then and then only true otherwise false
# print(not 2>3) #True
# print(not 3>2) #False  => this will Reverse the condition and then it will print

# #-----------------------------------------------------------------------------------------------------------------------------------------------
# #---------------------------------------------------------------if-else Statements-----------------------------------------------------------------

# age = int(input("Enter age :"))
# if age >=18 :
#     print("You are and adult.")
#     print("You can vote.")
# elif age<18 and age>3:
#     print("You are in school.")
# else:
#     print("You are a child..")

# print("Thank you!")

# #----------------------------------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------range() in python-----------------------------------------------------------------

# number = range(5)  #it prents sequence of list
# print(number)  

# #----------------------------------------------------------------------------------------------------------------------------------------------
# #----------------------------------------------------------------While loop in python --------------------------------------------------------------
# n =1
# while(n<=100):
#     print(n)
#     n = n + 1

# # pattern

# n = 1 
# while(n<=5):
#     print(n * "*")
#     n = n+1 

# # reversee patern

# n=5 
# while(n>=0):
#     print(n * "*")
#     n = n-1

# # ------------------------------------------------------------------------------------------------------------------------------------------------
# # --------------------------------------------------------------For loop in python---------------------------------------------------------------------

# for i in range(5):
#     print(i+1)

# # Pattern using for loop
# for i in range(5):
#     print(i*"*")

# # -------------------------------------------------------------------------------------------------------------------------------------------------
# #---------------------------------------------------------------List=[] in python---------------------------------------------------------------------

# marks = [59,65,78,63,21,"maths"]
# marks = [59,65,78,63,21]
# print(marks) #print the given list
# print(marks[1]) # for particular indexing access
# print(marks[-1]) # for prenting from lasr
# print(marks[::-1]) # reverse the list

# # -------------------------------------------------------------------------------------------------------------------------------------------------
# #---------------------------------------------------------------slicing in list---------------------------------------------------------------------

# print(marks[0:2]) # for printing particular range  of index => op :[59,65]

# for score in marks:
#     print(score)

# marks.append(99) # .append() is used for adding and element at the last in list
# print(marks)   

# marks.insert(0,90) # .insert( index, num) is used for add an element at particular index in the list
# print(marks)

# print(99 in marks)

# print(len(marks)) #len dunction used to find the length of given list

# # using while loop print the number of list

# i = 0 
# while i<len(marks):
#     print(marks[i])
#     i = i +1

# marks.clear() #clear function is used for clear the list
# print(marks)

# # ----------------------------------------------------------------------------------------------------------------------------------------------
# #-------------------------------------------------------------- Break keyword in list---------------------------------------------------------------

# students = ["ram", "shyam", "kishan", "radha", "radhika"]
# for student in students :
#     if student == "radha":
#         break
#     print(student)

# print("---------------------------------------------")

# for student in students:
#     if student == "kishan":
#         continue
#     print(student)


# # -----------------------------------------------------------------------------------------------------------------------------------------------
# #--------------------------------------------------------------Tuple()=> in python-------------------------------------------------------------------
# # Tuple is imutable means cant change after creation

# marks =(95,98,97,97,97,97)
# print(marks)
# print(marks.count(97)) # op:4 it counts the particular element is how much time in the given tuple

# print(marks.index(97)) # return index of particular element in tuple

# #------------------------------------------------------------------------------------------------------------------------------------------------
# #-----------------------------------------------------------Sets{}: in python => unorderd-----------------------------------------------------------

# marks = {95,98,97,97,97}
# print(marks)

# for score in marks:
#     print(score)

# #------------------------------------------------------------------------------------------------------------------------------------------------
# #-------------------------------------------------------- Dictionary in python (key : value ) pair-------------------------------------------------------

# marks = {"english" : 95 , "chemistry" : 98}
# print(marks["chemistry"])

# marks["Physics"] = 97 # ad value of physics in dictinary
# print(marks)

# marks["Physics"] = 99  # => update value of physics in dictionary
# print(marks)

# # -----------------------------------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------Functions in python--------------------------------------------------------------------
# # 1) In_Built Functions
# # 2) Module Function
# # 3) User-Defined Function

# import math 
# print(dir(math)) # for print all the functin of math module

# from math import *
# print(sqrt(4))

# import math 
# print(math.sqrt(4))

# def print_sum(n1,n2):
#     print(n1+n2)

# print_sum(1,2)

# n1 = int(input("enter the value :"))
# n2 = int(input("enter the value :"))
# print_sum(n1,n2)

def print_sum(n1,n2=4):
    print(n1+n2)

print_sum(1)