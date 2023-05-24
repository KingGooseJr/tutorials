numbers = [1, 2, 3, 4, 5]

# for index in range(0, len(numbers)):
#     element = numbers[index]
#     print(element)

#while loop
# index = 0
# numbers_length = len(numbers)

# while index < numbers_length:
#     element = numbers[index]
#     print(element)
#     index = index +1

# take user input
words = set()
while True:
    word = input('>>') ## blocking until something happens
    words.add(word)
    print('you have typed the following word: ', words)