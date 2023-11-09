# Minimum for a function 

def f():
    pass

# Function with parameters

def f(num):
    pass

# Function with parameters and return value

def f(num):
    return num

# Function with unlimted parameters

def f(*args):
    return args

print(f(1,2,3,4,5))

# Function with unlimited key-value parameters

def f(**kwargs):
    return kwargs

print(f(a=1,b=2,c=3))

# Function with everything together

def f(num, *args, **kwargs):
    return num, args, kwargs

# Function which makes sense and uses some of the concepts
## exercise: Create a function named `summe` which takes in unlimited parameters and returns their sum

def summe(*args):
    return sum(args)


# A function within a class is called a method
# class called Laptop
class Laptop:
    # konstruktor which doesn't accept any arguments
    def __init__(self):
        pass
    
    # method called `start_vs_code`
    def start_vs_code(self):
        print("Starting VS Code")
        
