class InMemoryStorage:
    def __init__(self) -> None:
        self._data = {}

    def add(self, id, item) -> None:
        self._data[id] = item

    def get(self, id):
        return self._data.get(id)

    def get_all(self):
        return list(self._data.values())

    def delete(self, id) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self) -> None:
        self._data.clear()
