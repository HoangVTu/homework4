class Base:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x,y,size):
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

