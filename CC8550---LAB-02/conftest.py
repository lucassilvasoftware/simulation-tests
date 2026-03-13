import pytest


@pytest.fixture
def cpfs_validos():
    return [
        "313.402.809-30",
        "111.444.777-35",
        "12345678909",
    ]


@pytest.fixture
def cpfs_invalidos():
    return [
        "111.222.333-44",
        "111.111.111-11",
        "123.456.789-00",
        "1234567890",
        "123456789012",
        "1234567890a",
        "",
    ]
