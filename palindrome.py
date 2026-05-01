from reverser import Reverser


class PanTester:
    """Tests whether a string is a palindrome."""

    def __init__(self) -> None:
        self._reverser = Reverser()

    def is_palindrome(self, text: str) -> bool:
        """Return True if *text* reads the same forwards and backwards."""
        normalised = text.lower().replace(" ", "")
        return normalised == self._reverser.reverse(normalised)
