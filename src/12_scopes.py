# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
## insert the line 
## global x
## indicating that the local varible is global in scope
print(x)


# This nested function has a similar problem.

# def outer():
#     y = 120
#     def inner():
#         #nonlocal y
#         y = 999
        
#         print(y)
#     inner()
#     print(y)
    
# outer()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?

    ### add in the "nonlocal y" line AND make sure you're running Python 3!!!
    # Note: Google "python nested function scope".


def outer():
    y = 120
    def inner():
        nonlocal y
        y = 999
        
        print(y)
    inner()
    print(y)
    
outer()



