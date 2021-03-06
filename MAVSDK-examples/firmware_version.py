#!/usr/bin/env python3

'''
    firmware version 固件版本
'''
import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    info = await drone.info.get_version()
                    # info.get_version()  Get the version information of the system.
    print(info)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
