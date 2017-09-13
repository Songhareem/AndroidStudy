
# list 선언 및 값 교체

list1 = [0,1,2,3,4,5]

for i in range(len(list1)):
    print(list1[i])

print(' ')

list1[0] = 6

for i in range(len(list1)):
    print(list1[i])

print(' ')

print(list1[-1], list1[-2], list1[-3], list1[-4], list1[-5], list1[-6])

# list 값 추가, 삭제, 확인

print(' ')

list2 = [0,1,2,3,4,5]

list2.append(6) # 맨뒤에 값 6을 추가함

for i in range(len(list2)):
    print(list2[i])

list2.remove(6) # 어떤 자리던 6를 찾아서 삭제
# del list2[0] # 첫번째 자리에 있는 수 제거

print(' ')

for i in range(len(list2)):
    print(list2[i])

if 2 in list2:
    print('there is two in list2')

# 리스트 합치기

list3 = [1,2,3]
list4 = [4,5,6]

list5 = list3 + list4

print(' ')

for i in range(len(list5)):
    print(list5[i])

# 선언 추가

list6 = list(range(20))
print(list6)
