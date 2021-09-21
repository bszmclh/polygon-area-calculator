class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __str__(self) -> str:
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return (self.width **2 + self.height **2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        str = ""
        for i in range(self.height):
            str += "*" * self.width + "\n"
        
        return str

    def get_amount_inside(self, shape):
        return int(self.width / shape.width) * int(self.height / shape.height)

    

class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side
    
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def __str__(self) -> str:
        return "Square(side=" + str(self.width)+")"

