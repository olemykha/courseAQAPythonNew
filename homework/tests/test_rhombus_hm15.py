from homework.homework15.homework_15_01 import Rhombus


def test_valid_construction():
    r = Rhombus(side_a=5.0, angle_a=60.0)
    assert r.side_a == 5.0
    assert r.angle_a == 60.0
    assert r.angle_b == 120.0


def test_reassign_angle_a_updates_angle_b():
    r = Rhombus(side_a=4, angle_a=45)
    r.angle_a = 90
    assert r.angle_a == 90
    assert r.angle_b == 90
