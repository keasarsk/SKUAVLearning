#!/usr/bin/env python3

'''
    calibration 校准
'''

import asyncio
# 编写并发代码的库
# 高性能异步框架的基础
# 高性能一部框架的基础

from mavsdk import System


async def run():

    drone = System()
        # system对象drone
    await drone.connect(system_address="udp://:14540")
        # .connect() 将drone对象连接到远程系统

    print("-- Starting gyroscope(陀螺仪) calibration")
    async for progress_data in drone.calibration.calibrate_gyro():
                                    # .calibration.calibrate_gyro() 执行陀螺标定
        print(progress_data)
    print("-- Gyroscope calibration finished")

    print("-- Starting accelerometer(加速器) calibration")
    async for progress_data in drone.calibration.calibrate_accelerometer():
        print(progress_data)
    print("-- Accelerometer calibration finished")

    print("-- Starting magnetometer(磁力计) calibration")
    async for progress_data in drone.calibration.calibrate_magnetometer():
        print(progress_data)
    print("-- Magnetometer calibration finished")

    print("-- Starting board level horizon(地面水平线) calibration")
    async for progress_data in drone.calibration.calibrate_level_horizon():
        print(progress_data)
    print("-- Board level calibration finished")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
