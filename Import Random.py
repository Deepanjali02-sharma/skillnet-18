
def guess_number(secret,attempts=1):
    guess=int(input(f"Attempt{attempts}: guess the number(between 1 and 10):"))
    if guess<secret:
        print("Too Low! Try again.")
        return guess_number(secret,attempts+1)
    elif guess>secret:
        print("Too High! Try again.")
        return guess_number(secret,attempts+1)
    elif guess ==secret:
        print(f"Congratulations! You guessed the number {secret} in {attempts} attempts")
        return attempts