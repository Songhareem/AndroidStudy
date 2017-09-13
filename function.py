
def HelloWorld():
    print('Hello world')

HelloWorld()

#------------------------------

def add(a, b):
    addnum = a + b

    return addnum

a = 10
b = 10

total = add(a, b)

print(total)

#------------------------------

def recursiveFuction(c):

    c += 1

    if c == 5:
        print('done')
        return 0

    else :
        print(c)
        recursiveFuction(c)

c = 0

recursiveFuction(c)

#-----------------------------

def changeNum(x, y):

    return y, x

x = 1
y = 2

print(x, y)

y,x = changeNum(x, y)

print(y, x)
