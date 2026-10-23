class animal():
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can move and run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
o1 = human()
o2 = snake()
o3 = dog()
o4 = lion()
o1.move()
o2.move()
o3.move()
o4.move()

