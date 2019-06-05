# Nested Lists
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print(matrix)
print('Print the index 0 of the matrix {}'.format(matrix[0]))
print('Print the first element of the matrix [{}]'.format(matrix[0][0]))

# List Comprehensions(very important)
# Python has an advanced feature called list comprehensions.
# They allow for quick construction of lists.
# To fully understand list comprehensions we need to understand for loops.

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print(first_col)