class Controller:
    def __init__(self, speed, gain):
        self.__speed = speed
        self.__gain = gain
        self.__motor_settings = (0,0)
        self.__prev_know_error = None
    def process(self, error):
        if error is not None:
            self.__prev_know_error = error
            diff = self.__gain * error
            self.__motor_settings = (self.__speed+diff, self.__speed-diff)
        elif self.__prev_know_error is not None:
            if abs(self.__prev_know_error) == 1:
                if self.__prev_know_error > 0:
                    self.__motor_settings = (self.__speed, -self.__speed)
                else:
                    self.__motor_settings = (-self.__speed, self.__speed)
        return self.__motor_settings
