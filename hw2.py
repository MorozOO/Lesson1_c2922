import random
class cat:
    hp = 100
    eat = 100
    name = ""
    def __init__(self,n):
        self.name = n
        print(self.name,"hello")
        self.live()
        self.live()
        self.eateng()
    def eateng(self):
        self.eat += 10
        print(self.eat)
    def live(self):
        self.eat -=5
        print(self.eat)
    def damsge(self):
        self.hp -=25
murzik = cat("Murzik")