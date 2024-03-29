from enum import Enum



class State(Enum):#creating a variable called State.INACTIVE = 0 or State.ACTIVE = 1
  INACTIVE = 0
  ACTIVE = 1
  #reference using 
print(State.INACTIVE.value)#or
print(State(1))


#GLOBAL COMMANDS
    #sorted() - print(sorted(variable_example))

#INPUTS
how_old = input('How old are you?')
print('You are ' + how_old)
  
#CONTROL STATEMENTS
    #are like if statements
    



name = 'Trottie'
age = 40

print(name)



# for, if, while, import are keywords that have specific meaning

# DATA TYPES

print(type(name) == str) #boolean
print(isinstance(name, str)) # checks to see if the NAME is an INSTANCE of a STR

print()
age = 2
print(isinstance(age, int))
print(isinstance(age, float))

# can use CLASS CONSTRUCTORS to change output of a value

# class constructor :
# float() 
# int() 

# complex() for complex numbers
num1 = 2+3j
num2 = complex(2,3)

print(num2.real, num2.imag)

#LIST() + IN operator
dog = ['string', 27, "strings", True] # - group together common values like an ARRAY IN JS
print("strings" in dog)

dogss = ["butch", 24, 35, "checkers"]
dogss.append("wolf")# SAME AS *PUSH IN JS AND *POP = REMOVE, SHIFT? & UNSHIFT?
print(dogss)

dogss = ["butch", 24, 35, "checkers"]
dogss.remove(24)
print(dogss)

dogss = ["butch", 24, 35, "checkers"]
dogss.insert(2, "hello")
print(dogss)

dogss = ["butch", 24, 35, "checkers"]
dogss[1:1] = ["hola", 20]#WHEN USING SLICES USE BRACKERS INSTEAD
print(dogss)

itemss = ["apple", 'orange', 'bananna', 'grapes', 'pear']#only can use sort to arrange same type only
itemss.sort()
print(itemss)


# bool() for booleans





# tuple() for tuples - objects that can't be modified - grab values by using indexing
list_names = ('Roger', 'Alex', 'Adam')
list_names[-1]
list_names.index('Adam')
len(list_names)
print('Roger' in list_names)



# range() for ranges
# dict() for dictionaries - allow you to create key value pairs - name= 'roger'
dog = { 'name': 'adam', 'age': 29}
dog['name'] = 'trottie'
#print(dog.get())
print(dog.pop('name'))#popitem - retreive and remove last item
#dog.keys(), values, items*converts to a list, len, del dog['color]




# set() for sets - immutable can be changed * CAN CONVERT TO A *LIST and CANNOT HAVE 2 OF SAME SET
#AND CAN USE COMPARE OPERATORS
namename1 = {'rog', 'adam'}
namename2 = {'adams'}

mod = namename1 | namename2
print(mod)#{'rog'}




ages = float(40)

number = "20" #CALLED CASTING - Extract a integer from a string
aging = int(number)
print(isinstance(aging, int))

#GLOBAL OPERATORS
    # in = checks if letters are in variable test
    # len = checks length
test = 'this is a test string'
print('tha' in test) # 

#STRING METHODS
    # is = to check

print('trottie'.upper())
print('trottie'.lower())
print('trottie'.title()) #to get a capitalized version of a string
print('trottie'.isalpha()) #to check if a string contains only characters and is not empty
print('trottie'.isalnum()) #to check if a string contains characters or digits and is not empty
print('trottie'.isdecimal()) #to check if a string contains digits and is not empty
print('trottie'.lower()) #to get a lowercase version of a string
print('trottie'.islower()) #to check if a string is lowercase
print('trottie'.isupper()) #to check if a string is uppercase
print('trottie'.upper()) #to get a uppercase version of a string
#print('trottie'.startswith()) #to check if a string starts with a specific substring
#print('trottie'.endswith()) #to check if a string ends with a specific substring
#print('trottie'.replace()) #to replace a part of a string
#print('trottie'.split()) #to split a string on a specific character seperator
#print('trottie'.strip()) #to trim the whitespace from a string
#print('trottie'.join()) #to append new letters to a string
#print('trottie'.find()) #to find the position of a substring

#STRING CHAR AND SLICING
names = 'trottie is going to accomplish something great'
print(names[:])#start and end indicies

#FUNCTIONS

def hello(name='mctrotto'):#can make a default arg if don't specify when we call at the bottom example
  print('Hello ' + name)
hello('Trot')#must call in order to print
hello()

def hello(name, age):
  print('Hello ' + name + ', you are ' + str(age))
hello('Trot')#must call in order to print
hello()
