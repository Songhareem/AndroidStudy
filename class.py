
# 인스턴스의 이해

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 is list1)

print(list1 is list2) # is - 같은 인스턴스인지 비교

print(list1 == list2) # == 내부 원소만 비교

# 클래스 선언

class Human():
    '''사람'''

    def __init__(self, hp,mp,name):
        # init function
        self.Hp = hp
        self.Mp = mp
        self.Name = name

    def getHp(self):
        print(self.Hp)

    def getMp(self):
        print(self.Mp)

    def getName(self):
        print(self.Name)

    def __str__(self):
        # str function - 사용은 print( 객체명 )
        return "{}의 HP는{}, MP는{} 입니다".format(self.Name,self.Hp,self.Mp)

kim = Human(6,4,'kim') # __init__ 사용
kim.getHp()
kim.getMp()
kim.getName()
print(kim) # __str__사용

