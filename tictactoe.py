import os

#Full Game
def the_game():

    def restart_game():
        while True:
            restart = input("Would you like to play again? (y = Yes and n = No): ").strip().lower()
            if restart == "y":
                os.system('cls')
                return the_game()
            elif restart == "n":
                print("Thanks for playing.")
                break
            else:
                print("Input is not valid.")
        

    #Sets player variables
    player1 = 'Player1' # player1 name 
    player2 = 'Player2' # player2 name

    #Function to name the players
    def name_players(players): 
        for i in range(len(players)):  
            players[i] = input(f"Player{i+1}. Please enter your name: ").strip() or f"Player{i}" #Strip removes white space at the end - white space is considered "true" as a boolean
            print(f"Welcome to the game {players[i]}.")
        return players

    players = [player1, player2]
    players = name_players(players)

    # Assigns the global variables player1, and player2, from the function
    player1, player2 = players

    print('Choose where you would like to go. The squares are numbered 1-9 and imputing one of these numbers will place your letter.')

    #Creates the board dictionary to assign moves to later 
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '} 

    #Board for the rules
    example_board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    #This Draws the board
    def display(board): 
        print(board[1] + '|' + board[2] + '|' + board[3]) #row1
        print(board[4] + '|' + board[5] + '|' + board[6]) #row2
        print(board[7] + '|' + board[8] + '|' + board[9]) #row3
        print('----------')
    display(example_board)

    print(' ')
    print('This is your current blank board.')
    display(board)
    

    #Check win conditions 
    def check_win():
        conditions = [(1,4,7),(2,5,8),(3,5,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7)]
        for condition in conditions: 
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
                return board[condition[0]]
        return None

    #Checks to see if the choice is good 
    def choice_check(choice):
        while True:
            if choice.isdigit() and int(choice) in range(1, 10):
                return int(choice)  # Return the validated choice as an integer
            else:
                choice = input("This choice is not correct. Choose again: ")
    
    #Game Itself 
    def game_loop():
        #Establishes Iterator 
        turn_count = 0
        current_player = 0 
        #Game loop
        while turn_count < 9:
            #Choice definition
            choice = input(f'{players[current_player]} please make your choice. ')
            choice = choice_check(choice)
            if board[choice] == ' ':
                if current_player == 0:
                    board[choice] = 'X'
                else: 
                    board[choice] = '0'
                if check_win():
                    print(f"Congratulations {players[current_player]}, you have won!")
                    display(board)
                current_player = 1 - current_player
                turn_count += 1
                display(board)
            else:
                print("This spot is already taken, please choose another.")
        print("Tie game!")
    game_loop()
    restart_game()
the_game()