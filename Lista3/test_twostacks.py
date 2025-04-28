import pytest
from Queue_TwoStacks import QueueTwoStacks  # ajuste o nome conforme seu arquivo

def test_enqueue_and_front():
    queue = QueueTwoStacks()
    queue.enqueue(10)
    assert queue.front() == 10
    queue.enqueue(20)
    assert queue.front() == 10
    queue.enqueue(30)
    assert queue.front() == 10

def test_dequeue():
    queue = QueueTwoStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    with pytest.raises(IndexError):
        queue.dequeue()

def test_front_empty():
    queue = QueueTwoStacks()
    with pytest.raises(IndexError):
        queue.front()

def test_is_empty():
    queue = QueueTwoStacks()
    assert queue.is_empty()
    queue.enqueue(5)
    assert not queue.is_empty()
    queue.dequeue()
    assert queue.is_empty()

@pytest.mark.parametrize(
    "sequence, expected_order",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([10, 20], [10, 20]),
        ([], []),
    ]
)
def test_enqueue_dequeue_sequence(sequence, expected_order):
    queue = QueueTwoStacks()
    for value in sequence:
        queue.enqueue(value)
    for expected in expected_order:
        assert queue.dequeue() == expected
    assert queue.is_empty()
