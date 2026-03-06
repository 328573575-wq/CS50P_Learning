from unit_test_learn.calculate import sequare

def test_positive():
    assert sequare(2) == 4
    assert sequare(3) == 9

def test_negative():
    assert sequare(-2) == 4
    assert sequare(-3) == 9
def test_zero():
    assert sequare(0) == 0

    