"""
Helper functions for using the Raspberry Pi Sense HAT.
"""

from typing import Tuple

from sense_hat import SenseHat

from helpers import converters


SENSE_HAT = SenseHat()


def show_message(message: str, scroll_speed: float = 0.2):
    """Displays a scrolling message on the Sense HAT.

    Args:
        message (str): Message to display.
        scroll_speed (float, optional): The time paused for between shifting the text to the left by one column of pixels. Defaults to 0.2.
    """

    SENSE_HAT.clear()

    SENSE_HAT.show_message(message, scroll_speed)


def draw_check_mark(color: Tuple[int, int, int] = (0, 255, 0)):
    """Draw a check mark on the Sense HAT in the provided color (R, G, B)

    Args:
        color (Tuple[int, int, in], optional): The (R, G, B) color value to draw the check mark in. Defaults to (0, 255, 0).
    """

    SENSE_HAT.clear()

    X = color
    O = (0, 0, 0)  # blank

    # fmt: off
    logo = [
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, X,
        O, O, O, O, O, O, X, O,
        O, X, O, O, O, X, O, O,
        O, O, X, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
    ]
    # fmt: on

    SENSE_HAT.set_pixels(logo)


def draw_x(color: Tuple[int, int, int] = (255, 0, 0)):
    """Draw an X on the Sense HAT in the provided color (R, G, B)

    Args:
        color (Tuple[int, int, in], optional): The (R, G, B) color value to draw the check mark in. Defaults to (255, 0, 0).
    """

    SENSE_HAT.clear()

    X = color
    O = (0, 0, 0)  # blank

    # fmt: off
    logo = [
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O,
        O, X, O, O, O, O, X, O, 
        O, O, X, O, O, X, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, X, O, O, O, O, X, O,
    ]
    # fmt: on

    SENSE_HAT.set_pixels(logo)


def get_pressure():
    return SENSE_HAT.get_pressure()


def get_temperature():
    temp = SENSE_HAT.get_temperature()

    return converters.convert_celcius_to_fahrenheit(temp)


def get_humidity():
    return SENSE_HAT.get_humidity()


def get_accelerometer():
    return SENSE_HAT.get_accelerometer()


def get_compass():
    return SENSE_HAT.get_compass()


def get_orientation():
    return SENSE_HAT.get_orientation()


def get_gyroscope():
    return SENSE_HAT.get_gyroscope()
