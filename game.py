import random
game_over = True
random_number = random.randint(1,100)
while game_over :
    guess_number = int(input("Enter the number between 0 to 100: "))
    if random_number == guess_number:      
        print("Congrates !! you win ..!! \n\n")
        break
    elif random_number < guess_number:
        print("Too high ! Guess Again ")
       
    else: 
          print("Too low ! Guess Again ...")
