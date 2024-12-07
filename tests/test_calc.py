import pytest
from mortgage import calculate_mortgage

def test_calculate_mortgage():
    result = calculate_mortgage(200000, 5, 30)
    assert round(result, 2) == 1073.64
