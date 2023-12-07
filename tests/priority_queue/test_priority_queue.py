from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0

    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 1})
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 3})

    assert len(priority_queue) == 4
    assert priority_queue.dequeue() == {"qtd_linhas": 4}
    assert priority_queue.dequeue() == {"qtd_linhas": 1}
    assert len(priority_queue) == 2

    assert priority_queue.search(0) == {"qtd_linhas": 3}

    with pytest.raises(IndexError):
        priority_queue.search(99)
