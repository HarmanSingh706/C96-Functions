def swapFile():
    nameOfFile = input("Enter The  First File Name You Want To Swap: ")
    nameOf2ndFile = input("Enter The 2nd File Name You Want To Swap: ")

    with open(nameOfFile, 'r') as a:
        data_a = a.read()

    with open(nameOf2ndFile, 'r') as b:
        data_b = b.read()

    with open(nameOfFile, 'w') as a:
        a.write(data_b)

    with open(nameOf2ndFile, 'w') as b:
        b.write(data_a)

swapFile()
