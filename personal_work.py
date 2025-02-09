user_float = float(input("please enter a float"))
print(type(user_float))
print(user_float)

x =int(input("please enter an interger"))
a = x + 10
print(a)


########## Functions 

def function_name():
    print(2+2)

function_name()    # A parameter is placeholder or variable that you want your python code to run on

def function_name(parameter):   #when you create a parameter, it goes inside the parathesis where you define the function
    print(parameter + 2)

function_name(8)     #when the function is called, the values that you pass in it are called arguments



first_str = "the number "

def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)

function_name(first_str,  5, " is an integer")    #here the first argument is a variable, the 2nd is an interger and the 3rd is a string but we concatenated all to a string 


def default_example(num1=7, num2=8):   #when a default value is called as parameters, the default values are called as the arguments
    print(num1 * num2)
    print(num1 * num2) 
default_example()    #56

def default_example(num1=7, num2=8):   #when a default value is called as parameters, the default values are called as the arguments
    print(num1 * num2) 

default_example(4, 6)    # 24 but if an argument is passed explictly, the argument values are called 


def default_example(num1=7, num2=8):   #when a default value is called as parameters, the default values are called as the arguments
    print(2 * num2)          #when a value is passed explictly for the first parameter, that value is called rather than the default value 

default_example()    #16



############# Return

def default_example(num1=7, num2=8):   
    return num1 * num2        #print function does not return anything you can use, only return can be used to work with the output in your argument

print(default_example() + 44) #100

def hello_world_printer():   #since no parameter was passed, and no argument was explicitly called the code ran in the print would hold
    print("hello world")

hello_world_printer()   


name = input("please enter your name. ")

def name_printer(hp):
    print(hp)

name_printer(name)



l = int(input("what is the length of the prism? "))
w = int(input("what is the width of the prism? "))
h = int(input("what is the height of the prism? "))


def volume(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is", str(volume(l, w, h)), "cubic feet. ")   #750 cubic feet


C = int(input("what is the temperature in celsius? "))           #Steps: set your varaible, define your function, return the function and print your output

def fahrenheit(C):
    return 1.8 * C + 32


print("The Fahrenheit equivalent of ", C, "degrees celsius " "is", str(fahrenheit(C)))