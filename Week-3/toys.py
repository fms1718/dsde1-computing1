'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    ans = a
    new_ans = int(ans)
    print(new_ans+1)
    return new_ans + 1 

user_input = input("input something")
user_input = int(user_input)
answer_2 = inc(user_input)
a = user_input
print(answer_2)

# write a function that adds 1
# to the input and returns the result

def inc_return(a):
    b = inc(a)
    return(b)

# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    return a + b


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    c = sum(a, b)
    c = inc_return(c)
    return c
    


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    b = bool(a%2 == 0)
    return(b)


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    x = phrase * repeat
    return x


    # hint: you can add strings together 
    # in order to concatenate them
    

