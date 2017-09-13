
# 튜플은 한번 정해진 순서를 바꿀 수 없다
# 튜플은 값의 변경 및 삭제가 불가능 하다

# 선언

tuple1 = (1,2,3,4)

tuple2 = 1,2,3,4

list = [1,2,3,4]

tuple3 = tuple(list)

if tuple1 == tuple2 == tuple3 :

    print('equal')

# 튜플을 활용한 패킹
# packing - 한 변수에 여러값을 넣는것
# unpacking - 여러변수에 값을 쪼개어 넣는것

c = (3, 4)

d, e = c   # unpacking

print(d,e)

f = d, e   # packing

print(f)
