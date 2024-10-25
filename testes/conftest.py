import pytest
from unittest.mock import MagicMock
from worker import Worker


@pytest.fixture
def worker():
    """
    Fixture que retorna uma instância da classe Worker.
    """
    client = MagicMock()  # Substitua pelo objeto client real
    return Worker(client)
