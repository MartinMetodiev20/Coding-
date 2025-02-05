class extraterrestrial:
    def __init__(self,stomach,tentacles,hands,chainsaw,eyes,wings):
        self.stomach = stomach
        self.tentacles = tentacles
        self.hands = hands
        self.chainsaw = chainsaw
        self.eyes = eyes
        self.wings = wings

    def fly(self):
        print(f"Hello! Im extraterrestrial. I have  {self.stomach}stomaches and i have {self.wings} wings so i can fly .On my {self.hands} hands i have  {self.chainsaw} chainsaw with which i can cut my humans and swallow them better. With my  {self.eyes} eyes i can see them from far away.")

    def eat(self):
        print(f"I can eat a lot of humans with my  {self.stomach} stomaches")

    

Boo = extraterrestrial ("2","4","4","1","10","2")
Boo.fly()
Boo.eat()


