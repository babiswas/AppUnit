import pytest
from App1.model.Cars import Car
from App1.model.Trucks import Lorry
from App1.Garage import Garage,GarageFull,EmptyGarage


class TestTruck:

    def test_no_vehicles(self):
        l=[Car() for i in range(3)]
        m=[Lorry() for i in range(3)]
        l.extend(m)
        garage=Garage(*l)
        assert len(garage.car_list)==3
        assert len(garage.truck_list)==3
        assert garage.is_empty()==False

    def test_no_cars(self):
        l=[Car() for i in range(3)]
        garage=Garage(*l)
        assert len(garage.car_list)==3
        garage.park_car()
        assert len(garage.car_list)==4
        assert len(garage.truck_list)==0
        garage.park_truck()
        assert len(garage.truck_list)==1

    def test_add_car_exception(self):
        l=[Car() for i in range(100)]
        garage1=Garage(*l)
        assert len(garage1.car_list)==100
        with pytest.raises(GarageFull):
            garage1.park_car()

    def test_add_truck_exception(self):
        l=[Lorry() for i in range(100)]
        mygarage=Garage(*l)
        assert len(mygarage.truck_list)==100
        with pytest.raises(GarageFull):
            mygarage.park_truck()

    def test_unpark_car(self):
        l=[Lorry() for i in range(10)]
        garage2=Garage(*l)
        assert len(garage2.truck_list)==10
        with pytest.raises(EmptyGarage):
            garage2.unpark_car()
        garage2.park_car()
        assert len(garage2.car_list)==1
        garage2.unpark_car()
        with pytest.raises(EmptyGarage):
            garage2.unpark_car()


    def test_unpark_truck(self):
        l=[Car() for i in range(10)]
        garage2=Garage(*l)
        assert len(garage2.car_list)==10
        with pytest.raises(EmptyGarage):
            garage2.unpark_truck()
        garage2.park_truck()
        assert len(garage2.truck_list)==1
        garage2.unpark_truck()
        with pytest.raises(EmptyGarage):
            garage2.unpark_truck()

    def test_car_attributes(self):
        c=Car()
        assert hasattr(c,"model")
        assert hasattr(c,"color")
        assert hasattr(c,"max_speed")
        assert hasattr(c,"speed")
        assert hasattr(c,"moving")

    def test_truck_attributes(self):
        l=Lorry()
        assert hasattr(l,"model")
        assert hasattr(l,"color")
        assert hasattr(l,"max_speed")
        assert hasattr(l,"speed")
        assert hasattr(l,"moving")

    def test_garage_attributes(self):
        cars=[Car() for i in range(10)]
        lorry=[Lorry() for i in range(20)]
        m=list()
        m.extend(cars)
        m.extend(lorry)
        garage3=Garage(*m)
        assert hasattr(garage3,"car_list")
        assert hasattr(garage3,"truck_list")

    



