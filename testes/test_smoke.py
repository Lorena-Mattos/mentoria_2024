import pytest
from worker import Worker


# @pytest.mark.worker --> Os custom markers são decorators usados para selecionar quais testes serão executados.
# Nesse caso, os testes marcados com @pytest.mark.worker serão executados individualmente através do comando pytest
# -m worker

def test_smoke():
    """ Testing the instance of Worker class """
    worker = Worker()
    assert isinstance(worker, Worker)


def test_methods_smoke():
    """ Testing if worker. transform is a method """
    worker = Worker()
    assert hasattr(worker.transform, '__call__')


def test_transform():
    """ Testing if the result of transform method is equal 1 """
    worker = Worker()
    result = worker.transform(value='1.0', convert_to='int')
    assert result == 1


def test_transform_with_exception():
    """ Testing if the method raise an Exception """
    worker = Worker()
    with pytest.raises(ValueError):
        worker.transform(value='1.0', convert_to='invalid_value')
