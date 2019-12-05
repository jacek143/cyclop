class Controller:
    def __init__(self, speed, gain):
        self.__speed = speed
        self.__gain = gain
    def process(self, error):
        if error is None:
            return (0, 0)
        diff = self.__gain * error
        return (self.__speed+diff, self.__speed-diff)
