
list1 = [] # list 선언(안해도 상관없음)

list1 = [ i for i in range(1,11) ] # for문을 이용, 1~10 까지 list1에 삽입
print(list1)

list2 = [i for i in range(0,11) if i%2 == 0 ] # for, if 이용 0 ~ 10 중 짝수만 삽입
print(list2)

list3 = [(x,y) for x in range(1,10) for y in range(1,10)] # 이중for문 + 튜플을 이용한 삽입
print(list3)

# comprehension 을 이용한 list -> dict 변환 (for 문 사용)

students = ['one','two','three']

dict1 = {'{}'.format(num+1): name for num, name in enumerate(students) }
print(dict1)

# zip(list1, list2) - list1, list2의 값을 key값에 맞춰 순차적으로 반환

product = ['풀','가위','크레파스']
price = [800,2500,5000]
dict2 = { product : price for product, price in zip(product, price)}

print(dict2)