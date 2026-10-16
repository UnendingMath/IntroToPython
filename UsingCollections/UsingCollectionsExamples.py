# # Indexing
# seq = ('a', 'b', 'c')
# print(seq[0]) # a (first element)
# print(seq[1]) # b (second element)
# print(seq[2]) # c (third element)
# # print(seq[3]) # IndexError: tuple index out of range 

# # Negative Indexing
# print(seq[-1])
# print(seq[-2])
# print(seq[-3])

# # Mutation by reassignment
# seq = ['a', 'b', 'c']
# seq[1] = "B"
# print(seq)

# # Slicing
# string = 'abcdefghi'
# print(string[3:7])
# print(string[-6:-2])
# print(string[2:8:2])
# print(repr(string[3:3])) # ''
# print(string[:]) # full string
# print(string[::-1]) # ihgfedcba (full string reversed
# # Key Based Access
# my_dict = {
#     'a': 'abc',
#     37: 'def',
#     (5, 6, 7): 'ghi',
#     frozenset([1, 2]): 'jkl',
# }

# print(my_dict['a'])
# print(my_dict[37])
# print(my_dict[(5, 6, 7)])
# print(my_dict[frozenset([1, 2])])
# # print(my_dict['nothing']) # KeyError: 'nothing' (Key has not been defined)

# # dict.get() method: Returns the value associated with a given key (if the key exists)
# print(my_dict.get('a'))
# print(my_dict.get('nothing')) # None (key has not been defined)
# print(my_dict.get('nothing', 'N/A')) # N/A (Even though it has not been defined, we are passing a default value if the key is not found)

# # Key Based Mutation
# my_dict['a'] = 'ABC'
# my_dict[37] = 'DEF'
# my_dict[(5, 6, 7)] = 'GHI'
# my_dict[frozenset([1, 2])] = 'JKL'

# # Assigning New Keys to a Dictionary (Key must be immutable/hashable)
# my_dict['xyz'] = 'Hey there!'
# # Assigning New Keys with Unhashable (Mutable) objects will not work
# # my_dict[[1, 2, 3]] = 'Hey There!' # TypeError; unhashable type: 'list'

# # Collection Membership: in operator determines whether the object to the operator's left is in the iterable collection on the right.
# seq = [4, 'abcdef', (True, False, None)]
# print(4 in seq) # True
# print(4 not in seq) # False (not operator inverses (takes complement))
# print('abcdef' in seq)
# print('abcdef' not in seq)
# print('cde' in seq[1]) # True; strings are considered an iterable sequence, in membership operator looks for substrings with the string.
# print('cde' not in seq[1]) # Fale
# print('acde' in seq[1]) # False
# print('acde' not in seq[1]) # True
# print(3.14 in seq) # False
# print(3.15 not in seq) # True

# # Locating Indices and Counting
# names = ['Karl', 'Grace', 'Clare', 'Victor', 'Antonina', 'Allison', 'Trevor']
# print(names.index('Karl')) # index method returns the index of the first element in the sequence that matches
# print(names.index('Trevor'))
# # print(names.index('Chris')) ValueError: 'Chris' is not in list

# numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
# print(names.count(1)) # count method returns the number of times a value occurs in a sequence.
# print(names.count(3))
# print(names.count(4))
# print(names.count(7)) # 0 (No error)

# # Merging Collections
# iterable1 = [1, 2, 3]
# iterable2 = ('Kim', 'Leslie', 'Bertie')
# iterable3 = [None, True, False]

# zipped_iterables = zip(iterable1, iterable2, iterable3) # iterates over iterables in parallel an returns a list-like object of tuples
# print(list(zipped_iterables))
# # Pretty printed for clarity
# # [
# #   (1, 'Kim', None),
# #   (2, 'Leslie', True),
# #   (3, 'Bertie', False)
# # ]

# result = zip('12345', 
#              ['chicken', 'banana', 'apple'],
#              {True, False}
#              )

# print(result) # If lengths differ and strict=True is not given, zip stops after exhausting the shortest iterable
# # zip() function is an iterator, meaning that it is an object that tracks its position among the values. Once it passes one,
# # it cannot go back. When we attempt to print it directly, it returns: <zip object at 0x7fb1161c8780>

# Operating on Dictionaries
people_phones = {
    'Chris': '111-2222',
    'Pete': '333-4444',
    'Clare': '555-6666',
}

# # The following are Dictionary View Objects that are tied to the dictionary

# print(people_phones.keys())
# # dict_keys(['Chris', 'Pete', 'Clare'])

# print(people_phones.values())
# # Pretty printed for clarity
# # dict_values([
# #     '111-2222',
# #     '333-4444',
# #     '555-6666'
# # ])

# print(people_phones.items())
# # Pretty printed for clarity
# # dict_items([
# #     ('Chris', '111-2222'),
# #     ('Pete',  '333-4444'),
# #     ('Clare', '555-6666')
# # ])

# If we remove, update, or add a new key/value pair, the corresponding view objects are updated immediately

keys = people_phones.keys()
values = people_phones.values()

print(keys)
print(values)

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)
print(values)

# Mutating Methods

example = [1, 2, 3]

example.append(4) # adds the integer 4 at the end of the list.
print(example)
example.insert(2, 2.5) # inserts the flost 2.5 before the current 2nd index. 
# If the index is higher than the list length, it will place it in the last position. Can use negative indexing.
print(example)
example.extend([5, 6, 7]) # Adds an iterable to the end of the iterable calling the method.
print(example)

example.remove(4) # Removes the element 4 if it exists. If not, a ValueError is raised. 
print(example)

example.pop(2) # Removes and returns an indexed element from a mutable sequence
# If no index is given, it removes the last element in the sequence. It raises an error if the index is out of range.
print(example)

example.clear()
print(example)


