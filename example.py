# Data Types

# def change_sound(sounds, animal, new_sound):
#     sounds[animal] = new_sound

# sounds = {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'oinks',
# }

# change_sound(sounds, 'cat', 'purrs')
# print(sounds)

# # Basic Operations

# ## Arithmetic Operators
# import math
# print(math.isclose(0.1 + 0.2, 0.3))

# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))

# # Equality Comparisons

# print(42 == 42)
# print(42 == 43)
# print('foo' == 'foo')
# print('FOO' == 'foo')

# Orderec Comparisons

# print(42 < 41)
# print(42 < 42)
# print(42 <= 42)
# print(42 < 43)

# print('abcdf' < 'abcdef')
# print('abc' < 'abcdef')
# print('abcdef' < 'abc')
# print('abc' < 'abc')
# print('abc' <= 'abc')
# print('abd' < 'abcdef')
# print('A' < 'a')
# print('Z' < 'a')

# print('3' < '24')
# print('24' < '3')

# print({3, 1, 2} < {2, 4, 3, 1})
# print([1, 2, 3] < [1, 3, 3])

# Coercion

# print(int('5'))
# print(float('3.141592'))

# print(str(5))
# print(str(3.141592))

# ## (Unnecessary) Coercion with 'str'
# print(str(False))
# print(str([1, 2, 3]))

# ## Implicit Coercion
# print(False)
# print([1, 2, 3])
# print({4, 5, 6})


# # Determining Types

# print(type('test') is str)

# print(type([1, 2, 3]).__name__)

# # String Representation

# my_str = 'abc'
# print(my_str)
# print(str(my_str))
# print(repr(my_str))

# # Collection and String Lengths

# print(len('Launch School'))

# # Variables and Variable Names

# answer = 41
# print(answer)
# answer = 42
# print(answer)

# # Naming Conventions

# variable_to_be_used = 12
# CONSTANT_NUMBER = 14
# # Classes: PascalCase/CamelCase

# # Creating and Reassigning Variables
# forename = 'Clare'
# forename = 'Victor'

# foo = 'abcdefghi'
# foo = 'hello'
# Python creates the string in a memory address; another memory address represents the variable, whose value is the address of the object

foo = 42
foo = foo - 2
foo = foo * 3
foo = foo + 5
foo = foo // 25
foo = foo / 2
foo = foo**3
print(foo)

# Augmented Assignment

foo = 42
foo -= 2
foo *= 3
foo += 5
foo //= 25
foo /= 2
foo **= 3

print(foo)

bar = 'xyz'
bar += 'abc'
bar *= 2
print(bar)

bar = [1, 2, 3]
bar += [4, 5]
print(bar)

bar = {1, 2, 3}
bar |= {2, 3, 4, 5}

bar -= {2, 4}
print(bar)