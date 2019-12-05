import pytest
from controller import Controller

@pytest.fixture
def controller():
    arbitrary_speed = 10
    arbitrary_gain = 3
    return Controller(speed=arbitrary_speed, gain=arbitrary_gain)

def test_if_goes_straight_with_given_speed_if_line_in_the_middle(controller):
    (left, right) = controller.process(0)
    assert left == right
    assert left > 0

def test_if_does_not_start_when_no_line(controller):
    assert (0, 0) == controller.process(None)

def test_if_turns_left_when_line_on_the_left(controller):
    (left, right) = controller.process(-0.3)
    assert left < right

def test_if_controller_is_linear():
    speed = 10
    gain = 3
    error = 0.3
    controller = Controller(speed, gain)
    (left, right) = controller.process(error)
    assert left == speed + gain * error
    assert right == speed - gain * error
