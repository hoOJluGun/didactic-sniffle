class Dog:
    """Represents a dog."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r})"


# Jet Lee – our resident dog
jet_lee = Dog("Jet Lee")
