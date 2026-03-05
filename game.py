print("Welome to Hangman")

# part 1
# We need the computer to pick a RANDOM word
import random
# We need the computer to choose from a LIST of words
words = ["mascara", "powder", "necklace", "banglets", "bracelets"]
# Store the randomly selected word in a variable to reference
secret_word = random.choice(words)

# print(secret_word)
# Part 2
# We need to display the secret word without the letters for people to guess
display = []
guessed_letter = []
# For each letter in our secret word, append an _ to our display
for letter in secret_word:
    display.append("_")

print(secret_word)
print(display)
# We need to create a way for people to guess letters


# while the word is not complete, and the game is not over, we get prompted for a new guess

game_over = False
lives = 5

while not game_over:
    guess = input("Guess a letter:").strip().lower()

    if(len(guess)) != 1:
        print("Please enter only ONE character")

    if guess in guessed_letter:
        print("Duh, you already chose this one! Try again!")
        continue
    
    guessed_letter.append(guess)
    print("You tried:", guessed_letter)

    if guess not in secret_word:
        lives -= 1
        print("Wrong guess! Try again")
        print("Lives left: ", lives)
        if lives == 0:
            game_over = True
            print("You lose!")
            print("The secret word was: ", secret_word)
            break

# We need to create a way to check if letter player used is in secret word
# for each postion in our secret word, if the letter the player picks in in that secret word, then find that position in our display and replace it
    for postion in range(len(secret_word)):
        secret_word_letter = secret_word[postion]

        if secret_word_letter == guess:
            display[postion] = guess

    print("Secret word: ", display)

    if "_" not in display:
        game_over = True
        print("Youre smart cookie - you win!")

# print(len("Mississippi"))
# print(len(""))
# print(len("a"))