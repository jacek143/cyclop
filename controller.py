class Controller:
    def __init__(self, forward_speed, rotation_speed):
        self.__forward_seed = forward_speed
        self.__rotation_speed = rotation_speed
        self.__motor_settings = (0,0)
        self.__prev_know_error = None
    def process(self, error):
        if error is not None:
            self.__prev_know_error = error
            if abs(error) < 0.251:
                self.__motor_settings = (self.__forward_seed, self.__forward_seed)
            elif error < 0:
                self.__motor_settings = (-self.__rotation_speed, self.__rotation_speed)
            else:
                self.__motor_settings = (self.__rotation_speed, -self.__rotation_speed)
        return self.__motor_settings
