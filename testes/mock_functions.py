# mock_functions.py
from worker import Worker
import mock


def test_table_exists(worker: Worker):
    """
       The Mock method return a fake function
    """
    # Corrigindo o retorno da consulta para que o resultado seja consistente com uma consulta real
    worker.client.query = mock.Mock(return_value=[{'a': 1}, {'b': 2}])
    worker.table_exists('database_name')

    """
       The call_args_list stores a list with passed args as Call objects
       A Call object can be compared with a tuple of tuples or dicts
    """
    assert worker.client.query.call_args_list == [
        mock.call("SELECT * FROM database_name LIMIT 1")
    ]


def test_get_file_content_to_file(worker: Worker):
    worker.client.get_blob = mock.Mock(return_value=b"blob_content")
    worker.get_file_content_to_file(file_name="file_name.txt")

    assert worker.client.get_blob.call_args_list == [
        mock.call({'blob_name': 'file_name.txt'})
    ]
