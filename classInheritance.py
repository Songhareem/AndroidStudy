
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

'''귀찮아서 Human 클래스가 있는 파일을 import하려했는데, 
    파일명이 class라서 못했다 가능하면 예약어를 파일명으로 정하지 말자'''

# class 클래스명 (부모 클래스명) - 상속 선언

class warrior(Human):

    def __init__(self, hp, mp, name, atk, agi):
        # call super() function
        super().__init__(hp, mp, name)
        self.Atk = atk
        self.Agi = agi

    def getAtk(self):
        print(self.Atk)

    def getAgi(self):
        print(self.Agi)

    def getHp(self):
    # getHp function override
        self.Hp += 1
        print('hp is {}'.format(self.Hp))

Hide = warrior(7,3,'Hide',12,8)

Hide.getHp()
Hide.getMp()
Hide.getName()
Hide.getAtk()
Hide.getAgi()

# python 에서 overloading은 지원하지 않는다


