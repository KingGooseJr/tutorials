
# user = { 'first_name': 'Vonne', 'last_name': 'Smith', 'age': 24 }
user = dict(first_name='Vonne', last_name='Smith', age=24)
foods = { 0: 'pizza', 1: 'cookie' }

# mathematical operations generally don't work

# getting elements (values)

first_name = user['first_name']
print(first_name)

f = foods[0]
print(f)

# set a value
user['age'] = 23
print(user)