from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from task_manager.repository import TaskRepository
from task_manager.task import Priority, Task


@pytest.fixture
def mock_storage():
    return Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Descricao", Priority.BAIXA, prazo)


def test_save_atribui_id(repo, task):
    resultado = repo.save(task)
    assert resultado.id == 1


def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_usa_storage(repo, task, mock_storage):
    mock_storage.get.return_value = task
    resultado = repo.find_by_id(1)
    assert resultado == task


def test_sequencia_save_e_find_by_id(repo, task, mock_storage):
    repo.save(task)
    mock_storage.get.return_value = task
    resultado = repo.find_by_id(1)
    assert resultado == task
    mock_storage.add.assert_called_once_with(1, task)
    mock_storage.get.assert_called_once_with(1)


def test_find_all_lista_vazia(repo, mock_storage):
    mock_storage.get_all.return_value = []
    resultado = repo.find_all()
    assert resultado == []
