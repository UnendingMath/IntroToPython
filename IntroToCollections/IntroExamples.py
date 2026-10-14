# Sequences 

letters = ['a', 'b', 'c', 'd']
print(letters[0]) # a (first element)
print(letters[1]) # b (second element)


# lists and tuples are heterogeneous (can contain different data types); ranges are homogeneous (can only contain integers)
my_list = [
    'May',
    2.99,
    {None, True, False},
    [1, 2, 3],
]

# strings are not actual collections since the characters inside the string aren't objects
letters = ['a', 'b', 'θ', 'd',]
char = letters[2]
print(char is letters[2]) 

letters = 'abθd'
print(char is letters[2])