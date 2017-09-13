
# list/dict 공통점
# make

list = [1,2,3]

dict = {

    'zero' : 1,
    'one' : 2,
    'two' : 3,

}

# call

print(list[0])
print(dict['zero'])

# del

del (list[1])
del (dict['one'])

# len check

print(len(list))
print(len(dict))

# values or key check

print(2 in list)
print(2 in dict.values())

# del all

list.clear()
dict.clear()

# list/dict 차이점
# list : 삭제시 순서가 바뀌기 때문에 인덱스 대한 값이 바뀐다
# dict : Key 값을 가져오므로 삭제와 상관 없다