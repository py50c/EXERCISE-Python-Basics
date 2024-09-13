import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
max_guesses = 10
guess_count = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. You have 10 tries to guess it.")

# Start the guessing loop
while guess_count < max_guesses:
    guess = input("\nGuess the number (attempt " + str(guess_count + 1) + "/" + str(max_guesses) + "): ")
    
    # Convert the input to an integer
    guess = int(guess)
    
    # Check if the guess is out of bounds
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue  # Skip the rest of the loop and ask again
    
    guess_count += 1  # Increment the guess count
    
    # Compare the guess with the random number
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number in", guess_count, "tries.")
        break  # Exit the loop if the guess is correct

# If the user runs out of guesses
if guess_count == max_guesses and guess != random_number:
    print("\nGame Over! The correct number was", random_number)
