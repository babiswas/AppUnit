import pytest
from App1.model.Cars import Car
from App1.model.Trucks import Lorry
from App1.Garage import Garage

class TestVehicle:

    def test_car_movement(self,get_car: Car):
        assert get_car.color=="black"
        assert get_car.model=="Luxury"
        assert get_car.speed==0
        assert get_car.max_speed==100
        assert get_car.moving==False

    def test_car_speed1(self,car_move:Car):
        assert car_move.speed==10

    def test_car_speed2(self,car_break:Car):
        assert car_break.speed==0

    def test_car_speed3(self,car_move:Car):
        assert car_move.speed==10

    def test_car_speed4(self,car_move:Car):
        assert car_move.speed==20

    def test_car_speed5(self,car_break:Car):
        assert car_break.speed==10