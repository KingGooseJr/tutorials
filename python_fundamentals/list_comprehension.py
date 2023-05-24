numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
other = []
print(numbers)
# add 3 to each number

# for number in numbers:
#     number = number + 3

# print(numbers)

# for index in range(0, len(numbers)):
#     number = numbers[index]
#     numbers[index] = number +3

print(numbers)

for index in range(0, len(numbers)):
    number = numbers[index] + 3
    other.append(number)
    

print(other)

other = [number + 3 for number in numbers]
print(numbers)
print(other)