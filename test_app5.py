import pytest
from App1.model.Cars import Car
from App1.model.Trucks import Lorry

class Test_Carspeed:
    value=0
    result=[2,5,9,14]

    @pytest.mark.parametrize("accelerate_car",[2,3,4,5],indirect=True)
    def test_vehc_speed(self,accelerate_car:Car):
        assert accelerate_car.speed==Test_Carspeed.result[Test_Carspeed.value]
        Test_Carspeed.value+=1
        if Test_Carspeed.value==len(Test_Carspeed.result):
            Test_Carspeed.value=0




