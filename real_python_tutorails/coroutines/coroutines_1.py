def grep(substr):
    while True:
        line = yield
        if substr in line:
            print("found {}".format(substr))


if __name__ == "__main__":
    g = grep("users/created")
    print(next(g))
    print(g.send("users/get api took 1 ms."))
    print(g.send("users/created api took 4 ms."))



            
