# function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def add(a, b):
    return a + b    
print(add(5, 3))

function_list = [greet, add]
for func in function_list:
    if func == greet:
        print(func("Bob"))
    elif func == add:
        print(func(10, 20))

# INBBUILT FUNCTIONS
print("Maximum mark:", max(mark))
print("Minimum mark:", min(mark))
print("Sum of marks:", sum(mark))   
# MODULES FUNCTIONS
import math
import random
print("Random mark:", random.choice(mark))
print("Square root of 16:", math.sqrt(16))