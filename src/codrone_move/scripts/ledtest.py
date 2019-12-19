#!/usr/bin/env python
from time import sleep

from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':

    drone = Drone()
    drone.open()


    drone.sendLightManual(DeviceType.Drone, 0xFF, 0)
    sleep(1);


    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyRed.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyRed.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyRed.value, 0)
    sleep(1);

    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyGreen.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyGreen.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyGreen.value, 0)
    sleep(1);

    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyBlue.value, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyBlue.value, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, LightFlagsDrone.BodyBlue.value, 0)
    sleep(1);


    drone.sendLightManual(DeviceType.Drone, 0x06, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x06, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x06, 0)
    sleep(1);

    drone.sendLightManual(DeviceType.Drone, 0x0A, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x0A, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x0A, 0)
    sleep(1);

    drone.sendLightManual(DeviceType.Drone, 0x0C, 10)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x0C, 100)
    sleep(1);
    
    drone.sendLightManual(DeviceType.Drone, 0x0C, 0)
    sleep(1);


    drone.close()
