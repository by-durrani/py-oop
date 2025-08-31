# DUNDER METHODS

# class Person:
#     def __init__(self, name:str, age:int): ## __init__ or __main__ so the __ double underscore is called dunder method __init__ is a constructor
#         self.name:str  = name
#         self.age:int = age
    
#     def getUserData(self):
#         return f"{self.name} {self.age}"
    
# p = Person('ali', 22)

# class Vector:
    
#     def __call__(self, *args, **kwds):
#         print('Hello i was called', args, kwds)
    
#     def __init__(self, x:int, y:int):
#         self.x = x 
#         self.y = y
        
#     def __add__(self, other_vec):
#         return Vector(self.x + other_vec.x, self.y + other_vec.y) ## returns another instance of vector with property x and y which has sum of both x with x and y with y

#     def __repr__(self):
#         return f"X: {self.x}, Y: {self.y}"
    
#     def __len__(self):
#         return 10

# v1 = Vector(10, 20)
# v2 = Vector(50, 60)

# v3 = v1 + v2 ## when we add two classes and have a __add__ or any dunder method in it python knows what to do with this first element is first i.e "self" param of __add__ on line 16 and second element is "other_vec"
# print(v3) -> X: 60, Y: 80 
# print(v3) ## print does convert any thing or object into a string if its a number or string it shows directly and if its something else it shows the memory address of that object but in class case it calls __str__ method of that class if exists and if don't it goes to __repr__ method and calls that class instance method
# print(v3.x)
# print(v3.y) 

# print(len(v3))

# v3(2,3, len=3, object=0)


# DECORATORS
    