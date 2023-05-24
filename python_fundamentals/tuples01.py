# define some tuples

user_fieldnames = ('first name', 'last name', 'age', 'favorite food')
user = ('Vonne', 'Smith', 23, 'pizza')
numbers = (1, 2, 3, 4, 5, 6)

one_number = (1, )
another_number = (1)
empty = ()

# print(type(empty))
# print(type(one_number))
# print(type(another_number))

# common operations with tuples

result = numbers * 3
print(result)

# accessing elements
print(user)
username = user[0:2]
# user[-1] = 'burrito'