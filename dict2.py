
dict = {

    'one' : 1,
    'two' : 2,
    'three' : 3,
}

for i in dict:

    print(i)
    print(dict[i])

dict['four'] = 4 # add into dict

for i in dict:

    print(i)
    print(dict[i])

dict['four'] = 10 # change dict

for i in dict:

    print(i)
    print(dict[i])

del(dict['four']) # remove in dict
# dict.pop('four') # same

for i in dict:

    print(i)
    print(dict[i])
