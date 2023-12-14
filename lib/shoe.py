#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._repaired = False
        self._condition = 'New'


    def get_size(self):
        print('retrieving size.') 
        return self._size
    
    def get_brand(self):
        print('retrieving brand.') 
        return self._brand

    def set_size(self, size):
        if isinstance(size, int):
            print(f"setting size to {size}")
            set._size = size

        else:
            print("size must be an integer")  

    def set_brand(self, brand):   
            print(f"setting brand to {brand}")
            set._brand = brand

    def  repaired (self):
         return self._repaired  
    
    def condition(self):
        return self._condition  

    def cobble(self):
        #print(f"The {self._brand} shoe has been repaired.")
        print('Your shoe is as good as new!')
        self._repaired = True
        self._condition = 'New' 

    def is_repaired(self):
        return self._repaired
    
    def get_condition(self):
        return self._condition       
    

    size = property(get_size, set_size) 
    brand = property(get_brand, set_brand)   
    repaired = property(is_repaired)
    condition = property(get_condition)          
        