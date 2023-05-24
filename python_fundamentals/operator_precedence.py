#membership tests
edutainers = ['Vonne', 'Justin', 'Aubri', 'Ronnie']
print ('Daniel in Edutainers: ', 'Daniel' in edutainers)
print ('Vonne in Edutainers: ', 'Vonne' in edutainers)
print ('Daniel in Edutainers: ', 'Daniel' not in edutainers)

# identity tests
favorite_food = 'cheese'
lunch_today = 'cheese'
print(favorite_food is lunch_today)
other_edutainers = ['Vonne', 'Justin', 'Aubri', 'Ronnie']
print (edutainers is other_edutainers)

#not operator
print(not 1 == 1)
print(1 != 1)

# precedence
print(3 % 2 + 1 is 4 - 2 // 3)

print(4 * 3 + 1)