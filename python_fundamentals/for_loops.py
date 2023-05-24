numbers = [1, 2, 3, 4, 5]
words = {'the', 'cheese', 'is', 'good'}
user = ('Vonne', 'Smith', 23, 'pizza')
foods = dict(pizza=True, onions=False, olives=False, salami=True)

# print(numbers)
# print(words)
# print(user)
# print(foods)
#
# the standard for loop in Python
for number in numbers:
    print(number)

for index in range(1, len(numbers)):
    element = numbers[index]
    print(element)