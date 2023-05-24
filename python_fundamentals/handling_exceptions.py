total = 4
count = 0

try:
    average = total / count
    print('Average is: ', average)
except ZeroDivisionError as e:
    print('Cannot divide zero', e)

print('Save my progress')