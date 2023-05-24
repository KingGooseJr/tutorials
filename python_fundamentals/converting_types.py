favorite_number = '7' #string variable
fav_num_type = type(favorite_number)

print ('The type for favorite_number is ', fav_num_type)

favorite_number_as_number = float(favorite_number)
print ('favorite_number_as_number: ', favorite_number_as_number)
print ('The type for favorite_number_as_number is ', type(favorite_number_as_number))

age = 12
print ('age: ', age)
print ('The type for age is ', type(age))
age_str = str(age)
print ('age_str: ', age_str)
print ('The type for age_str is ', type(age_str))

print (int(3.001992309847098))
print (int(3.901992309847098))

likes_cheese = 'False'

print ('as_boolean: ', bool(likes_cheese))

number = '18'
number_as_a_number = eval(number)
print ('number_as_a_number: ', number_as_a_number)
print ('type: ', type(number_as_a_number))