def error(sensors_value):
    weights = [-4, -3, -2, -1, 1, 2, 3, 4]
    weighted = [weights[ind]*value for ind, value in enumerate(sensors_value) if value]
    if len(weighted):
        return sum(weighted)/(4*len(weighted))
    return None

def controller(error_value):
    speed = 20
    k = 10
    return (speed+k*error_value,speed-k*error_value)

from sensors_array import SensorsArray
from motor_driver import MotorDriver

sensors = SensorsArray()
motor_driver = MotorDriver()
while(True):
    error_value = error(sensors.value())
    print(error_value)
