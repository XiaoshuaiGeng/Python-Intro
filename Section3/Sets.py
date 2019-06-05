# Sets
# Sets are an unordered collection of unique elements. We can construct them by using the set() function.
newSet = set()
print('The current set status: {}'.format(newSet))
newSet.add(1)
print('The current set status: {}'.format(newSet))
newSet.add(2)
print("Now add another 2 into the set")
newSet.add(2)
print('The current set status: {}'.format(newSet))

# We can cast a list with multiple repeat elements to a set to get the unique elements.
anotherSet = set([1,2,2,3,5,5,5,7,9])
print('The original list is {}'.format([1,2,2,3,5,5,5,7,9]))
print('After putting the list into set, now the set is: {}'.format(anotherSet))

stringSet = set('Parallel')
print(stringSet)
