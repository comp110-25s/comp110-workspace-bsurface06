"""This program helps plan tea parties by asking for the number of guests, the quantity of tea bags needed, the number of treats, and the expected cost of the party"""

__author__: str = "730772358"


def main_planner(guests: int) -> None:
    """Plans number of tea bags, treats, and the cost of the party based on number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates total number of tea bags needed based on amount of guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates number of treats needed based on number of teas guests are expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
