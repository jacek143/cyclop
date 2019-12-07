import pytest
from controller import Controller

@pytest.fixture
def controller():
    arbitrary_forward_speed = 10
    arbitrary_rotation_speed = 3
    return Controller(forward_speed=arbitrary_forward_speed, rotation_speed=arbitrary_rotation_speed)

def test_if_goes_straight_with_given_speed_if_line_in_the_middle():
    rotation_speed = 13
    forward_speed = 7
    controller = Controller(forward_speed=7, rotation_speed=rotation_speed)

    assert (forward_speed, forward_speed) == controller.process(0.25)
    assert (forward_speed, forward_speed) == controller.process(0.20)
    assert (forward_speed, forward_speed) == controller.process(0)
    assert (forward_speed, forward_speed) == controller.process(-0.20)
    assert (forward_speed, forward_speed) == controller.process(-0.25)

def test_if_does_not_start_when_no_line(controller):
    assert (0, 0) == controller.process(None)

def test_if_rotates_when_line_not_in_the_middle():
    rotation_speed = 13
    forward_speed = 7
    controller = Controller(forward_speed=7, rotation_speed=rotation_speed)
    
    assert (rotation_speed, -rotation_speed) == controller.process(1)
    assert (rotation_speed, -rotation_speed) == controller.process(0.5)
    assert (rotation_speed, -rotation_speed) == controller.process(0.251)
    assert (-rotation_speed, rotation_speed) == controller.process(-0.251)
    assert (-rotation_speed, rotation_speed) == controller.process(-0.5)
    assert (-rotation_speed, rotation_speed) == controller.process(-1)

def test_if_keep_going_when_line_disappears(controller):
    arbitrary_error = 0.39
    old_speed = controller.process(arbitrary_error)
    assert old_speed == controller.process(None)
