import random

random_number = random.randint(0,100)
print(random_number)

print("""--------Number Guessing Game------
      
      Instructions: You have only ten chances. If you have not guess number in given ten chances you will losse the game.""")


count = 0
while(count < 3):

    count +=1
    user_input = int(input(("Enter any number from 0 to 100 :  ")))
    
    if user_input > random_number:
        print(f"{user_input} is too high from actual number. ")
        
    # continue
    elif user_input < random_number:
        print(f"{user_input} is too low from actual number. ")
        
    
    
    elif user_input == random_number: 
        print("Hurray! You have guess the number and won.")
        break


if random_number != user_input:
    print("game loss")


