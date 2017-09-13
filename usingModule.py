
import math
import random

r = 10

print(2*r*math.pi) # math.pi = 3.14...

print(math.ceil(2.5)) # 올림

print(math.floor(2.5)) # 내림

list = ['가위','바위','보']

choice = random.choice(list)

print(choice)

num = random.choice(range(100)) # 0 ~ 99

print(num)

num = random.randint(2,5) # 2 ~ 5

print(num)

