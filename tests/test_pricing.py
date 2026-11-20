import pytest

from orderlab.pricing import subtotal


def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)
