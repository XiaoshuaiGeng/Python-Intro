# List Practice
# 1. List is initialized in middle brackets []

list = ['one', 'two', 'three']
print(list)

# 2. List append()
list.append('four')
print(list)

# 3. List pop()
list.pop()  # pop() will pop the last index element in default
print(list)
list.append('five')  # list concatenation also works list + ['five']
print('Print the full list {}'.format(list))
print('Print the list from its first index {}'.format(list[1:]))

# 4. List reverse()
newList = ['e', 't', 'c', 'v', 'x']
print('The list before reverse \n{}'.format(newList))
newList.reverse()
print('The list after reverse \n{}'.format(newList))

# 5. List sort()
newList.sort()
print('The list after sort \n{}'.format(newList))


