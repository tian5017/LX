_EPSILON = 1e-8


def is_zero(x):
    return abs(x) < _EPSILON


def is_equal(x, y):
    return abs(x - y) < _EPSILON