import datetime
import random

def stime(clientName):
    tm = datetime.datetime.now()
    time = tm.strftime("%H:%M:%S")
    print(f'{clientName} The time is {time}')

activities = {
        'Book': ['The Alchemist', 
                 'The mysterious incident of the dog in the night time', 
                 'Holes', 
                 'The Fourth Agreement', 
                 'The Voice of Knowledge'],
        'Movie': ['Blade', 
                  'Game of throns', 
                  'Vikings', 
                  'Breaking Bad', 
                  'Archane', 
                  'Peaky Blinders', 
                  'The Warriors',
                  'Creed II',
                  'Power', 'The Sinners', 'Empire']
    }

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
                
    print("\n--- Rock, Paper, Scissors ---")
    player = input("Choose rock, paper, or scissors: ").lower()
                
    if player not in options:
        print("Invalid choice. Try again.")
        return
                
    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")
                
    if player == computer:
         print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
          print("Computer wins!")
          print()

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? Because it had too many problems."
]
#---------------------------------------------------------------------------    

def bookRecommendation(clientName):
        print(f"{clientName} '{random.choice(activities['Book'])}' is a good book, read it and tell me what you think")
    
def movieRecommendation(clientName):
        print(f"{clientName} '{random.choice(activities['Movie'])}' is a good movie, watch it and tell me what you think")

def tellAJokes(clientName):
    print('------------------------------')
    print(f"|--{clientName} want to hear a joke?--|")
    print('------------------------------')
    print('Take this:', random.choice(jokes))
    
        
def doMath(clientName):
    print('---------------------')
    user = input("|-- Chose an option--|: ")
    print('---------------------')

    if user == "1":
        print('----------------------------')
        print(f"|--{clientName} let's do some math--|")
        print('-----------------------------')
            
        op_sign = input("Please enter your operating sign here '+, -, *, /, **, %': ")
            
        try:
            if op_sign in ["+", "-", "**", "*", "/","%"]:
                number0 = int(input("Enter the first number here: "))
                number1 = int(input("Enter the second number to add here: "))
                    
                if op_sign == '+':
                    result = number0 + number1
                
                elif op_sign == '-':
                    result = number0 - number1
                
                elif op_sign == '/':
                    result = number0 / number1
        
                elif op_sign == '*':
                    result = number0 * number1
                
                elif op_sign == '**':
                    result = number0 ** number1
                
                elif op_sign == '%':
                    result = number0 % number1
                print(f'The result is {result}')
                print()
                print("What would you like to do next?")
                choice = input("Choose an option: ")
                                

            else:
                print("Invalid input")
        
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please try again.")
        
        except ValueError as e:
            print(f"Error: {e}")

    elif user == "2":
        getnumber = int(input("Enter your decimal number here: "))
        if getnumber > 1:
            for i in range(2, int(getnumber**0.5) + 1):
                if getnumber % i == 0:
                    print(f"'{getnumber}' Is not a prime number because it has other divisers more than 1 and itself!")
                    break
            else:
                print(f"'{getnumber}' Is a prime number")
        else:
            print(f"'{getnumber}' Is not a prime number because it has other divisers more than 1 and itself!")

def playGame(clientName):
    while True:
        print("Enter 1 for Number Guessing or 2 for Rock-Paper-Scisors")
        choiceGame = input("Do you want to play 'Number guessing' or 'Rock-Paper-Scisor'?")
                
        if choiceGame == '1':
            countLoops = 0
            while True:
                countLoops = countLoops + 1
                print('----------------------------------------------------------')
                user_1 = input("|--Plese enter a number to guess range from 0 to 10: --|")
                print('----------------------------------------------------------')
                pc_number = random.randint(0, 10)
                print(f'Was: {pc_number}')
                        
                if pc_number > int(user_1):
                    print(f"{user_1}, is too small")
    
                elif pc_number < int(user_1):
                        print(f"{user_1}, is too large")

                elif int(user_1) == pc_number:
                    print(f"Congratulations {clientName}, {user_1} is the right guess:)")
                    print(f"You did it after {countLoops} guess(es)")
                    print("--------------------")
                    break
                            
                elif user_1 == "exit":
                    print("Bye...")
                    break
                else:
                    print("Invalid input")
                    choice = input("Choose an option: ")
        
        elif choiceGame == '2':
                rock_paper_scissors()
    
        elif choiceGame.lower() == 'Exit':
            print("Exiting game...")
            break
    
        else:
                print("Invalid input!")
