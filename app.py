#print("Hello world!")


#variables in python
#name="sabin"
#print("Hello"  +  name)
#print(type(name))



# age="21"
# age=age+"2"
# print(type(age))
# print(age)

#boolen
# human=False
# print("Are you a human  "+str(human))

#Sum of the two given number
# num1=float(input("Enter the first number"))
# num2=float(input("Enter the second number"))
# sum_result=num1+num2
# print(f"sum:{num1}+{num2}={sum_result}")


#find the division of two number

# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))
# if(num1<num2):
#     print('please provide numerator is greater than denomenator')
# else:
#     div_result=num1/num2
#     print("The division of two number is :",div_result)


#multiple assignment=allows us to assign multiple variables at the same time

# name="Bro"
# age=25
# attractive=True

# name,age,attractive="bro",21,True


# print(name)
# print(age)
# print(attractive)

#name="hello Bro"
#print(len(name))
#print(name.find("o"))
#print(name.capitalize())
#print(name.upper())



#type Casting=Convert the data type of a value to another data type

# x=1
# y=2.0
# z='3'
# x=str(x)
# print(x*3)
# print(y)
# print(z)


# x="sabin"
# x=2
# print(x)


# x=y=z="Nepal"
# print(x)
# print(y)
# print(z)

# fruits=["apple" , "banana" , "orange"]
# x,y,z=fruits
# print(x)
# print(y)


# x="python "
# y="is "
# z="popular"
# print(x+y+z)

# x="2"
# y='3'
# print(x+y)

#global variables
# x="python"
# def mufunc():
   
#     print("best programming language" + x)
# mufunc()  

# x='awesome'
# def myfunc():
#     x="fantastic"
#     print("python is" + x)
# myfunc()

# print("python is " + x)


#global keyword
# x="awesome"
# def mufunc():
#     global x
#    # x="fantastic"
# mufunc()
# print("python is " + x)


#datatype in python
# x=5
# print(type(x))

# x = ("apple", "banana", "cherry")
# print(type(x))


# import random
# print(random.randrange(1,10))

#multiline string
# x="""lfjdsflkafklajdfsajlksajfkaslfjsaf
# sfdksalksajfklsadjflsaf
# fksajfklsajflasd
# fklsafjladfjsalfsa"""
# print(x)

#strings are arrays
# a="Hello world!"
# print(a[1])


# for x in "banana":
#     print(x)

# a="hello world sajfkdjfks"
# print(len(a))

# txt="The best things in life are free!"
# print("expensive" not in txt)

# b="Hello world"
# print(b[2:5])



#insert into array
# list=[]
# list.insert(0,"nabin")
# print(list)


# append
# list=["apple" , "banana" ,"orange"]
# list.append("abc")
# print(list)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i=0
# while i< len(thislist):
#     print(thislist[i])
#     i=i+1
# thislist = ["apple", "banana", "cherry"]
# newlist=[]
# for x in thislist:
#     if "a" in x:
#         newlist.append(x)
#     print(newlist)

# def my_funcation(fname,lname):
#     print(fname + " Hello iam function " +lname)
# my_funcation("Email","data")

def my_funcation(child3, child2, child1):
    print("The younges child is:"+ child2)
my_funcation(child1="sarthak", child2="Suman", child3="Linux")

