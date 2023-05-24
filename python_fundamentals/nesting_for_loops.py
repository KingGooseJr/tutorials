numbers = [1, 2, 3, 4]
letters = 'abcd'
my_list = ['the', 'dog', 'was', 'fat', 'and', 'I', 'ran', 'away']

# for number, letter in zip(numbers, letters):
#     print(number, letter)

# for number in numbers:
#     for letter in letters:
#         for word in my_list:
#             print(number, letter, word)

days = [
    list(range(3)),
    list(range(4)),
    list(range(5))
]
total = 0
for day in days:
    for sale in day:
        print(total, ': ', sale)
        total = total + sale
print(total)
