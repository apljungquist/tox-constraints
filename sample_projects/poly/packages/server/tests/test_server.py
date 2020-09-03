import server
import client


def test_num_request_is_strictly_increasing():
    client_ = client.Client(server.Server())
    lo = client_.get_status().num_request
    hi = client_.get_status().num_request
    assert lo < hi
