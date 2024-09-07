import random


def roll_biased_dice():
    """
    Rolls a biased dice with a higher probability for the number 6.
    
    :return: A randomly selected number from 1 to 6 with bias towards 6
    """
    # Define the numbers from 1 to 6
    numbers = [1, 2, 3, 4, 5, 6]

    # Assign weights to each number (higher weight for 6)
    weights = [1, 1, 1, 1, 1, 5]  # 6 is more likely to be chosen

    # Randomly select one number, considering the weights
    result = random.choices(numbers, weights=weights, k=1)[0]
    
    return result


if __name__ == "__main__":
    print("Rolling the biased dice...")
    biased_number = roll_biased_dice()
    print(f"The dice rolled: {biased_number}")
