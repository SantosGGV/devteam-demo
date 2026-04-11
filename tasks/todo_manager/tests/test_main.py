from main import todo_manager
import pytest

@pytest.fixture
def reset_todo_manager():
    todo_manager.tasks = []

def test_add_task(reset_todo_manager):
    todo_manager.add_task("Tarea 1")
    assert len(todo_manager.tasks) == 1

def test_complete_task(reset_todo_manager):
    todo_manager.add_task("Tarea 1")
    todo_manager.complete_task(0)
    assert todo_manager.tasks[0]["completed"] == True

def test_delete_task(reset_todo_manager):
    todo_manager.add_task("Tarea 1")
    todo_manager.delete_task(0)
    assert len(todo_manager.tasks) == 0

def test_list_tasks(reset_todo_manager):
    todo_manager.add_task("Tarea 1")
    todo_manager.add_task("Tarea 2")
    assert len(todo_manager.list_tasks()) == 2