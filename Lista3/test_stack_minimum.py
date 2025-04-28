import pytest
from StackO1_time import StackMinimum  

@pytest.mark.parametrize(
    "inputs, expected_tops",
    [
        ([5, 3, 7], [5, 3, 7]),
        ([1, 2, 0, 4], [1, 2, 0, 4]),
        ([10], [10]),
    ]
)
def test_push_and_get_top(inputs, expected_tops):
    stack = StackMinimum()
    for i, value in enumerate(inputs):
        stack.push(value)
        assert stack.get_top() == expected_tops[i]

@pytest.mark.parametrize(
    "inputs, expected_mins",
    [
        ([5, 3, 7], [5, 3, 3]),
        ([2, 2, 2], [2, 2, 2]),
        ([10, 9, 8], [10, 9, 8]),
        ([5, 1, 6, 0], [5, 1, 1, 0]),
    ]
)
def test_get_min(inputs, expected_mins):
    stack = StackMinimum()
    for i, value in enumerate(inputs):
        stack.push(value)
        assert stack.get_min() == expected_mins[i]

def test_pop_behavior():
    stack = StackMinimum()
    stack.push(2)
    stack.push(1)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.get_min() == 1
    assert stack.pop() == 1
    assert stack.get_min() == 2
    assert stack.pop() == 2
    assert stack.is_empty()
    with pytest.raises(IndexError):
        stack.pop()

def test_get_top_empty():
    stack = StackMinimum()
    with pytest.raises(IndexError):
        stack.get_top()

def test_get_min_empty():
    stack = StackMinimum()
    with pytest.raises(IndexError):
        stack.get_min()

@pytest.mark.parametrize(
    "push_sequence, expected_stack",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([7, 5], [7, 5]),
        ([], []),
    ]
)
def test_get_stack(push_sequence, expected_stack):
    stack = StackMinimum()
    for value in push_sequence:
        stack.push(value)
    assert stack.get_stack() == expected_stack