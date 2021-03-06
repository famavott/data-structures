"""Tests for Stack Class."""


def test_stack_init_empty():
    """Test initialization of Stack with no values passed."""
    from stack import Stack
    test_stack = Stack()
    assert test_stack._length == 0


def test_stack_push_one_node():
    """Test initializing stack with a value creates head node."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(1)
    assert test_stack._linkedlist.head.data == 1


def test_stack_pop_one_node():
    """Test that popping a stack of one node works correctly."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(2)
    test_stack.push(1)
    test_stack.pop()
    assert test_stack._linkedlist.head.data == 2


def test_stack_init_with_iterable():
    """Test that initializing stack with iterable has correct nodes."""
    from stack import Stack
    test_stack = Stack([1, 2, 3])
    assert test_stack._linkedlist._length == 3


def test_stack_pop_empty():
    """."""
    from stack import Stack
    test_stack = Stack()
    assert test_stack.pop() is None
