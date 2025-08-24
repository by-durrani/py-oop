# class Person:
#     def __init__(self, name:str, age:int): ## __init__ or __main__ so the __ double underscore is called dunder method __init__ is a constructor
#         self.name:str  = name
#         self.age:int = age
    
#     def getUserData(self):
#         return f"{self.name} {self.age}"
    
# p = Person('ali', 22)

class Vector:
    def __init__(self, x:int, y:int):
        self.x = x 
        self.y = y
        
    def __add__(self, other_vec):
        return Vector(self.x + other_vec.x, self.y + other_vec.y) ## returns another instance of vector with property x and y which has sum of both x with x and y with y

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
 
v1 = Vector(10, 20)
v2 = Vector(50, 60)

v3 = v1 + v2 ## when we add two classes and have a __add__ or any dunder method in it python knows what to do with this first element is first i.e "self" param of __add__ on line 16 and second element is "other_vec"

print(v3)
# print(v3.x)
# print(v3.y) 