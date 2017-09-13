
# type(a) - return a의 자료형
# isinstance( x, y ) - x(값)의 y(자료형)형 검사

a = 1
b = 1.0
c = 'Hello'
d = list(range(2))
e = (1,2,3,4)
f = { 1:1, 2:2, 3:3 }

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))
print(isinstance(e, tuple))
print(isinstance(f, dict))

