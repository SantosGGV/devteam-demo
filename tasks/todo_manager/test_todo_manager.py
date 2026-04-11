import pytest
from tasks.todo_manager import TodoManager

@pytest.fixture
def todo_manager():
    return TodoManager()

def test_add_task(todo_manager):
    todo_manager.add_task('Comprar leche')
    assert 'Comprar leche' in todo_manager.list_tasks()

def test_complete_task(todo_manager):
    todo_manager.add_task('Comprar leche')
    todo_manager.complete_task('Comprar leche')
    assert 'Comprar leche' not in todo_manager.list_tasks()

def test_delete_task(todo_manager):
    todo_manager.add_task('Comprar leche')
    todo_manager.delete_task('Comprar leche')
    assert 'Comprar leche' not in todo_manager.list_tasks()

def test_list_tasks(todo_manager):
    todo_manager.add_task('Comprar leche')
    assert 'Comprar leche' in todo_manager.list_tasks()