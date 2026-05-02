from reverser import Reverser
from palindrome import PanTester
from networker import Networker
from pets import jet_lee


def main() -> None:
    reverser = Reverser()
    pan_tester = PanTester()
    networker = Networker()

    print("=== Reverser ===")
    sample = "didactic sniffle"
    print(f"  reverse({sample!r}) -> {reverser.reverse(sample)!r}")

    print("\n=== Pan Tester ===")
    for word in ("racecar", "hello", "A man a plan a canal Panama", "jet lee"):
        result = pan_tester.is_palindrome(word)
        print(f"  is_palindrome({word!r}) -> {result}")

    print("\n=== Networker ===")
    print(f"  hostname -> {networker.hostname()}")

    print("\n=== Pets ===")
    print(f"  {jet_lee!r}")
    print(f"  {jet_lee.speak()}")


if __name__ == "__main__":
    main()
