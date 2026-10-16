# Exercise 1: If you have a list named people, how can you determine the number of entries in that list?
# We can determine the number of elements in a list with the len() function.

# Exercise 2: Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)

example = {1, 2, 3, 4}

# Exercise 3: Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.
# Order matters for both lists and tuples, as they are ordered sequences. We can also use numerical-based indexing to access the elements of both. Both are also heterogeneous.
# As for some differences, lists are mutable while tuples are immutable. Lists also use square brackets, while tuples use parentheses.

# Exercise 4: Why can we treat strings as sequences?
# We can treat strings as sequences as they are an ordered set of characters. Python treats strings as iterables, meaning we can iterate through each character in a string. 

# Exercise 5: How do the set types differ from the sequence types?
# Set types must have all unique elements, while sequences allow for repeats and duplicates. Sets are also unordered, while the order is more important for sequences. 
# We cannot use numerical indexing for sets, while sequences allow for them. (Question for self: are sequences the only type of collection that uses numerical indexing?)

# Exercise 6: Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.
pi = 3.141592
str_pi = str(pi)
print(type(str_pi).__name__)

# Exercise 7: Without running the following code, identify the numbers that are included in each of the following ranges:
# range (7): [0, 1, 2, 3, 4, 5, 6]
# range(1, 6): [1, 2, 3, 4, 5]
# range(3, 15, 4): [3, 7, 11]'
# range(3, 8, -1): []; cannot have positive range with a negative step
# range(8, 3, -1): [8, 7, 6, 5, 4]; descending range with negative step size.

# Exercise 8: How would you print all the numbers in the following range?
range(3, 17, 4)
print(list(range(3, 17, 4)))

# Exercise 9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 9.1) Are the lists assigned to my_list and another_list equal?
# The lists assigned to my_list and another_list are equal

# 9.2) Are the lists assigned to my_list and another_list the same object?
# The two lists are not the same object. Our constructor list() creates a new object, so, therefore they are two different objects with two different IDs.

# 9.3) Are the nested lists at index 3 of my_list and another_list equal?
# Yes, they are equal.

# 9.4) Are the nested lists at index 3 of my_list and another_list the same object?
# Yes, they are the same object. This is because Python does something called shallow copying

# Exercise 10: Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will?
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
# Yes, it will print in alphabetical order, but not for the reason Bob intends. 
# Sets are unordered, but are somewhat ordered based on their insertion order. Their insertion is akphabetical, so it should print alphabetically.

# Exercise 11: 
name_country = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru', 
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
    }
print(name_country['Yoshitaka'])

