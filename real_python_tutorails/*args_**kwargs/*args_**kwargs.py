# order is standard arguments, *args arguments, **kwargs arguments

def my_function(a, b, *args, **kwargs):
    pass



#unpacking with * and **

def print_unpacked_list():
    my_list = [1, 2, 3]
    print(*my_list)

def my_sum(a, b, c):
    print(a + b + c)


def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result



if __name__ == "__main__":
    print_unpacked_list()


    my_list = [1,2,3]
    my_sum(*my_list)

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]

    print(my_sum(*list1, *list2, *list3))


    #unpacking 
    my_list = [1, 2, 3, 4, 5, 6]

    a, *b, c = my_list
    print(a)
    print(*b)
    print(c)

    #merging  list

    my_first_list = [1, 2, 3]
    my_second_list = [4, 5, 6]
    my_merged_list = [*my_first_list, *my_second_list]

    print(my_merged_list)

    #merging dict

    my_first_dict = {"A": 1, "B": 2}
    my_second_dict = {"C": 3, "D": 4}
    my_merged_dict = {**my_first_dict, **my_second_dict}

    print(my_merged_dict)


    #unpacking string

    a = [*"RealPython"]
    print(a)

    a,*b = "RealPython"
    print(a)
    print(b)
