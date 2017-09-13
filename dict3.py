
# dict 반복문 사용

ages = {

    'Jack' : 23,
    'Song' : 26,
    'Chol' : 27,

}

for key in ages.keys():

    print(key)

for val in ages.values():

    print(val)

for key, val in ages.items():

    print(key, val)