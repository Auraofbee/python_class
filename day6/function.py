# def add(a, b):
#     print("sum : ", a + b)

# add(10, 20)
# add(30, 50)

# def greet(name="guest"):
#     print(f"hello, {name}!")

# greet("benny")


# def student_details(name, age):
#     print(f"Name: {name}, Age: {age}")

# student_details(age=30, name="Benny")

#Arbitary arguments (*args and **kwargs)



# def sum_numbers(*numbers):
#     total = sum(numbers)
#     print("sum :", total)

# sum_numbers(1, 2, 3, 4, 5)

counter = 0 #Global variable

def update_counter():
    global counter
    counter =counter + 1
    print("Counter ", counter)

update_counter()
update_counter()
update_counter()
update_counter()