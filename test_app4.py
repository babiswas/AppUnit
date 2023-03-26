import pytest
from App1.model.Cars import Car
from App1.model.Trucks import Lorry
from App1.Garage import Garage




class Test_Speed:
    value=0
    expected=[12,25,39]

    def test_speed_car(self,change_gear:Car):
        assert change_gear.speed== Test_Speed.expected[Test_Speed.value]
        Test_Speed.value+=1
        if Test_Speed.value==3:
            Test_Speed.value=0

    @pytest.mark.parametrize("loop_count,expected",[(1,10),(2,20),(3,30)],)
    def test_vehicle_speed(self,loop_count,expected):
        mycar=Car()
        for i in range(loop_count*10):
            mycar.run()
        assert mycar.speed==expected

    

    
