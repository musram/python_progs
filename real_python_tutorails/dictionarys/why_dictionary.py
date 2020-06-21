
def bits(a):
    print("{0:b}".format(a))


if __name__ == "__main__":
    """
    (1) A dictionary is really a list.

    (2) Keys are hashed to produce indexes.

    (3) To build an index python uses  bottom n bits of the hash.

    (4) So the table looks like Idx, hash, key, value.
           (a) compute hash. 
           (b) truncate it.
           (c)  Look in that slot.
    (5)  DIcionary returns  their contents in crazy order.
          (a) SInce collision happens becuase of multiple key mapped to same slots, keys are moved away from the natural hash values.
    """
    
    for key in 'Monty', 3.323, (1,2,3):
        print(bits(hash(key)), key)



    """
    Hashing your classes"
    """
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self):
            return self.x == self.y

        def __hash__(self):
            return hash(self.x) * hash(self.y)
