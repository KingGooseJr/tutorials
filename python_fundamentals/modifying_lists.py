edutainers = ['Adam', 'Aubri', 'Daniel', 'Jo']

#How do I add an element to the end of a list?
print ('Edutainers: ', edutainers)

edutainers.append('Justin')

print ('Edutainers: ', edutainers)

#How do I remove an element from a list?
del edutainers[0]
print ('Edutainers: ', edutainers)

#How do I remove an element from the end of a list?
special = edutainers.pop()
print ('Edutainers: ', edutainers)
print ('Special: ', special)

#How do I change an element in a list?
edutainers[1] = 'Dan'
print ('Edutainers: ', edutainers)