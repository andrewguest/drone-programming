from mavsdk import System
from mavsdk.action import ActionError
from rich.console import Console

console = Console()
blue = "#5f5fff"
green = "#5fd700"
red = "#ff0000 "
white = "#ffffff"


async def arm_drone(drone: System):
    """
    Try to arm the drone and, if it arms, then return True.
    If the drone fails to arm, terminate and return False.
    """
    print("[+] Arming")
    try:
        await drone.action.arm()
        if drone.telemetry.armed():
            console.print(f"[{green}][!] Armed successfully![/{green}]")
            return True
    except ActionError as arming_error:
        console.print(f"[{red}][!] Drone failed to arm with error: {arming_error}.[/{red}]")
        console.print(f"[{red}][!] TERMINATING[/{red}]")
        await drone.action.terminate()
        return False
