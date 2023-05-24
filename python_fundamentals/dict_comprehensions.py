labels = ['first_name', 'last_name', 'favorite_food']
data = ['Vonne', 'Smith', 'pizza']

# favorite_food_index = labels.index('favorite_food')
# favorite_food = data[favorite_food_index]

# print('Favorite food: ', favorite_food)

results = [(labels[index], data[index]) for index in range(0, len(labels))]

print(results)