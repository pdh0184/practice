#게임
#보스 요괴 5마리가 있다
#각 요괴는 레벨이 30(불), 40(물), 50(불), 60(번개), 70(바람) 이고 속성을 가지고 있다
#캐릭터는 한 명이고 장비는 갑옷, 무기 , 펫을 가질 수 있다
import random
#요괴
class Monster():
    def __init__(self,level, type):
        self.level = level
        self.type = type

    def attr(self):
        return self.level, self.type

class character():
    name = ''
    level = 0
    weapon = ''
    pet = ''
    def weapon(self, level):
        if level < 30:
            return "나무몽둥이"
        elif level < 40:
            return "기본검"
        elif level < 50:
            return "강력한 검"
        elif level < 60:
            return "용검"
        elif level < 70:
            return "킹왕짱 검"
        else:
            return "소울웨폰"
        
    def pet(self, animal):
        if animal == 'cat':
            cat = ['냥냥이' , '개냥이' , '냥냥펀쳐', '호랑이']
            num = random.randrange(len(cat))
            return cat[num]
        
        elif animal == 'dog':
            dog = ['진돌이' , '멍멍이' , '바둑이', '월월이', '파트라슈']
            num = random.randrange(len(dog))
            return dog[num]
        
Hero = character()
Hero.name = "super power"
Hero.level = 55
Hero.weapon = Hero.weapon(Hero.level)
Hero.pet = Hero.pet('dog')

pig = Monster(30, '물')
dog = Monster(50 , '불')
sheep  = Monster(60 , '번개')
horse  = Monster(70 , '바람')
print(Hero.name ,Hero.level ,Hero.weapon,Hero.pet)
print(pig.attr())
print(dog.attr())
print(sheep.attr())
print(horse.attr())

print("\n")
print("여기서 부터는 다른 클래스 공부")
print("======================================")
print('\n')

class Animal:
    def __init__(self, name, species): #__init__은 클래스 파라미터로 필드를 정의해준다
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    #raise는 예외를 발생시킨다
    '''NotImplementedError 추상 클래스를 만들때 사용는 내장예외로 하위클래스에 def speak(self)가 구현되어 있지 않으면
    예외를 발생시킨다'''

    def info(self):
        return f"I am {self.name}, a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog") 
        self.breed = breed
        '''super()은 부모 생성자, 객체를 호출한다 여기서는 Animal의 __init__이 self.name = name,self.species = species이므로
        name은 파라미터 값 name, species는 Dog, breed는 파라미터 값 breed가 된다'''

    def speak(self):
        return "Woof!"
    #여기서 def spedak(self)를 따로 구현해주지 않으면 부모 클래스(Animal)에 의하여 예외가 발생한다

    def info(self):
        return super().info() + f" and my breed is {self.breed}"
    '''super()을 사용했기 때문에 부모 클래스 Animal.info()인 f"I am {self.name}, a {self.species}" 가 그대로 실행되며
    여기에 추가로 f" and my breed is {self.breed}" 까지 실행된다'''

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"

    def info(self):
        return super().info() + f" and my color is {self.color}"

# 사용 예시
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Brown Tabby")

print(dog.info())  # 출력: I am Buddy, a Dog and my breed is Golden Retriever
print(dog.speak())  # 출력: Woof!

print(cat.info())  # 출력: I am Whiskers, a Cat and my color is Brown Tabby
print(cat.speak())  # 출력: Meow!

print('\n')
print('====================================================================================')
print('직접 super(), raise NotImplementedError, __init__을 활용하여 클래스 만들어보기')
print('====================================================================================')
print('\n')

class Artist:

    def __init__(self, name, music):
        self.name = name
        self.music = music

    def age(self):
        raise NotImplementedError("메소드를 구현해주셔야 합니다!")
    
    def info(self):
        return f"{self.name} 은/는 {self.music}을 발매했으며 "
    

class psy(Artist):

    def __init__(self, name, genre, rank = '1'):
        super().__init__(name,music='강남스타일')
        self.genre = genre
        self.rank = rank

    def age(self, old = 40):
        return f'{self.name}의 나이는 {old}살 입니다'
    
    def info(self):
        return super().info() + f'{self.genre}에서 {self.rank}등을 했습니다'

psy = psy('싸이','빌보드')
print(psy.age())
print(psy.info())
