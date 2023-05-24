favorite_phrase = 'I Like Cheese'

# for letter in favorite_phrase:
#     print(letter)

# index = 0
# while index < len(favorite_phrase):
#     letter = favorite_phrase[index]
#     print(letter)
#     index = index + 1

favorite_number = 7
while True:
    guess = int(input("What is Vonne's favorite number?\n"))
    if guess == favorite_number:
        print('yayyyy!!! you win!!!')
        break
    else:
        print('Try again')