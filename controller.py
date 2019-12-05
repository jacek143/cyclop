class Controller:
    def __init__(self, speed):
        self.__speed = speed
    def process(self, error):
        if error is None:
            return (0, 0)
        return (self.__speed*(1+error), self.__speed*(1-error))
