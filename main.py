def compute_error(sensors_value):
    weights = [-4, -3, -2, -1, 1, 2, 3, 4]
    weighted = [weights[ind]*value for ind, value in enumerate(sensors_value) if value]
    if len(weighted):
        return sum(weighted)/(4*len(weighted))
    return None

class Controller:
    def __init__(self):
        self.speed = 15
        self.k = 15
    def process(self, error_value):
        return (self.speed+self.k*error_value,self.speed-self.k*error_value)

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
controller = Controller()
while(True):
    error_value = compute_error(sensors.value())
    if error_value is not None:
        motors.set(controller.process(error_value))
    else:
        motors.stop()
    
