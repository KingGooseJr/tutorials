numbers = [31, 2, 43, 0, 9, 10]
letters = ['b', 'c', 'e', 'd']
edutainers = ['Jo', 'Justin', 'Vonne', 'Cherokee']

print ('Numbers:', numbers)
print ('Letters:', letters)
print ('edutainers:', edutainers)

#How do I put a lsit in "ascending" order?

#numbers.sort()
sorted_numbers = sorted(numbers)
print ('Sorted Numbers: ', sorted_numbers)
print ('Numbers:', numbers)

sorted_letters = sorted(letters)
print ('Sorted Letters: ', sorted_letters)
print ('Letters:', letters)

sorted_edutainers = sorted(edutainers)
print ('Sorted Edutainers: ', sorted_edutainers)
print ('Edutainers:', edutainers)

#How do I put a list in "descending" order?
sorted_letters = sorted(letters)
des_letters = sorted(letters, reverse=True)
print ('Sorted Letters: ', sorted_letters)
print ('Letters:', letters)
print ('Descending Letters:', des_letters)

#How do I flip a list?
reversed_edutainers = list(reversed(edutainers))
print (edutainers)
print (reversed_edutainers)

edutainers.reverse()
print (edutainers)