import pytest
from unittest.mock import Mock
from worker import Worker


# @pytest.mark.worker --> Os custom markers são decorators usados para selecionar quais testes serão executados.
# Nesse caso, os testes marcados com @pytest.mark.worker serão executados individualmente através do comando pytest
# -m worker
@pytest.fixture
def mock_client():
    # Cria um mock do cliente
    client = Mock()
    return client


def test_smoke(mock_client):
    """ Testing the instance of Worker class """
    worker = Worker(mock_client)
    assert worker is not None


def test_methods_smoke(mock_client):
    """ Testing if worker.transform is a method """
    worker = Worker(mock_client)
    assert hasattr(worker, 'transform')


def test_transform(mock_client):
    """ Testing if the result of transform method is equal 1 """
    worker = Worker(mock_client)
    result = worker.transform("1.0", "int")
    assert result == 1


def test_transform_with_exception(mock_client):
    """ Testing if the method raises an Exception """
    worker = Worker(mock_client)
    with pytest.raises(ValueError):
        worker.transform("abc", "int")
