import random

def main():
    """
    Main function to run the Little Professor game.
    It gets the level, generates 10 math problems, and scores the user.
    """
    level = get_level()
    score = 0

    # Generate and ask 10 problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        tries = 0
        # Allow up to 3 tries for each problem
        while tries < 3:
            try:
                # Prompt the user for the answer
                user_answer = int(input(f"{x} + {y} = "))

                # Check if the answer is correct
                if user_answer == correct_answer:
                    score += 1
                    break # Correct, so move to the next problem
                else:
                    tries += 1
                    print("EEE")
            except ValueError:
                # Handle cases where input is not a number
                tries += 1
                print("EEE")

        # If the user failed 3 times, show the correct answer
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Print the final score
    print(f"Score: {score}")


def get_level():
    """
    Prompts the user for a level and returns 1, 2, or 3.
    It will re-prompt until a valid level is entered.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            # This handles non-integer input
            pass


def generate_integer(level):
    """
    Generates a random non-negative integer with a number of digits
    equal to the level.

    Args:
        level (int): The number of digits for the integer (1, 2, or 3).

    Returns:
        int: A randomly generated integer.

    Raises:
        ValueError: If the level is not 1, 2, or 3.
    """
    if level == 1:
        # 1-digit numbers (0-9)
        return random.randint(0, 9)
    elif level == 2:
        # 2-digit numbers (10-99)
        return random.randint(10, 99)
    elif level == 3:
        # 3-digit numbers (100-999)
        return random.randint(100, 999)
    else:
        # This case should not be reached due to get_level() validation
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()
