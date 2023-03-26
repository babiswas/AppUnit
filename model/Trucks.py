class Lorry:

    def __init__(self,model:str="Heavy Duty",color:str="green",maxspeed:int=100,moving:bool=False,speed:int=0)->None:

        '''Truck model describing a truck'''

        self.model=model
        self.color=color
        self.max_speed=maxspeed
        self.moving=moving
        self.speed=speed

    def __str__(self)->str:

        '''Truck object to string'''

        return f"{self.model} and {self.color} and {self.max_speed} and {self.is_moving}"
    
    def is_moving(self)->bool:

        '''Check if the truck is moving'''

        return self.moving
    
    def current_speed(self)->int:

        '''Current speed of the truck'''

        return self.speed
    
    def run(self)->None:

        '''Increase the speed of the truck'''

        self.speed+=1

    def stop(self)->None:

        '''Stop the truck'''

        self.speed=0

    def apply_break(self)->None:

        '''Decrease the speed of the truck'''

        self.speed-=1