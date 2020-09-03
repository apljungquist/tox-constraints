import json
import time

import common


class Server:
    def __init__(self):
        self._started_at = time.time()
        self._num_request = 0

    def get_status(self) -> str:
        num_request = self._num_request
        self._num_request += 1
        return json.dumps(common.Status(num_request)._asdict())
