
# 슬라이싱(slicing) 방법
# [x:y] - x번째 값부터 y-1 값까지 가져옴
# [x: ] - x번째 값부터 끝까지 가져옴
# [ :y] - 처음부터 y-1 값까지 가져옴
# [ : ] - 처음부터 끝까지 가져옴

text = "good python"
text1 = text[5:11]
text2 = text[ :5]

print(text1)
print(text2)

list = [0,1,2,3,4,5]
list1 = list[1:5]
list2 = list[0:4]

print(list1)
print(list2)

# 슬라이싱 step
# step 값을 이용하여 띄엄띄엄 값을 가져올 수 있다

list3 = list[0:6:2]

print(list3)

# 슬라이싱 활용 ( 삭제 및 수정 )

tmp = [0,1,2,3,4,5,6,7,8,9]

del tmp[5: ] # 삭제
print(tmp)

tmp[0:5] = [1,2,3,4,5] # 원소와 같은 갯수 수정
print(tmp)

tmp[ : ] = [1,2,3,4,5,6] # 원소보다 많은 수로 수정
print(tmp)

tmp[ : ] = [1,2,3,4] # 원소보다 적은 수로 수정
print(tmp)
