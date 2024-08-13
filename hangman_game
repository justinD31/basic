import random

# Predefined list of words or phrases for the game
WORDS = [
    "python programming",
    "data science",
    "artificial intelligence",
    "machine learning",
    "natural language processing",
    "deep learning",
    "neural networks",
    "computer vision",
]

# Hangman stages as a list of strings
HANGMAN_STAGES = [
    """
      ------
      |    |
           |
           |
           |
           |
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    """
]

def choose_word():
    """Choose a random word or phrase from the predefined list."""
    return random.choice(WORDS).upper()

def display_word(word, guesses):
    """Display the current state of the word with guessed letters."""
    return ' '.join(letter if letter in guesses else '_' for letter in word)

def hangman_game():
    """Main function to run the Hangman game."""
    word = choose_word()
    word_set = set(word)
    guesses = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMAN_STAGES) - 1
    
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    while incorrect_guesses < max_attempts:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word: {display_word(word, guesses)}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guesses))}")

        guess = input("Enter a letter: ").upper()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        
        guesses.add(guess)
        
        if guess in word_set:
            print(f"Good guess: '{guess}'")
        else:
            print(f"Wrong guess: '{guess}'")
            incorrect_guesses += 1
        
        if set(word).issubset(guesses):
            print("Congratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Sorry, you've run out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman_game()
