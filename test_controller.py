import pytest
from controller import Controller

@pytest.fixture
def controller():
    arbitrary_speed = 10
    return Controller(speed=arbitrary_speed)

def test_if_goes_straight_with_given_speed_if_line_in_the_middle():
    controller = Controller(speed=25)
    assert (25,25) == controller.process(0)

def test_if_does_not_start_when_no_line(controller):
    assert (0, 0) == controller.process(None)

def test_if_turns_left_when_line_on_the_left(controller):
    (left, right) = controller.process(-0.3)
    assert left < right
