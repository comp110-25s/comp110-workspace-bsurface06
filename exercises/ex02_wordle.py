"""This program plays the Wordle game by assigning a string of any length and executing the Wordle game logic. 
There are 6 turns, each turn the player gets to input a guess of the same length of the example word, and the guess 
is compared with the secret and codified to a set of boxes. 
If the guess is correct, the player wins, and if it is incorrect, the program loops for another guess."""

__author__: str = "730772358"


def contains_char(search_string: str, search_char: str) -> bool:
    """checks if a specific given character is present within the search_string"""
    assert len(search_char) == 1, f"len('{search_char}') is not 1"

    for char in search_string:
        if char == search_char:
            return True

    return False


def emojified(guess: str, secret_word: str) -> str:
    """Given two strings of equal length, the function returns an emoji string of the
    same length to represent if the guesses are correct or not (green = letters match in the same position,
    yellow = letters that are in the word but in the wrong position, white = letters are not in the word at all)
    """
    assert len(guess) == len(
        secret_word
    ), f"Lengths of guess '{guess}' and secret word must be equal"

    GREEN: str = "\U0001F7E9"
    YELLOW: str = "\U0001F7E8"
    WHITE: str = "\U00002B1C"

    result = ""

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result += GREEN
        elif contains_char(secret_word, guess[i]):
            result += YELLOW
        else:
            result += WHITE

    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user to enter a word of the specified length.
    If the input is not the right length, it keeps prompting"""
    guess = input(f"Enter a {expected_length} character word:")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret_word: str) -> None:
    """main function that runs the Wordle game loop,
    and ensures the player has a max of 6 turns"""

    MAX_TURNS = 6
    turns = 0
    won = False

    while turns < MAX_TURNS and not won:
        turns += 1
        print(f"\n=== Turn {turns}/{MAX_TURNS} ===")

        guess = input_guess(len(secret_word))
        emoji_result = emojified(guess, secret_word)
        print(emoji_result)

        if guess == secret_word:
            won = True

    if won:
        print(f"\nYou won in {turns}/{MAX_TURNS} turns!")
    else:
        print(f"\nX/{MAX_TURNS} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
