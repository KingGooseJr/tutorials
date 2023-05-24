output_filename = 'output.txt'
with open('data.txt', 'r') as input_file, open(output_filename, 'w') as output:
    for line in input_file:
        if line != '\n':
            output.write(line)