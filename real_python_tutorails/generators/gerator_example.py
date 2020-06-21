#https://realpython.com/introduction-to-python-generators/#example-1-reading-large-files



#to read a large csv file


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row


def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


if __name__ == "__main__":

    #1 generator

    next(csv_reader("hate_crimes.csv"))

    print(csv_reader("hate_crimes.csv"))


    #2 genertor   using comprehension

    csv_gen = ( row for row in open("hate_crimes.csv"))

    print(csv_gen)



    #generating infinite sequence


    def count_down(n):
        while n > 0:
            yield n
            n -= 1

    print(next(count_down(10)))


    #clarity of yield


    gen = multi_yield()
    print(next(gen))
    print(next(gen))
  
    try:
        print(next(gen))
    except StopIteration as e:
        print(e)


    letters = ["a", "b", "c", "y"]

    # 3 generator
    gen = iter(letters)

    while True:
        try:
            letter = next(gen)
        except StopIteration:
            break
        print(letter)


    #process a file template

    def file_process(file_name):
        lines = (line for line in open(file_name, 'r'))
        list_line = (s.rstrip().split(",") for s in lines)
        col_names = next(list_line)

        company_dicts = (dict(zip(col_names, line)) for line in list_line)

        print(next(company_dicts))

        # average median_household_income for Alabama state

        avg_median_household_income = ( company_dict['median_household_income'] for company_dict in company_dicts if company_dict['state'] == 'Alabama')

        average = sum(avg_median_household_income)

        print( f'Avg is {average}')

    file_process("hate_crimes.csv")

    

    


            

    
