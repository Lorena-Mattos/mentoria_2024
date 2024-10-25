import pytest
from worker import Worker


def test_table_exists(worker, mocker):
    """
    The method worker.table_exists should run internally the method worker.client.query
    """
    query_spy = mocker.spy(worker.client, "query")
    worker.table_exists('table_name')
    assert query_spy.call_count == 1
