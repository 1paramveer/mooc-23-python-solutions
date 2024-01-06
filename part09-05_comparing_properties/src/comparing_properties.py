# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        return False
    
    def price_difference(self, compared_to):
        priceOriginal = self.square_metres * self.price_per_sqm
        priceCompared = compared_to.square_metres * compared_to.price_per_sqm

        if  priceOriginal > priceCompared:
            return priceOriginal - priceCompared
        return priceCompared - priceOriginal
    
    def more_expensive(self, compared_to):
        priceOriginal = self.square_metres * self.price_per_sqm
        priceCompared = compared_to.square_metres * compared_to.price_per_sqm

        if  priceOriginal > priceCompared:
            return True
        return False
        
