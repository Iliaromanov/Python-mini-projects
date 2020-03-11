from robot import Robot

def test__str__():
    a = Robot("blue", 200, 10)
    assert str(a) == "blue 200 10 100"


def test_punch():
    a = Robot("blue", 200, 10)
    b = Robot("red", 100, 5)
    a.punch(b)
    assert b.health == 90

    b.punch(a)
    assert a.health == 95


def test_recharge():
    a = Robot("blue", 200, 10)
    a.recharge()
    assert a.health == 110
