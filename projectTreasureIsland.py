print("Welcome to Treasure Island.Your mission is to find the treasure.")

user_input = input("Which way you want to go? Right? Press R or r or left? Press L or l: ")
user_input = user_input.lower()

if user_input == "r":
    print("you fall into a hole. Game over")
    exit()
if user_input == "l":
    swimOrWait = input("you wanna Swim? press S or s or you want to wait? Press W/w: ")
    swimOrWait = swimOrWait.lower()

    if swimOrWait == 's':
        print("Attacked by trout. Game over")
        exit()
    elif swimOrWait == "w":

        door = input("Which door you wanna go? Red/R or Blue/B or Yellow/Y: ")
        door = door.lower()
        if door == 'r':
            print("Burned by fire. Game Over.")
            exit()
        elif door == 'b':
            print("Eaten by beasts. Game Over.")
            exit()
        else:
            print("WOW! You win!")
            exit()














