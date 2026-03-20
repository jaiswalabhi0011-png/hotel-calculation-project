import random


easy_words = ["Apple", "train", "tiger"," money","india"]
medium_words = ["python", "bottle","monkey","planet","laptop"]
hard_words = ["elephant", "diamond","umbrella","computer","mountain"]

print("Welcome to the guessing game")
print("Choose a difficulty level : easy,medium or hard")
level = input('enter difficulty: '). lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret  = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice .DEfaulting to easy level")
    secret = random.choice(easy_words)    
    
    
attempts = 0
print("\n guess the secret password")


while True:
    guess = input("enter your guess: ").lower()
    attempts += 1
    
    if guess == secret:
        print(f'Congratulatins!you guessed  it in {attempts} attempts.')
        break        
    
    hint = ""
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
            
print("hint", hint) 
print("Gameover")
                
        