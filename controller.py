class Controller:
    def __init__(self, speed, gain):
        self.__speed = speed
        self.__gain = gain
        self.__motor_settings = (0,0)
    def process(self, error):
        if error is not None:
            diff = self.__gain * error
            self.__motor_settings = (self.__speed+diff, self.__speed-diff)
        return self.__motor_settings
