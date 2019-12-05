import pytest
from controller import Controller

def test_if_goes_straight_with_given_speed_if_line_in_the_middle():
    controller = Controller(speed=25)
    assert (25,25) == controller.process(0)

def test_if_does_not_start_when_no_line():
    controller = Controller(speed=10)
    assert (0, 0) == controller.process(None)
