letters = list('abcdefghijklmnop')

print (letters)

# How do I get the letters 'c' through 'f'?

selected = letters[2:6]
print ('Selected:', selected)

# How do I get every other letter from the list?
every_other = letters[::2]
print ('Every Other:', every_other)

# Bonus: Revers with slices
reverse_letters = letters[::-2]
print ('Reversed:', reverse_letters)
