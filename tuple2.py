
list = [1,2,3,4,5]

for i,v in enumerate(list):

    print('{}번째 값 : {}'.format(i,v))

for a in enumerate(list):

    print('{}번째 값 : {}'.format(*a)) # *a 는 언패킹한 값( key, val )

dict = {

    '나' : 20,
    '동생' : 18,
    '엄마' : 40,
    '아빠' : 43,
}

for key, val in dict.items():

    print("{}의 나이는 : {}".format(key, val))

for family in dict.items():

    print("{}의 나이는 : {}".format(*family))



