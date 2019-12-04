def error(sensors_value):
    weights = [-4, -3, -2, -1, 1, 2, 3, 4]
    weighted = [weights[ind]*value for ind, value in enumerate(sensors_value) if value]
    if len(weighted):
        return sum(weighted)/(4*len(weighted))
    return None

def controller(error_value):
    if error_value is None:
        return None
    speed = 20
    k = 10
    return (speed+k*error_value,speed-k*error_value)

class Motors:
    def __init__(self, motor_driver):
        self.__driver = motor_driver()
    def set(self, speeds):
        self.__driver.MotorRun(1, 'forward', speeds[0])
        self.__driver.MotorRun(0, 'forward', speeds[1])
    def stop(self):
        self.__driver.MotorStop(0)
        self.__driver.MotorStop(1)
        
from sensors_array import SensorsArray
from motor_driver import MotorDriver

sensors = SensorsArray()
motors = Motors(MotorDriver)
while(True):
    error_value = error(sensors.value())
    speeds = controller(error_value)
    print(speeds)
    if speeds is not None:
        motors.set(speeds)
    else:
        motors.stop()
