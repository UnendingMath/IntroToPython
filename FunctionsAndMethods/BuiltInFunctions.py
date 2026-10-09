# # Built In Functions


# # Minimum and Maximum (min and max)
# print(min(-10, 5, 12, 0, -20))
# print(max(-10, 5, 12, 0, -20))

# print(min('over', 'the', 'moon'))
# print(max('over', 'the', 'moon'))
# # print(max(-10, '5', '12', '0', -20)) gives a TypeError; must have ordering that can e recognized


# # Order and Character (ord and char)
# print(ord('a'))
# print(ord('='))
# # ord returns the integer that represents the Unicode code point of the character in the argument.

# print(chr(97))
# print(chr(65))
# # chr returns the character associated with the code inputted as an argument.


# Any and All (any() and all())
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))
print(any(collection2))
print(any(collection3))
print(any([]))

print(all(collection1))
print(all(collection2))
print(all(collection3))
print(all([]))

# ID Function for the REPL (id())

# Directory Function for the REPL (dir())

# Help Function for the REPL (help())

greeting = "Salutations"

def well_howdy(who):
    greeting = 'Howdy'
    print(f"{greeting}, {who}")

well_howdy('Angie')
print(greeting)