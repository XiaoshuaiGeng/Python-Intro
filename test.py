
# String format exercise
print('String format exercise')
result = 100 / 777
testString = "test"
print(result)
print("{}".format("Hello World"))
print(f'hello world{testString}')
# f-string method is supported in python 3.6 or higher
print('****************\n')
# list testing
print('List testing')
print("my_list1 is [1,2,3]")
print("my_list2 is ['String',100,23,2]")
my_list1 = [1,2,3]
my_list2 = ['String',100.23,2]
# len() measures the length of the string
print('my_list2 is {}'.format(len(my_list2)))
print('This element is from my_list1[2]: {}'.format(my_list1[2]))
print('This element is from my_list2[1]: {}'.format(my_list2[1]))
print('List concatenation: list1+list2 = {}'.format(my_list1+my_list2))
print("String appending")
print('my_list1.append(4)')
my_list1.append(4)
print('This element is from my_list1[2]: {}'.format(my_list1))

