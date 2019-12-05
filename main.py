def compute_error(sensors_value):
    weights = [-4, -3, -2, -1, 1, 2, 3, 4]
    weighted = [weights[ind]*value for ind, value in enumerate(sensors_value) if value]
    if len(weighted):
        return sum(weighted)/(4*len(weighted))
    return None

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
from controller import Controller

sensors = SensorsArray()
motors = Motors(MotorDriver)
controller = Controller(10)

try:
    while(True):
        motors.set(controller.process(compute_error(sensors.value())))
except:
    motors.stop()
