# refer : http://dev.byrobot.co.kr/documents/kr/products/e_drone/library/python/e_drone/
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

def test(serial_port):
    drone = Drone()
    drone.open(serial_port)

    # takeOff
    drone.sendTakeOff()
    for i in range(5, 0, -1):
        sleep(1)

    # hovering
    for i in range(3, 0, -1):
        drone.sendControlWhile(0, 0, 0, 0 1000)
        sleep(0.01)

    # landing
    drone.sendLanding()
    for i in range(5, 0, -1):
        sleep(1)

    drone.close()

if __name__ == '__main__':
    serial_port = 
    test(serial_port)
