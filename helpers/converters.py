"""
Functions to help in convert one unit of measurement to another.
"""


def convert_mph_to_ms(miles_per_hour) -> float:
    """Convert a speed in miles per hour to meters per second
        since this is what MAVsdk expects.

    Args:
        miles_per_hour (number): A speed, in miles per hour, to be converted into meters per second.

    Returns:
        float: The converted (and rounded) speed in meters per second.
    """
    return round((miles_per_hour * 0.44704), 2)


def convert_feet_to_meters(feet) -> float:
    """Convert feet to meters, since that is what MAVsdk expects.

    Args:
        feet (number): The amount of feet to be converted into meters.

    Returns:
        float: The converted (and rounded) height in meters.
    """
    return round((feet * 0.3048), 2)


def convert_celcius_to_fahrenheit(celcius_temp):
    """Convert a temperature in Celcius to Fahrenheit

    Args:
        celcius_temp (number): Temperature in Celcius

    Returns:
        float: The temperature in Fahrenheit
    """

    return (celcius_temp * 9 / 5) + 32
