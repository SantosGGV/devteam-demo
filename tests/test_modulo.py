import pytest
from modulo import Stack

def test_stack_push_pop_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    with pytest.raises(IndexError):
        stack.pop()
