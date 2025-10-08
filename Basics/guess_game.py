import random
secret = random.randint(1, 20)

def guess_game():
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret:
            print("TOO LOW")
        elif guess > secret:
            print("TOO HIGH")
        else:
            print("🎉 CONGRATULATIONS! You guessed it right!")
            break

        if attempts >= 10:
            print(f"❌ Game Over! The number was {secret}")
            break

guess_game()
