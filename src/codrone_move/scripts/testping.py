from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone(False)
    drone.open()

    drone.sendPing(DeviceType.Controller)

    timeStart = time.time()

    while True:
        sleep(0.01)
        dataType = drone.check()

        if dataType == DataType.Ack:
            ack = drone.getData(DataType.Ack)
            print "{0} / {1} / {2:04X}".format(ack.dataType.name, ack.systemTime, ack.crc16)
            print "T: {0}".format(time.time() - timeStart)
            break

        if time.time() > timeStart + 1:
            print "Time Over"
            break

    drone.close()
