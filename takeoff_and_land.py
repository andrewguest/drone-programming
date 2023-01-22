import asyncio

from mavsdk import System

from helpers import arming_helper, converters, precheck_helper


async def configure_and_takeoff(drone: System, altitude_feet):
    """Configure takeoff settings and then takeoff.

    Args:
        drone (System): Object representing the quadcopter (drone).
        altitude_feet (number): Altitude, in feet, for the initial takeoff.

    Returns:
        None
    """
    await drone.action.set_takeoff_altitude(
        converters.convert_feet_to_meters(altitude_feet)
    )
    await drone.action.takeoff()


async def run():
    """
    Main loop of the program
    """
    drone = System(mavsdk_server_address="localhost", port=50051)
    await drone.connect()

    # run flight checks before arming
    print("[...] Running prechecks")
    print("-" * 20)
    await precheck_helper.precheck_battery(drone)
    await precheck_helper.precheck_connection(drone)
    await precheck_helper.precheck_gps(drone)
    await precheck_helper.precheck_position(drone)
    print("-" * 20)

    # Get user confirmation before continuing
    continue_input = input("\n[?] Continue to arm the drone and then takeoff? (y/n): ")

    match continue_input.lower():
        case "y":
            print("[+] Continuing...")
        case "n":
            print("[!] Exiting...")
            await drone.action.terminate()
            exit()
        case _:
            print("[!] Unexpected input. Exiting...")
            await drone.action.terminate()
            exit()

    await arming_helper.arm_drone(drone)  # arm the drone
    await configure_and_takeoff(drone, 5)  # takeoff to 5ft
    await asyncio.sleep(10)  # sleep for 10 seconds
    await drone.action.land()  # land the drone


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
