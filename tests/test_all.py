import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from reverser import Reverser
from palindrome import PanTester
from networker import Networker
from pets import Dog, jet_lee


class TestReverser:
    def setup_method(self):
        self.reverser = Reverser()

    def test_reverse_simple(self):
        assert self.reverser.reverse("hello") == "olleh"

    def test_reverse_empty(self):
        assert self.reverser.reverse("") == ""

    def test_reverse_single_char(self):
        assert self.reverser.reverse("a") == "a"

    def test_reverse_palindrome_unchanged(self):
        assert self.reverser.reverse("racecar") == "racecar"


class TestPanTester:
    def setup_method(self):
        self.tester = PanTester()

    def test_palindrome_simple(self):
        assert self.tester.is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert self.tester.is_palindrome("hello") is False

    def test_palindrome_case_insensitive(self):
        assert self.tester.is_palindrome("RaceCar") is True

    def test_palindrome_with_spaces(self):
        assert self.tester.is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string(self):
        assert self.tester.is_palindrome("") is True

    def test_jet_lee_not_palindrome(self):
        assert self.tester.is_palindrome("jet lee") is False


class TestNetworker:
    def setup_method(self):
        self.networker = Networker()

    def test_hostname_is_string(self):
        assert isinstance(self.networker.hostname(), str)

    def test_hostname_non_empty(self):
        assert len(self.networker.hostname()) > 0

    def test_unreachable_host(self):
        assert self.networker.is_reachable("0.0.0.0", port=1, timeout=0.1) is False


class TestDog:
    def test_jet_lee_name(self):
        assert jet_lee.name == "Jet Lee"

    def test_jet_lee_speak(self):
        assert jet_lee.speak() == "Jet Lee says: Woof!"

    def test_dog_repr(self):
        assert repr(jet_lee) == "Dog(name='Jet Lee')"

    def test_custom_dog(self):
        dog = Dog("Rex")
        assert dog.speak() == "Rex says: Woof!"
