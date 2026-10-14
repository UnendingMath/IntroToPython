# # Exercise 1:

# False or (True and False) # Evaluates all values; False
# True or (1 + 2) # Evaluates just the left operand; True
# (1 + 2) or True # Evaluates just the left operand; 3
# True and (1 + 2) # Evaluates all operands; 3
# False and (1 + 2) # Evaluates just the left operand; False
# (1 + 2) and True # Evaluates both operands; True
# (32 * 4) >= 129 # Evaluates both operands; False
# False != (not True) # Evaluates both operands; False
# True == 4 # Evaluates both operands; False
# False == (847 == '847') # Evaluates both operands; True

# # Exercise 2:

# def even_or_odd(value):
#     match value % 2:
#         case 0:
#             print("even")
#         case _:
#             print("odd")

# even_or_odd(5)

# value = 4

# print("even" if value % 2 == 0 else "odd")

# # Exercise 3:
# # bar_code_scanner('113') prints 'Product2', as our argument is '113', and the match/case statement matches our argument.
# # bar_code_scanner(142) prints 'Product not found!', as our argument is an integer, while all cases are strings.

# # Exercise 4:

# def baz():
#     if foo():
#         return 'bar'
#     else:
#         return qux()

# Exercise 5:
# This code outputs 'Empty', as we are providing a falsy value (an empty list) as an argument to the function call.

# Exercise 6:

def all_caps(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text

def all_caps_second(text):
    return text.upper() if len(text) > 10 else text

print(all_caps('hello world'))
print(all_caps_second('hello world'))

# Exercise 7:

def number_range(number):
    if number >= 0 and number <= 50:
        print(f"{number} is between 0 and 50")
    elif number > 50 and number <= 100:
        print(f"{number} is between 51 and 100")
    elif number > 100:
        print(f"{number} is greater than 100")
    else:
        print(f"{number} is less than 0")
