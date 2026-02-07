# Python Basics ####################################################################################################

# What is your name! print your name!
# Only use one print function
print("Abhi")

# define variables named as with values: mukesh=7, z=6, rohan=5, longitude=4
mukesh = 7
z = 6
rohan = 5
longitude = 4

# print required variable
# output - 5
print(rohan)

# Declaring Variable ###############################################################################################

# declare 4 variables with values as: ur_age 21,ur_weight 50.6, ur_first_name = 'Mukesh',ur_last_name = "Manral"
ur_age = 21
ur_weight = 50.6
ur_first_name = 'Mukesh'
ur_last_name = "Manral"


# Data Type (types of variabls #
## print type of ur_age,ur_weight,ur_first_name,ur_last_name variables
print(type(ur_age))
print(type(ur_weight))
print(type(ur_first_name))
print(type(ur_last_name)) 

# print values of ur_age,ur_weight,ur_first_name,ur_last_name variables
print(ur_age)
print(ur_weight)
print(ur_first_name)
print(ur_last_name)

# make 2 variables with values as: ur_first_name 'Mukesh',ur_last_name'Mukesh'
ur_first_name = 'Mukesh'
ur_last_name = 'Mukesh'

# make a variable TrueOrFalse which will have comparison of variables ur_last_name == ur_first_name
TrueOrFalse = ur_last_name == ur_first_name
print(TrueOrFalse)

# define a variable name "x" and assign value 777 and print it
x = 777
print(x)

# Initialize variables [x,y,z,zz] with values
## x as 7 =>int ,
## y as 77 =>int,
## z as 77.7 => float,
## zz as 'Hi' => string

x = 7
y = 77
z = 77.7
zz = 'Hi'

# Arithmetic Operators #

# add x and z
print(x + z)

# subtract z and y
print(z - y)

# Multiply x and z
print(x * z)

# Exponent (raise the power or times) x times z
print(x ** z)

# division on x and z
print(x / z)

# floor division(ignores decimal) on x and z (gives quotient)
print(x // z)

# Modulo(gives remainder) on x and z
print(x % z)

# Comparison Operators #

# comapre and see if x is less then z
# can use '<' symbol
print(x < z)

# check the type of above comaprison where it says comapre and see if x is less then z
print(type(x < z))

# comapre and see if x equall to z
# can use '==' symbol
print(x == z)

# comapre and see if x is greater than z
# can use '>' symbol
print(x > z)

# comapre and see if x is greater than or equall to z
# can use '>=' symbol
print(x >= z)

# comapre and see if x is Not equall to z
# can use '!=' symbol
print(x != z)

# Logical Operators #

# compare if 108 is equall to 108, 21 is equall to 21 using logical and
# equall to => '=='
# logical and => and

# in and both condition must be True to get a True
print((108 == 108) and (21 == 21))

# how above condition can give False as output show all those conditions
print((108 == 108) and (21 == 22))
print((108 == 999) and (21 == 21))
print((108 == 999) and (21 == 777))

# compare if 108 is equall to 108, 21 is equall to 11 using logical or
# equall to => '=='
# logical or => or

# in or Only one condition need to be True to get a True
print ((108 == 108) or (21 == 11))

# this is for you to understand it
(108 == 108) or (21 == 11) or (108 <= 11)

####################################################################################################################

# if --- else => to handle single condition
# if --- elif --- else => to handle multiple condition

# make variable with value as : money 100000
money = 100000

# see output of money > 2000
print(money > 2000)

# assign money variable value of 10000
##### say you have this much ammount in your account
money = 10000

# start of if condition
# if money is greater then 1000 which is data science course free
# if money > 1000 is false i.e. you have less money then 1000 in your account then else will work for now only if is working

if money > 1000:
  print("You Have Sufficient Balance!")
else:
  print("Sorry, Insufficient Balance! Maybe Next Time")

###########################################################################

# take a test_score variable with 80 in it.
test_score = 80

# if test_score greater then 80 then print A grade
# elif test_score greater then 60 and less then 80 print B grade
# else print Nothing for you

if test_score >= 80:
  print("A grade")
elif test_score > 60 and test_score < 80:
  print("B grade")
else:
  print("Nothing for you")

####################################################################################################################

# Python Loops #

for iterating_variable in range(10):
    print(iterating_variable)

# print 'I love sports' 10 times using for loop
for i in range(10):
    print("I love sports")

# while loop
# save 0 in variable number
number = 0

# print till 10 using while loop
while number < 10:
  print(number)
  number = number + 1


# Type of Jump Statements #

#Break Statement #

# example that uses break statement in a for loop
# take range(10) and print 'The number is' + value
# break when num equals 5

for num in range(10):
  if num == 5:
        break
  print("The number is", num)


# Using same `for loop program` as in Break Statement section above
# Use a continue statement rather than a break statement
# take range(10) and print 'The number is' + value
# continue when num equals 5

for num in range(10):
  if num == 5:
    continue
  print("The number is", num)


# String Manipulation #

# define a string variable with "We are creating next generation data science eco-system at CollegeRanker"
sentence = "We are creating next generation data science eco-system at CollegeRanker"

# Find length of string including spaces
print(len(sentence))

# Access characters in a string with indexing i.e string[0]
print(sentence[0])

# Access characters with negative indexing i.e string[-1]
print(sentence[-1])

# String Slicing #

# select string from first to 6th element i.e string[:6]
print(sentence[:6])

# select string from 7th to negative 10th element i.e string[7:-10]
print(sentence[7:-10])

# Count of a particular character in a string
print(sentence.count('o'))

# Count of a particular sub-string in a string
print(sentence.find('data'))

# Find a substring in string using find and index function
# .find() => if present it will return starting index, not found then it will return -1
print(sentence.find('generation'))

# .index() => if present it will return starting index, not found then it will give error
print(sentence.index('generation'))

### Checking whether string `startswith` or `endswith` a particular substring or not
print(sentence.startswith('We'))
print(sentence.endswith('creating'))

### Converting string to upper case ###
print(sentence.upper())

### Converting only first character of string to upper case
print(sentence.capitalize())

### Checking if string is in lower case or upper case
print(sentence.islower())
print(sentence.isupper())

### Checking if string is digit, alpabetic, alpha-numeric
print(sentence.isdigit())
print(sentence.isalpha())
print(sentence.isalnum())

# assign "C++ is easy to learn" to a new_str variable
new_str = "C++ is easy to learn"

### Replace C++ with Python
new_str = new_str.replace("C++", "Python")
print(new_str)

### Use Split function on new_str ###
print(new_str.split())

# Python Functions ################################################################################################

# define a function with welcome_message(name) and body 'Welcome to Functions !!!'
def welcome_message(name):
  print(f"Hello {name},Welcome to Functions !!!")

# call a function with your name
welcome_message("Ranchoor Das Chanchar")

# Write a function to add two number which are as 3 and 4
# in total variable store adition of 3 + 4
# print total variable
def add_numbers(a, b):
  total = a + b
  print(total)

add_numbers(3, 4)

# Positional Arguments #

## Create substraction_function(small_number,large_number) and return difference between large_number and small_number
def substraction_function(small_number, large_number):
  return large_number - small_number

# always pass arguments using there name(keyword arguments) then order does not matter
print(substraction_function(large_number=93, small_number=24))

# Scope of Variables means that part of program where we can access particular variable ############################

#### Observe every output from here onwords #####
# defining a global variable
global_variable = str(input('Write Something Here: '))

def random_function(value):
    # accessing variable which is outside of this function
    return value

print(random_function(global_variable))

# => Let's see what will happen if we try to change value of global variable from Inside of the Function

#### Observe every output from here onwords #####
# defining a global variable
global_variable2 = 'variable outside of function'

# defining function
def random_function():
    # changing value of global variable from inside of the function
    global_variable2 = 'changing variable outside of function from inside of function'
    # accessing variable which is outside of this function
    return global_variable2

print(random_function())
print(global_variable2)



