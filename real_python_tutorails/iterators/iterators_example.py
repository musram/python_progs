



if __name__ == "__main__":

    names = ['sai', 'asi', 'isa']
    for name in names:
        print(name)


    #what actuall happens internally is this:

    it = names.__iter__()

    print(next(it))

    #similalry

    f = open('/etc/passwd', 'r')

    it = f.__iter__()

    print(next(it))


    #writing generator
    #(1)

    def countDown(n):
        print('Counting from' , n)
        while (n > 0):
            yield n
            n -= 1
        print('Done')

    for x in countDown(5):
        print(x)


    #this is same as

    c  = countDown(5)

    it = c.__iter__()

    print(next(it))



    #writing genertor
    #(2)

    it = ( x for x in range(5,0,-1))

    print(next(it))


    #writing generator
    #(3)

    class CountDown:

        def __init__(self, n):
            self.n = n

        def __iter__(self):
            n = self.n
            while (n > 0):
                yield n
                n -= 1

    c = CountDown(5)

    for x in c:
        print(x)


    import os
    import time

    def follow(filename):
        f = open(filename, 'r')
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

    for line in follow('/etc/passwd'):
        row = line.split(',')
        print(row)

        
           
