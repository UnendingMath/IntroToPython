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

print(int('5'))
print(float('3.141592'))

print(str(5))
print(str(3.141592))

## (Unnecessary) Coercion with 'str'
print(str(False))
print(str([1, 2, 3]))

## Implicit Coercion
print(False)
print([1, 2, 3])
print({4, 5, 6})