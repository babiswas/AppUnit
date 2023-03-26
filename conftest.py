import pytest
from App1.model.Cars import Car
from App1.model.Trucks import Lorry
import logging

@pytest.fixture(scope="module")
def get_car():
    car=Car("Luxury","black",100,False,0)
    return car

@pytest.fixture(scope="function")
def car_move(get_car: Car):
    for i in range(10):
        get_car.run()
    return get_car

@pytest.fixture(scope="function")
def car_break(get_car: Car):
    for i in range(10):
        get_car.apply_break()
    return get_car

@pytest.fixture(scope="function",params=[2,3,4])
def speed_change(request,get_car: Car):
    get_car.speed+=request.param
    return get_car

@pytest.fixture
def change_gear(speed_change:Car):
    for i in range(10):
        speed_change.run()
    return speed_change

@pytest.fixture(scope="function")
def accelerate_car(request,get_car:Car):
    get_car.speed+=request.param
    return get_car
