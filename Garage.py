from App1.model.Cars import Car
from App1.model.Trucks import Lorry

class GarageFull(Exception):

    def __init__(self,message:str)->None:
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    
class EmptyGarage(Exception):

    def __init__(self,message:str)->None:
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class Garage:

    '''Garage for parking a car'''

    def __init__(self,*vehicle)->None:

        '''Garage constructor'''

        self.car_list=list()
        self.truck_list=list()
        for obj in vehicle:
            if isinstance(obj,Car):
                self.car_list.append(obj)
            elif isinstance(obj,Lorry):
                self.truck_list.append(obj)

    def is_empty(self)->bool:

        '''Check if the garage is empty'''

        return list(self.car_list)==0 and list(self.truck_list)==0
    
    def total_cars(self)->int:

        '''Number of car in garage'''

        return len(self.car_list)
    
    def total_truck(self)->int:

        '''Number of trucks'''

        return len(self.truck_list)
    
    def park_car(self)->None:
         
        '''Park a car in the garage'''

        if len(self.car_list)>100 or len(self.car_list)==100:
            raise GarageFull("Garage is full")
        self.car_list.append(Car())

    def park_truck(self)->None:

        '''Park a truck in the garage'''
        
        if len(self.truck_list)>100 or len(self.truck_list)==100:
            raise GarageFull("Garage is full")
        self.truck_list.append(Lorry())

    def unpark_car(self)->None:

        '''Unpark a car'''

        if len(self.car_list)==0:
            raise EmptyGarage("Garage is empty")
        self.car_list.pop()

    def unpark_truck(self)->None:

        '''Unpark a truck'''

        if len(self.truck_list)==0:
            raise EmptyGarage("Garage is empty")
        self.truck_list.pop()
    

    
    