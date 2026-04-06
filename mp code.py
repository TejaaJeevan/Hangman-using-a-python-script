import os
import random
import time

# Cool ASCII Art for Hangman stages
HANGMAN_STAGES = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    GAME OVER
    """
]

# Word list
WORDS = [
    "python", "vscode", "hangman", "programming", "computer", "keyboard",
    "developer", "algorithm", "function", "variable", "terminal", "github",
    "jupyter", "debugging", "framework", "database", "network", "binary"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\033[96m" + "="*60 + "\033[0m")
    print("\033[95m" + " " * 20 + "🔥 HANGMAN GAME 🔥" + "\033[0m")
    print("\033[96m" + "="*60 + "\033[0m\n")

def print_colored(text, color_code):
    colors = {
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'cyan': '\033[96m',
        'purple': '\033[95m',
        'bold': '\033[1m'
    }
    reset = '\033[0m'
    print(colors.get(color_code, '') + text + reset)

def play_hangman():
    clear_screen()
    print_header()

    
    
    word = random.choice(WORDS).upper()
    guessed_letters = set()
    attempts = 6
    word_display = ["_" if letter.isalpha() else letter for letter in word]
    
    print_colored("Welcome to Hangman! Guess the word before the man is hanged!", "cyan")
    print_colored("Hint: It's related to programming or tech! ({len(word)} letters)\n", "yellow")
    
    while attempts > 0:
        clear_screen()
        print_header()
        
        # Show hangman
        print_colored(HANGMAN_STAGES[6 - attempts], "red")
        
        # Show current word
        print_colored("Word: " + " ".join(word_display), "bold")
        print(f"\nAttempts left: {'❤️ ' * attempts}")
        
        # Show guessed letters
        if guessed_letters:
            print_colored("Guessed letters: " + " ".join(sorted(guessed_letters)), "purple")
        
        # Win condition
        if "_" not in word_display:
            clear_screen()
            print_header()
            print_colored("🎉 CONGRATULATIONS! YOU SAVED HIM! 🎉", "green")
            print_colored(f"The word was: {word}", "bold")
            print_colored("🏆 You're a coding legend! 🏆", "yellow")
            break
        
        # Get guess
        guess = input("\n\033[93mGuess a letter: \033[0m").strip().upper()
        
        try:
            if len(guess) != 1 or not guess.isalpha():
                print_colored("❌ Please enter a single letter!", "red")
                time.sleep(1.5)
                continue
        except:
            print_colored('Please enter only a single alphabet.',"red")
        
        if guess in guessed_letters:    
            print_colored("⚠️  You already guessed that letter!", "yellow")
            time.sleep(1.2)
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print_colored(f"✅ Good job! '{guess}' is in the word!", "green")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print_colored(f"❌ Wrong! '{guess}' is not in the word.", "red")
        
        time.sleep(1.2)
    
    # Game Over
    if attempts == 0:
        clear_screen()
        print_header()
        print_colored(HANGMAN_STAGES[-1], "red")
        print_colored(f"💀 GAME OVER! The word was: {word}", "red")
        print_colored("Better luck next time, coder!", "yellow")
    
    # Play again?
    play_again = input("\n\033[96mPlay again? (y/n): \033[0m").strip().lower()
    if play_again == 'y':
        play_hangman()

if __name__ == "__main__":
    try:
        play_hangman()
    except KeyboardInterrupt:
        clear_screen()
        print_colored("\n\n👋 Thanks for playing Hangman! See you next time!", "cyan")