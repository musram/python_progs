from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests


if __name__ == "__main__":
    names = 'pybites mike bob julian tim sara guido'.split()
    print(names)


    #p = re.compile(r'[A-M]')

    #p.find(names)

    #print(p)



    resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
    words=  resp.text.lower().split()
    print(words[:5])
    print( '-' in words)
    

    #remove the '-'



    #remove the stop words

    resp  =  requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
    stop_words = resp.text.lower().split()

    words = [ word for word in words if word.strip() and word not in stop_words]


    print( 'the' in words)

    cnt = Counter(words)
    print(cnt.most_common(5))


    # convert to title
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

    names = [ name.title() for name in NAMES]

    print( names[:5])

    #reverse the name

    def reverse_name(names):
        for name in names:
            first, second = name.split()
            yield 'second, firstxs'

    reverse_name_list = [names for name in reverse_name(NAMES)]
    #print(reverse_name_list)
    
    
    
    
    

    #generator
    options = 'red yellow blue white black green purple'.split()
    def create_select_options(options=options):
        for option in options:
            yield '<option value={}>{}</option>'.format(option, option.title())
    
    print(create_select_options())

    for elem in create_select_options(options):
        print(elem)


    #Arnold teams up with Brad

    def gen_pairs():
        first_names = [ name.split()[0] for name in NAMES]

        while True:

            first , second = None, None
            while first == second:
                first, second = random.sample(first_names, 2)

            yield f'{first} teams up with {second}'

    pairs = gen_pairs()
    for _ in range(10):
        print(next(pairs))
            

    #using isslice

    first_ten = itertools.islice(pairs, 10)
    print( list(first_ten))

    #parisng the names

    def parsing_names(names):
        if isinstance(names, list):
            names = list(set([ name.title() for name in names]))

        shortest_name = sorted(names, key= lambda x: x[1])[0]

        return shortest_name

    print(parsing_names(NAMES))
        
                         
    
