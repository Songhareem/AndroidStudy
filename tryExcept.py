
'''
try - 예외가 일어날 가능성이 있는 코드 부분

except - 예외가 일어났을때 처리하는 부분
'''

try:
    print(a)

except NameError:
    print('NameError')

# 예외 이름을 모르는 경우 처리방법

try:
    b = 3/0

except Exception as ex:    #  Excetption as ex - 에러의 발생 및 종류를 알아냄

    print(ex)
    print('UnknownError')

# 에러 직접 발생

c = 1

try:
    while c != 0:

        c += 1

        print(c)

        if c > 5 :
            raise ValueError # 에러 발생, ValueError은 원래 에러 종류 중 하나

except ValueError:

    print('c가 5를 넘었습니다')
