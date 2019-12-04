from gpiozero import LineSensor

class SensorsArray:
    def __init__(self):
        self.__sensors = [LineSensor(gpio_id) for gpio_id in [16, 23, 25, 22, 24, 6, 5, 26]]
    def value(self):
        return [sensor.value for sensor in self.__sensors]
