import json

import common
import server


class Client:
    def __init__(self, server_: server.Server):
        self._server = server_

    def get_status(self) -> common.Status:
        return common.Status(**json.loads(self._server.get_status()))
