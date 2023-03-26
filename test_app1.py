import pytest
from App1.model.Cars import Car
from App1.Garage import Garage

@pytest.fixture
def get_car_list()->list[Car]:

    car_list=[Car("Suv","Red",100,False,0),Car("HeavyDuty","White",200,False,0),Car("Luxury","Black",100,False,0)]
    return car_list

def test_total_cars_garage(get_car_list: list[Car]):

    garage=Garage(*get_car_list)
    assert garage.total_cars()==3

def test_car_speed(get_car_list: list[Car]):

    l=get_car_list
    assert l[0].current_speed()==0
    l[0].run()
    assert l[0].current_speed()==1
    l[0].run()
    assert l[0].current_speed()==2

def test_car_movement(get_car_list: list[Car]):

    l=get_car_list
    assert l[1].is_moving()==False
    assert l[1].color=="White"

def test_default_car():

    cr=Car()
    assert cr.color=="green"
    assert cr.max_speed==100
    assert cr.moving==False
    assert cr.model=="Luxury"

def test_car_parking(get_car_list: list[Car]):

    garage=Garage(*get_car_list)
    garage.park_car()
    assert garage.car_list[-1].color=="green"
    assert garage.car_list[-1].max_speed==100
    assert garage.car_list[-1].moving==False
    assert garage.car_list[-1].model=="Luxury"

def test_total_cars(get_car_list: list[Car]):

    get_car_list.append(Car())
    assert len(get_car_list)==4
    get_car_list.pop()
    assert len(get_car_list)==3

def test_empty_garage(get_car_list: list[Car]):

    get_car_list.clear()
    assert len(get_car_list)==0


















