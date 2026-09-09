#snake and ladder
import random
class Game():
    def __init__(self,name):
        self.name=name
        self.pos=0
        self.l={
            6:17,
            10:30,
            21:40,
            43:70,
            60:82,
            76:97
        }
        self.s={
            99:65,
            93:86,
            76:56,
            66:45,
            55:49,
            32:18,
            19:2
        }
    def roll(self):
        return random.randint(1,6)
    def move(self,dice):
        if self.pos==0:
            if dice==1:
                print(f"{self.name} has started the game")
                self.pos=1
            else:
                print("need 1 to start")
        else:
            if self.pos+dice <= 100:
                self.pos=self.pos+dice
            else:
                print("retry in next roll can't exceed 100")
        if self.pos in self.l:
            print(f"Ladder.......")
            self.pos=self.l[self.pos]
        elif self.pos in self.s:
            print(f"Snake........")
            self.pos=self.s[self.pos]
        print(f"{self.name} current position is {(self.pos)}")

        

p1=Game("player1")
p2=Game("player2")
print("....let's begin  the game....")
while p1.pos<=100 and p2.pos<=100:
    print(f"----------------------------------------------------------------------------------------------------")
    input("player1-presss enter to roll dice ")
    dice=p1.roll()
    print("Dice:",dice)
    p1.move(dice)
    if p1.pos==100:
        print("player1 wins...")
        break
    print(f"----------------------------------------------------------------------------------------------------")
    input("player2-presss enter to roll dice ")
    dice=p2.roll()
    print("Dice:",dice)
    p2.move(dice)
    if p2.pos==100:
        print("player2 wins...")
        break
