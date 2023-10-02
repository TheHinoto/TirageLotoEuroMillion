import random
from os import urandom


class TirageEuroMillion:
    all_existing_number = set(range(1, 50 + 1))
    all_existing_star = set(range(1, 12 + 1))

    def __init__(self) -> None:
        random.seed(urandom(2048))
        self.numbers: set[int] = set(random.sample(self.all_existing_number, 5))
        self.stars: set[int] = set(random.sample(self.all_existing_star, 2))

    def __str__(self) -> str:
        return f"Numbers: {self.numbers}, Stars: {self.stars}"

    def __repr__(self) -> str:
        return f"TirageEuroMillion(Numbers: {self.numbers}, Stars: {self.stars})"


class TirageLoto:
    all_existing_number = set(range(1, 49 + 1))
    all_existing_star = set(range(1, 10 + 1))

    def __init__(self) -> None:
        random.seed(urandom(2048))
        self.numbers: set[int] = set(random.sample(self.all_existing_number, 5))
        self.stars: set[int] = set(random.sample(self.all_existing_star, 1))

    def __str__(self) -> str:
        return f"Numbers: {self.numbers}, Stars: {self.stars}"

    def __repr__(self) -> str:
        return f"TirageLoto(Numbers: {self.numbers}, Stars: {self.stars})"
