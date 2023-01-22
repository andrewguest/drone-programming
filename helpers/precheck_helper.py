"""
Functions to perform different type of pre-checks (for safety reasons) and
    print the results of the checks.
"""


from mavsdk import System
from rich.console import Console


console = Console()
blue = "#5f5fff"
green = "#5fd700"
red = "#ff0000 "
white = "#ffffff"


async def precheck_battery(drone: System):
    battery_info = drone.telemetry.battery()
    battery_info = await anext(battery_info)

    console.print(
        f"[{blue}]Battery voltage:[/{blue}] [{white}]{round(battery_info.voltage_v, 2)}v[/{white}]"
    )
    console.print(
        f"[{blue}]Battery percentage:[/{blue}] [{white}]{battery_info.remaining_percent} %[/{white}]"
    )


async def precheck_connection(drone: System):
    connection_state = drone.core.connection_state()
    connection_state = await anext(connection_state)

    if connection_state.is_connected:
        console.print(
            f"[{blue}]Connection state:[/{blue}] [{green}]Connected[/{green}]"
        )
    else:
        console.print(
            f"[{blue}]Connection state:[/{blue}] [{red}]Disconnected[/{red}]"
        )


async def precheck_gps(drone):
    gps = drone.telemetry.gps_info()
    gps = await anext(gps)

    console.print(
        f"[{blue}]Number of GPS satellites:[/{blue}] [{white}]{gps.num_satellites}[/{white}]"
    )
    console.print(
        f"[{blue}]GPS fix type:[/{blue}] [{white}]{gps.fix_type}[/{white}]"
    )


async def precheck_position(drone):
    position = drone.telemetry.position()
    position = await anext(position)

    console.print(
        f"[{blue}]Latitude:[/{blue}] [{white}]{position.latitude_deg:.4f}[/{white}]"
    )
    console.print(
        f"[{blue}]Longitude:[/{blue}] [{white}]{position.longitude_deg:.4f}[/{white}]"
    )
    console.print(
        f"[{blue}]Absolute altitude (meters):[/{blue}] [{white}]{position.absolute_altitude_m:.4f} meters[/{white}]"
    )
    console.print(
        f"[{blue}]Relative altitude (meters):[/{blue}] [{white}]{position.relative_altitude_m:.4f} meters[/{white}]"
    )
