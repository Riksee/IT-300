import sys
import random
import platform

x= platform.system()
print(x)

# #do not print this

# print(sys.version)

# print("hello world"); 
# learn = "aprende"
# type = type(learn)
# print(learn)
# print(type)

# #this is how to assign multiple variables

# first, then = "fragrance","fire"
# print(first, then)

# praise = worship = "weapon"
# print(praise, worship)

# #this is called UNPACKING
# weapon = ("fragrance", "fire")
# first, then = weapon
# print(first, then)

# #now, global variables
# name = "Victoria " #This is a global variable
# lastName = "Adedire"

# def fullName():
#     name = "Iyanuoluwa " #This is a local variable
#     print(name + lastName)

# fullName()

# print(name+lastName)

# #to use global keyword to create global variable inside of a function
# name = "victoria"

# def allName():
#     global name
#     name = "Iyanuoluwa"

# allName()

# print(name)

# #to create and print random numbers
# x = random.randrange(1,20)


# if x is 6:
#     print("True")
# else:
#     print("False")

# print(x)




# #to assign multiline strings to a single variable
# name = """#Victoria
# Iyanuoluwa
# Adedire"""
# print(name)

# #To loop through a string
# name = "Adedire Victoria Iyanuoluwa"

# for x in name:
#     print(x)

# #to check if a particular phrase of char is in a string
# print ("Vic" in name)

# name = "VICTORIA"
# print(name[0:3].upper())
# name = name.casefold() #converts a sting to lowercase
# print(name.center(10)) #to create a string of 15 charcaters with the string in the center
# print(name.count("i")) #to count the number of times a character appears in a string
# print(name.encode())

# #let's try formatting
# name = "Vee"
# age = 23
# intro = "My name is " + name + f". I am {age}"
# print(intro)

# #let's use escape characters
# txt = "He is a \"good\" person."
# print(txt)

#let's test boolean
print(10>9)
print(bool("Victoria"))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 5
x ^= 3
print(x)

