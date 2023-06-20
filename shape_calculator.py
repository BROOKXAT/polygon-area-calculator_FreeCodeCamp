class Rectangle:
    def __init__(self, width ,height ) :
        self.width = width 
        self.height = height
    def set_width(self,width) :
        self.width = width 

    def set_height(self,height) :
        self.height = height
        
    def __str__(self ) :
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

    def get_area(self): return (self.width * self.height)
        
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self): 
        return  ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self) : 
        if self.width >50 or self.height > 50 :
            return  "Too big for picture."
        picture =  "*"*self.width+"\n"
        return picture*self.height

    def get_amount_inside(self,shape) :
        x = self.width // shape.width
        y = self.height // shape.height
        return x*y
    
        

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f'Square(side={self.width})'
        
    def set_side(self, new_side_length):
        self.width = new_side_length
        self.height = new_side_length