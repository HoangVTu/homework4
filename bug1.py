class Base:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
    def shape(self):
        return "Base shape"
    def draw(self):
        return "Drawn from base shape"

class Circle(Base):
    def __init__(self, x, y,size):
        super().__init__(x, y, size)

    def shape(self):
        return "Circle Shape"

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """

def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())

main()