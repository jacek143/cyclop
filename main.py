def error(sensors_value):
    weights = [-4, -3, -2, -1, 1, 2, 3, 4]
    weighted = [weights[ind]*value for ind, value in enumerate(sensors_value) if value]
    if len(weighted):
        return sum(weighted)/len(weighted)
    return None

from sensors_array import SensorsArray

sensors = SensorsArray()
while(True):
    print(error(sensors.value()))
