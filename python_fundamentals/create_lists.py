## our first list
## indices:     0         1       2         3       4       5

edutainers = ['Adam', 'Aubri', 'Daniel', 'Jo', 'Justin', 'Zach']

print ('Edutainers: ', edutainers)
print ('The third edutainer is: ', edutainers[2])

# How do I know how many elements there are programatically?

print ('The number of edutainers is: ', len(edutainers))
# with string
print ('Jo has:', len(edutainers[3]))

#How do I convert a string (others apply) to a  list?
favorite_food = 'fish taco'
favorite_food_character_list = list(favorite_food)

print ('Favorite Food: ', favorite_food)
print ('Characters: ', favorite_food_character_list)

numbers = [3, 4, 5, 6]
empty = []

print (numbers)
print (empty)

mixed = ['a', 2, False, []]
print (mixed)