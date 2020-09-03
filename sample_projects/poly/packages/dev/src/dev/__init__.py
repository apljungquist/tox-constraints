import contextlib
import time

import server


@contextlib.contextmanager
def print_timing(name):
    print(f"{name}...")
    t0 = time.perf_counter()
    try:
        yield
    finally:
        t1 = time.perf_counter()
        print(f"{name} ran in {t1 - t0} seconds")


class DebugServer(server.Server):
    def get_status(self) -> str:
        with print_timing("get_status"):
            return super(DebugServer, self).get_status()
