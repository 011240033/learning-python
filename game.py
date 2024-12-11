import random

def results(num,guess):
            if num == guess:
                print("you finally got it right")
            elif num ==(guess - 1):
                    print("a littile bit low")
            elif num ==(guess - 2):
                    print("a bit low")
            elif num ==(guess - 3):     
                    print("your guess is low")
            elif num ==(guess - 4): 
                    print("your guess is low")    
            elif num ==(guess - 5):
                    print("your guess is low")
            elif num ==(guess - 6): 
                    print("your guess is low")
            elif num ==(guess - 7):
                    print("your guess is verylow") 
            elif num ==(guess - 8): 
                    print("your guess is  too low")
            elif num ==(guess - 9): 
                    print("your guess is  very very  low")
            elif num ==(guess + 1):
                    print("a littile bit highw")
            elif num ==(guess + 2):
                    print("a bit high")
            elif num ==(guess + 3):     
                    print("your guess is high")
            elif num ==(guess + 4): 
                    print("your guess is high ")    
            elif num ==(guess + 5): 
                    print("your guess is high")
            elif num ==(guess + 6): 
                    print("your guess is high")
            elif num ==(guess + 7):
                    print("your guess is very high") 
            elif num ==(guess + 8): 
                    print("your guess is  too high")
            elif num ==(guess + 9): 
                    print("your guess is  very very  high")
            else:
                    print("guess in the right range") 
def game():
    print("game has started")
    guess = random.randint(1,10)
    num = int(input("guess a number from 1 to 10"))
    attempt = 0
    if num == guess:
            print("wow quick guess")
    else:  
        results(num,guess)      
        while attempt < 4:
            print("try again")
            num = int(input("guess a number from 1 to 10"))
            if num == guess:
                print("you finally got it")
                break
            else:
                attempt +=1
                results(num,guess)
                if attempt == 3:
                    print("You've used up all your chances!")
                    print(f"The correct number was {guess}.")
                    break  
    choice = int(input("do want to play again?\n 1 Yes\n 2 No"))           
    if choice == 1:
        game()
    elif choice == 2:
        print("end of game\n thank you for playing")
    else:
        print("choose either 1 or 2")
        
        
game()


        