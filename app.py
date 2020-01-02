win = False
slots = ["0"," "," "," "," "," "," "," "," "," "]
divider = "-----+-----+-----"
isChanceOfPlayer2 = False
player1, player2 = 'O', 'X'
AI = False

def printFormat():
    print(f"\t   {slots[7]}  |  {slots[8]}  |  {slots[9]}  ")
    print("\t",divider)
    print(f"\t   {slots[4]}  |  {slots[5]}  |  {slots[6]}  ")
    print("\t",divider)
    print(f"\t   {slots[1]}  |  {slots[2]}  |  {slots[3]}  ")

def play(player):
    try:
        tick(int(input(f"\nEnter the position for {player} (think it as a numpad): ")), player)
    except ValueError:
        print("Oop! you entered wrong input")
        play(player)

def tick(position, player):
    if 0 < position < 10 and checkPositionIsEmpty(position):
        slots[position] = player
    elif checkPositionIsEmpty(position):
        print("This position is already occupied..")
        pass
    else:
        print("please enter the position from 1 to 9...")
        tick(position, player)
        pass
    printFormat()

def checkPositionIsEmpty(position):
    if slots[position] == " ":
        return True

def allPositionsDone():
    flag = True
    for slot in slots:
        if slot ==" ":
            flag = False
    return flag

def winner():
    flag = False
    i = 0
    # Cross
    if(slots[i+1] == slots[i+5] == slots[i+9] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+1] else 'player2'} won!")
    if(slots[i+3] == slots[i+5] == slots[i+7] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+3] else 'player2'} won!")
    # Horizontal
    if(slots[i+1] == slots[i+2] == slots[i+3] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+1] else 'player2'} won!")
    if(slots[i+4] == slots[i+5] == slots[i+6] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+4] else 'player2'} won!")
    if(slots[i+7] == slots[i+8] == slots[i+9] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+7] else 'player2'} won!")
    # Vertical
    if(slots[i+1] == slots[i+4] == slots[i+7] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+1] else 'player2'} won!")
    if(slots[i+2] == slots[i+5] == slots[i+8] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+2] else 'player2'} won!")
    if(slots[i+3] == slots[i+6] == slots[i+9] != " "):
        flag = True
        print(f"{'player1' if player1 == slots[i+3] else 'player2'} won!")
    return flag


# main function
if __name__ == "__main__":
    print("Your are playing against AI👽")
    player1 = input("Choose 'X' or 'O' : ").upper()
    if player1 == 'X' or player1 == 'O':
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    else:
        print("Selecting by default values:\n Player1: 'X' and: Player2 'O'")

    printFormat()

    while not win and not allPositionsDone():
        if isChanceOfPlayer2:
            play(player2)
            isChanceOfPlayer2 = False
        else:
            play(player1)
            isChanceOfPlayer2 = True
        win = winner()
    else:
        if not win:
            print("It's a draw..\nLooks like you both have the similar amount of brain")
        print("Thank you!")