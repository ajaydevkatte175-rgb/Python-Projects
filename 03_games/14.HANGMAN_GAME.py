import random
import os
import sys

# --- GLOBAL CONFIGURATIONS ---
# ASCII art matrix representation for the 7 stages of a standard Hangman gallows structure
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
]

# Word category bank for the engine gameplay pipeline
WORD_BANK = ["PYTHON", "PROGRAMMING", "DEVELOPER", "INTERFACE", "COMPILER", "ALGORITHM"]

def clear_screen():
    """Utility to clean the terminal viewport between active player turns."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_hangman_game():
    # --- INITIALIZE CORE GAME STATE ---
    secret_word = random.choice(WORD_BANK)
    guessed_letters = set()
    incorrect_attempts = 0
    max_allowed_attempts = len(HANGMAN_STAGES) - 1

    while True:
        clear_screen()
        print("=========================================")
        print("         LETS PLAY GAME OF HANGMAN!         ")
        print("=========================================")
        
        # 1. Print current visual gallows structural progress frame
        print(HANGMAN_STAGES[incorrect_attempts])
        
        # 2. Render target secret word masking block array (e.g., P _ T H _ N)
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word to guess: " + " ".join(display_word))
        print(f"Incorrect Attempts Left: {max_allowed_attempts - incorrect_attempts}")
        print(f"Guessed Letters Basket: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("-----------------------------------------")

        # 3. Check Game Win Condition State Matrix
        if "_" not in display_word:
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: {secret_word}!")
            break

        # 4. Check Game Lose Condition State Matrix
        if incorrect_attempts >= max_allowed_attempts:
            print(f"\n💀 GAME OVER! You ran out of lives.")
            print(f"The secret hidden word was: {secret_word}")
            break

        # 5. Capture and validate user keystroke input data safely
        guess = input("Guess a letter: ").upper().strip()

        # --- INPUT PROTECTIONS GUARDRAILS ---
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid Input! Please enter a single alphabetical character.")
            input("\nPress Enter to continue...")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one!")
            input("\nPress Enter to continue...")
            continue

        # Commit verified guest character token value directly into state track collections
        guessed_letters.add(guess)

        # 6. Evaluate guess status parameters
        if guess in secret_word:
            print(f"✅ Nice job! '{guess}' is part of the secret target matrix.")
        else:
            print(f"❌ Oops! '{guess}' is not in the secret word.")
            incorrect_attempts += 1
            
        input("\nPress Enter to pass turn back to next step...")

if __name__ == "__main__":
    while True:
        run_hangman_game()
        print("=========================================")
        play_again = input("Do you want to play another match? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\nThank you for playing Hangman Studio. Goodbye!")
            sys.exit()