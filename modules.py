## Modules Import 

import random # the random modules is used to import random integers or random floats

print(random.randint(1, 10))   # this module randomly gives you integers between the values in the parenthesis. you must call the module put a period. and the function randint

#### Functions Import

from random import randint    #To import a function, you must type the name of the module the function is being imported from and "from" the name of the function you want to import

print(randint(10,20))    #to run a function within a module, you dont't need to call the module with a period. before running the function


##### Universal Import
from random import *    # to run a universal import, you type "from" the name of the module you want to import and "import" wildcard * , meaning you want to import all the functions that exists within that module.

print(random())  # the random function within the random Module outputs floats thas = 0.0 AND LESS THAN 1.0 when it is called

import random
from random import randint
fuel= randint(10, 25)  #No of gallons of gas that the car's fuel tank holds
miles = randint(200, 400) #miles that the car can travel on a full tank

#MPG = miles per gallon
print("the car can travel ", str(miles // fuel), "miles per gallon. ")
print("the car's fuel tank can hold ", str(fuel), "gallons. ")
print("the car can travel ", str(miles), "miles on a full tank. ")


############### Variable scope

example = "hello world"     # This is a global scope variable

def loc_ex():
    example = "this is a string"  # this is a local scope variable
    return example   ## this would return the value within the local scope

print(example)
print(loc_ex())


###Local variables cannot be used by codes in the global scope
breakfast = "pancakes"    #global vaiable


def loc_ex():
    breakfast = "waffles"
    return breakfast

loc_ex()
print(breakfast)      # without breakfast being defined globally as pancakes, the code would break with error message "breakfast is not defined" 


##Global variables can be accessed by codes in the local scope

def print_glob():
    loc_var = "that is very long. "
    print(glob_var + loc_var)

glob_var = 'This is a string '         # this is a global variable but it was accessed by the code print(glob_var + loc_var) within the local scope

print_glob()


##The local scope of one function cant use variables from another function's local scope

def first():
    loc = 2
    return loc     #after a return statement is declared, the variable within this local scope is destroyed

def second():
    return loc      # As a result cannot be utilized within this local scope


first()
second()           # No output can be expected here as loc was never defined within the 2nd function which is a different local scope from the First.


#You can used the same name for different variables as long as they are in different scopes

def loc_ex1():
    fruits = "banana"       # this is a local scope as it exists under a function
    print(fruits)

def loc_ex2():
    fruits = "orange"
    print(fruits)          # this is a local scope as it exists under a function

fruits = "apple"          # this is a global variable as it is indented where the def is also indented 

loc_ex1()
loc_ex2()
print(fruits)

#Global statement 

def loc_ex1():
    global fruits        #this is a global statement that assigns the fruits within a local scope a global identity, thus it can displace the variable used in a global scope
    fruits = "orange"
    print(fruits)          # this is a local scope as it exists under a function

fruits = "apple" # this is a global variable as it is indented where the def is also indented 
loc_ex1()
print(fruits)


words = "hello world"

def hi_world():
    return words

print(hi_world())   #it printed "hello world" because global variables can be accessed by codes within a local scope 


def p1_returner():
    approx = 3.144
    return approx
  
print(p1_returner())    # It would print 3.1444
     

def float_holder():
    flo = 21.9
    return flo

float_holder()
print(flo)       # It would result in an error message because flo is not defined globally here

