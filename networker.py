import socket


class Networker:
    """Simple network connectivity helper."""

    def is_reachable(self, host: str, port: int = 80, timeout: float = 3.0) -> bool:
        """Return True if *host*:*port* is reachable within *timeout* seconds."""
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            return False

    def hostname(self) -> str:
        """Return the local machine hostname."""
        return socket.gethostname()
