# Exercise 1: Use concatenation to create your full name from your first and last names. 

first_name = "Jack"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Exercise 2: 

number = 4936

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10

# Exercise 3
# Equals 510
print('5' + '10')

# Exercise 4: Refactor the code from the previous exercise to use coercion to print 15 instead.

print(int('5') + int('10'))

# Exercise 5: Will an error occur if you try to access a list element with an index greater than or equal to the list's length?

foo = ['a', 'b', 'c']
print(foo[3])
# Yes, this will result an error. Only dictionaries allow us to assign new elements

# Exercise 6: To what value does the following expression evaluate?

'foo' == 'Foo'
# This evaluates to False, as F and f have different ASC-II codes (F being lower than f)

# Exercise 7: What will the following code do? Why?

int('3.1415')
# This will create an object with the value 3 (as an integer)

# Exercise 8: To what value does the following expression evaluate?

'12 < '9'
# This would evaluate to true. Since both comparsions are strings, it is evaluated Lexicographicallty