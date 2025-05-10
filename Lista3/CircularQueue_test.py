import pytest
from CircularQueue import CircularQueue  # substitua pelo nome do seu arquivo real (sem .py)

def test_enqueue_and_dequeue():
    q = CircularQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30

def test_front_and_rear():
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.front() == 1
    assert q.rear() == 3

def test_is_empty_and_is_full():
    q = CircularQueue(2)
    assert q.is_empty()
    q.enqueue(5)
    assert not q.is_empty()
    q.enqueue(10)
    assert q.is_full()

def test_circular_behavior():
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    q.enqueue(4)  # aqui o rear deve voltar pro início
    assert q.front() == 2
    assert q.rear() == 4
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty()

def test_enqueue_on_full_raises():
    q = CircularQueue(2)
    q.enqueue(1)
    q.enqueue(2)
    with pytest.raises(OverflowError):
        q.enqueue(3)

def test_dequeue_on_empty_raises():
    q = CircularQueue(2)
    with pytest.raises(IndexError):
        q.dequeue()

def test_front_on_empty_raises():
    q = CircularQueue(2)
    with pytest.raises(IndexError):
        q.front()

def test_rear_on_empty_raises():
    q = CircularQueue(2)
    with pytest.raises(IndexError):
        q.rear()
