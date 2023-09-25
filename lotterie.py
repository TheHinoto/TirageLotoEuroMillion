import random
from os import urandom


class TirageEuroMillion:
    def __init__(self) -> None:
        random.seed(urandom(2048))
        self.all_existing_number = list(range(1, 50 + 1))
        self.all_existing_star = list(range(1, 12 + 1))

        self.numbers: list[int] = random.sample(self.all_existing_number, 5)
        self.stars: list[int] = random.sample(self.all_existing_star, 2)

    def __str__(self) -> str:
        return f"Numbers: {self.numbers}, Stars: {self.stars}"

    def __repr__(self) -> str:
        return f"TirageEuroMillion(Numbers: {self.numbers}, Stars: {self.stars})"


class Tirageloto:
    def __init__(self) -> None:
        random.seed(urandom(2048))
        self.all_existing_number = list(range(1, 49 + 1))
        self.all_existing_star = list(range(1, 10 + 1))

        self.numbers: list[int] = random.sample(self.all_existing_number, 5)
        self.stars: list[int] = random.sample(self.all_existing_star, 1)

    def __str__(self) -> str:
        return f"Numbers: {self.numbers}, Stars: {self.stars}"

    def __repr__(self) -> str:
        return f"TirageLoto(Numbers: {self.numbers}, Stars: {self.stars})"
