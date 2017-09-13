
list = [1,2,3,4]

print(list.index(2)) # index(x) - x가 어딨는지 찾음

list.extend( [5, 6] )  # extend([x,y]) - x,y값을 리스트 뒤에 추가
print(list)

list.insert(6,7) # insert(x,y) - x자리에 y값을 끼워넣음
print(list)

list.reverse() # reverse - 리스트를 역순으로 정렬
print(list)

list.sort() # sort - 순서대로 정렬
print(list)