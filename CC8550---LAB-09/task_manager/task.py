from __future__ import annotations

from datetime import datetime
from enum import Enum, IntEnum


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(
        self,
        id: int | None,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
        status: Status = Status.PENDENTE,
    ) -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self._status = Status.PENDENTE
        self.status = status

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        if not isinstance(value, Status):
            raise ValueError("Status invalido.")
        self._status = value

    def validar(self) -> None:
        if len(self.titulo.strip()) < 3:
            raise ValueError("Titulo deve ter ao menos 3 caracteres.")
        if self.prazo < datetime.now():
            raise ValueError("Prazo nao pode estar no passado.")
