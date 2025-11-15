import random

# Step 1: List of predefined words
words = ["python", "hangman", "program", "developer", "challenge"]

# Step 2: Randomly choose one word
word = random.choice(words)
word_letters = list(word)
guessed_letters = []  # letters guessed correctly
tries = 6  # number of incorrect attempts allowed

print("🎯 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print(f"The word has {len(word)} letters.")

# Step 3: Game loop
while tries > 0:
    # Display current guessed word
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in word_letters):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    # Check if guess is in word
    if guess in word_letters:
        print("✅ Good guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        tries -= 1
        print(f"Remaining tries: {tries}")

# Step 4: If player runs out of tries
if tries == 0:
    print("\n💀 Game Over! The correct word was:", word)
