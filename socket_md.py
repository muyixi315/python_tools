import socket
from contextlib import closing
from typing import cast

def unused_tcp_port() -> int:
    """Return an unused port"""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("", 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return cast(int, sock.getsockname()[1])

print(unused_tcp_port())
