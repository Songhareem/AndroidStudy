
# 문자열.format

num = 20
welcome = '어서오세요'

print(num,'번 손님',welcome)
print('{} 번 손님 {}'.format(num,welcome))

# 주석 문장에 관하여

str = '''주석처리 된 문장도 문자열 변수에 입력 가능
이렇게 줄이 여러줄이어도 상관이 없습니다'''

print(str)

# number (about int / float) 및 cast 연산

print(6/5) #몫 표현(소수점 포함)
print(6//5) #몫 표현(소수점 버림)

a = int(6.5)
b = float(6)

print(a)
print(b)

