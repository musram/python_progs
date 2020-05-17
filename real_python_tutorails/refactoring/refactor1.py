#https://sourcery.ai/blog/explaining-refactorings-1/





if __name__ == "__main__":

    #reducing if statements
    
    a = True
    b = True

    if a:
        if b:
           print("yes")

    if a and b:
        print("yes")


    #Hoist repeated code outside conditional statement

    sold = 20
    DISCOUNT_PRICE = 10
    DISCOUNT_AMOUNT = 10
    if sold > DISCOUNT_AMOUNT:
        total = sold * DISCOUNT_PRICE
        label = 'Total: {}'.format(total)
    else:
        total = sold * PRICE
        label = 'Total: {}'.format(total)
    print(label)

    if sold > DISCOUNT_AMOUNT:
        total = sold * DISCOUNT_PRICE
    else:
        total = sold * PRICE

    label = 'Total: {}'.format(total)
    print(label)


    #Replace yield inside for loop with yield from


    def get_contents(entry):
        for block in entry:
            yield block

    print(next(get_contents([1,2,3])))

    def get_contents(entry):
        yield from  entry


    print(next(get_contents([1,2,3])))


    #Replace list() with []

    x = []

    #Hoist statements out of for/while loops


    class Building:
        def __init__(self, street_address):
            self.street_address = street_address

        def __str__(self):
            return self.street_address

    buildings = [ Building("no1"),Building("no3"),Building("no6"),Building("no8")]

    address = []

    for building in buildings:
        city = 'London'
        address.append((building.street_address, city))

    print(address)    

    city = 'London'    
    for building in buildings:
        address.append((building.street_address, city))

    print(address)

    #Use any() instead of for loop

    found = False
    things = [1,2,2,3,4,5,2,4,5,2]
    other_things = 7
    for thing in things:
        if thing == other_things:
            found = True
            break
    print(found)

    found = any( thing == other_things for thing in things)

    print(found)

    
        

    

