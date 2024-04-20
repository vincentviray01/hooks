import pytest


@pytest.mark.parametrize("v", [float(n) for n in range(1, 10)])
def test_my_func(v: float):
    assert isinstance(v, float)
