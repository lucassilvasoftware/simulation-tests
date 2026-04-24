from datetime import datetime, timedelta

import pytest

from task_manager.task import Priority, Status, Task


@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


def test_estado_inicial(task_valida):
    task_valida.validar()
    assert task_valida.id is None
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Descricao", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado_invalido():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Tarefa valida", "Descricao", Priority.MEDIA, prazo)
    with pytest.raises(ValueError):
        task.validar()


def test_ciclo_vida_transicao_valida(task_valida):
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO


def test_ciclo_vida_transicao_invalida(task_valida):
    with pytest.raises(ValueError):
        task_valida.status = "finalizada"
