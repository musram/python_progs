




if __name__ == "__main__":

    # read the entire file
    with open('dog_breeds.txt', 'r') as reader:
        print(reader.read())

    #read 5 characters of the line
    with open('dog_breeds.txt', 'r') as reader:
        print(reader.readline(5))
        print(reader.readline(5))
        print(reader.readline(5))
        print(reader.readline(5))

    # Read and print the entire file line by line    
    with open('dog_breeds.txt', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            print(line, end='')
            line = reader.readline()
        
    #read the lines as a list
    with open('dog_breeds.txt', 'r') as reader:
        for line in reader.readlines():
            print(line, end= ' ')

    #pythonic approach        
    with open('dog_breeds.txt', 'r') as reader:
        for line in reader:
            print(line, end= ' ')


    #Working with two files
    d_path = 'dog_breeds.txt'
    d_r_path = 'dog_breeds_reversed.txt'
    with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
        dog_breeds = reader.readlines()
        writer.writelines(reversed(dog_breeds))

    #appending to a file
    with open('dog_breeds.txt', 'a') as a_writer:
         a_writer.write('\nBeagle')
