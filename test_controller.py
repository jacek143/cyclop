import pytest
from controller import Controller

def test_if_robot_goes_straight_if_line_in_the_middle():
    speed = 30
    controller = Controller(speed)
    error = 0
    assert (speed,speed) == controller.process(error)

def test_if_does_not_start_when_no_line():
    speed = 20
    controller = Controller(speed)
    assert (0, 0) == controller.process(None)
