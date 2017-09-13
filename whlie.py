
a = 0

while True:

    print(a)

    a += 1

    if a == 10 :

        print('save point')

        break

while a<100:

    print(a)

    a += 10

    if a%20 != 0:
        continue



num = 0

while num not in ['one','two','three']:

    num = input('you can input "one" "two" "three",only > ')

