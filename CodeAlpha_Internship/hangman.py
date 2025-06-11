import random

def hangman():
    words = ['python', 'developer', 'hangman', 'internship', 'codealpha']
    chosen_word = random.choice(words)
    guessed = ['_'] * len(chosen_word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman Game!")

    while attempts > 0 and '_' in guessed:
        print("\nWord:", ' '.join(guessed))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⛔ Already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong guess.")

    if '_' not in guessed:
        print("🎉 You won! The word was:", chosen_word)
    else:
        print("💀 Game over! The word was:", chosen_word)

hangman()
