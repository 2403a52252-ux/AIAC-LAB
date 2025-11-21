import pytest
from task2 import ParcelHistoryStack

def test_initial_state_empty():
    s = ParcelHistoryStack()
    assert s.is_empty() is True
    assert s.size() == 0
    assert s.peek() is None
    assert s.pop() is None

def test_push_updates_size_and_peek():
    s = ParcelHistoryStack()
    s.push("Picked up")
    assert s.is_empty() is False
    assert s.size() == 1
    assert s.peek() == "Picked up"

def test_pop_returns_most_recent_and_updates_size():
    s = ParcelHistoryStack()
    s.push("A")
    s.push("B")
    s.push("C")
    assert s.size() == 3
    assert s.pop() == "C"
    assert s.size() == 2
    assert s.peek() == "B"
    assert s.pop() == "B"
    assert s.pop() == "A"
    assert s.pop() is None
    assert s.is_empty() is True

def test_limit_keeps_only_latest_10():
    s = ParcelHistoryStack()
    # push 12 items, names item0 .. item11
    for i in range(12):
        s.push(f"item{i}")
    # size must be limited to 10
    assert s.size() == 10
    # The oldest two (item0, item1) should have been discarded,
    # so popping returns item11 down to item2
    popped = [s.pop() for _ in range(10)]
    expected = [f"item{i}" for i in range(11, 1, -1)]
    assert popped == expected
    assert s.is_empty() is True

def test_peek_on_empty_and_after_operations():
    s = ParcelHistoryStack()
    assert s.peek() is None
    s.push("X")
    assert s.peek() == "X"
    s.push("Y")
    assert s.peek() == "Y"
    s.pop()
    assert s.peek() == "X"
    s.pop()
    assert s.peek() is None