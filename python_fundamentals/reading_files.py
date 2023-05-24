# file = open('./data.txt', 'r')
# lines = file.readlines()
# for line in lines:
#     print(line)
# file.seek(0)
# for line in lines:
#     print(line)
# print(lines)

# text = file.read()
# print(text)
# file.close()

with open('./data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
    file.seek(0)
    for line in lines:
        print(line)
    print(lines)

    text = file.read()
    print(text)
# file.close()