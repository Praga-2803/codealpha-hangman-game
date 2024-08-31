import random

def making_a_guess(guess, chosen_word, blank_list, update_display):
    correct_guess = False
    for index, letter in enumerate(chosen_word):
        if guess.lower() == letter:
            blank_list[index] = guess.lower()
            correct_guess = True
    if not correct_guess:
        print(f"There is no '{guess}', sorry.")
        update_display[0] += 1
    return update_display

def display_status(HANGMANPICS, update_display, blank_list):
    print(HANGMANPICS[update_display[0]])
    print(f"Current word: {''.join(blank_list)}")

def main():
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
     / \  |
          |
    =========''']

    word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
    chosen_word = list(random.choice(word_list))
    initial_reveal_index = random.randint(0, len(chosen_word) - 1)
    blank_list = ['_'] * len(chosen_word)
    blank_list[initial_reveal_index] = chosen_word[initial_reveal_index]

    update_display = [0]  # Use a list to allow mutability

    print("Welcome to Hangman!")
    display_status(HANGMANPICS, update_display, blank_list)

    guessed_letters = set()

    while update_display[0] < len(HANGMANPICS) - 1:
        guess = input("Make a guess (single letter): ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.add(guess)
        update_display = making_a_guess(guess, chosen_word, blank_list, update_display)
        
        display_status(HANGMANPICS, update_display, blank_list)

        if '_' not in blank_list:
            print("YOU WIN!")
            break
    else:
        print(f"GAME OVER. The word was: {''.join(chosen_word)}")

if _name_ == "_main_":
    main()