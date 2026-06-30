import random

def game():
    player_score = 0
    computer_score = 0
    mode = 0
    mode = input("Enter which Mode to Play : ").upper()

    while mode not in ['A','B','C']:
        print("Invalid Mode Selection")
        mode = input("Enter which Mode to Play : ").upper()

    mode1 = {'A' : 3 , 'B' : 5, 'C' : 7}
    
    value = {1: "Rock",2: "Scissor",3: "Paper"}

    i=0
    while i <mode1[mode] :

        print(f"\nRound {i+1}")
        
        comp = random.randint(1,3)
        choice = int(input("Enter your Choice (1/2/3) : "))
        if (choice<1 or choice>3 ) :
            print("Invalid Choice")
            continue

        print("++++++++++++++++++++++++++++")
        print(f"You chose {value[choice]}")
        print("++++++++++++++++++++++++++++")
        print(f"Computer chose {value[comp]}") 
        print("______________________________")      
        if choice==comp :
            print("It is a Tie Game\n")

        elif ((choice==1 and comp==2)
             or (choice==2 and comp==3)
             or (choice==3 and comp==1)):
            print("You Won!!\n")
            player_score+=1

        else:
            print("You Lose!!\n")
            computer_score+=1
        print("______________________________")    
        i+=1  

    print(f"Your Score is {player_score}")
    print(f"Computer Score is {computer_score}")
    if (player_score>computer_score):
        print("You Won the Game!! :)")  
    elif(player_score == computer_score):
        print("This is a Tie Game!!")    
    else:
        print("You Lost the Game!! :(")      


print("**** ROCK SCISSOR PAPER Game ****\n")
print("---------------------------------\n")
print("Modes:")
print("A.Best of 3")
print("B.Best of 5")
print("C.Best of 7\n")
print("Choose an Option from the following:")
print("1.Rock")
print("2.Scissor")
print("3.Paper")
    
while True:
    game()    

    replay = input("You Want to Replay (Y/N) : ")
    if replay == 'N':
        break
          

