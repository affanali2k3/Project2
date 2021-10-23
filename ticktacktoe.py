from random import choice
from os import system
index = [1,2,3,4,5,6,7,8,9]
game_mode = input("Do you want to play with computer?\n")
while True:
    def player_a_win():
        if board_solution[3] == "A" and board_solution[7] == "A" and board_solution[11] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[17] == "A" and board_solution[21] == "A" and board_solution[25] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[31] == "A" and board_solution[35] == "A" and board_solution[39] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[3] == "A" and board_solution[17] == "A" and board_solution[31] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[7] == "A" and board_solution[21] == "A" and board_solution[35] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[11] == "A" and board_solution[25] == "A" and board_solution[39] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[3] == "A" and board_solution[21] == "A" and board_solution[39] == "A":
            print("Player A Won")
            escape = input()
            exit()
        elif board_solution[11] == "A" and board_solution[21] == "A" and board_solution[31] == "A":
            print("Player A Won")
            escape = input()
            exit()

  
    def player_b_win():
        if board_solution[3] == "B" and board_solution[7] == "B" and board_solution[11] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[17] == "B" and board_solution[21] == "B" and board_solution[25] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[31] == "B" and board_solution[35] == "B" and board_solution[39] == "B":
            print("Player B Won")
            escape = input()
        elif board_solution[3] == "B" and board_solution[17] == "B" and board_solution[31] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[7] == "B" and board_solution[21] == "B" and board_solution[35] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[11] == "B" and board_solution[25] == "B" and board_solution[39] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[3] == "B" and board_solution[21] == "B" and board_solution[39] == "B":
            print("Player B Won")
            escape = input()
            exit()
        elif board_solution[11] == "B" and board_solution[21] == "B" and board_solution[31] == "B":
            print("Player B Won")
            escape = input()
            exit()





    board = ("  |1|\t|2|\t|3|\n  |4|\t|5|\t|6|\n  |7|\t|8|\t|9|\n")
    print(board)
    input_a_1 = int(input("Player A select\n"))
    if input_a_1 == 1:
        x = 1
        board_1 = board.replace("1", "A")
        print(board_1)
    elif input_a_1 == 2:
        board_1 = board.replace("2", "A")
        print(board_1)
    elif input_a_1 == 3:
        board_1 = board.replace("3", "A")
        print(board_1)
    elif input_a_1 == 4:
        board_1 = board.replace("4", "A")
        print(board_1)
    elif input_a_1 == 5:
        board_1 = board.replace("5", "A")
        print(board_1)
    elif input_a_1 == 6:
        board_1 = board.replace("6", "A")
        print(board_1)
    elif input_a_1 == 7:
        board_1 = board.replace("7", "A")
        print(board_1)
    elif input_a_1 == 8:
        board_1 = board.replace("8", "A")
        print(board_1)
    elif input_a_1 == 9:
        board_1 = board.replace("9", "A")
        print(board_1)
    board_solution = board_1
    player_a_win()
    

    if game_mode.upper() == "Y":
        choice_1 = choice(index)
        input_b_1 = choice_1
        if input_b_1 == 1:
            board_2 = board_1.replace("1", "B")
            print(board_2)
        elif input_b_1 == 2:
            board_2 = board_1.replace("2", "B")
            print(board_2)
        elif input_b_1 == 3:
            board_2 = board_1.replace("3", "B")
            print(board_2)
        elif input_b_1 == 4:
            board_2 = board_1.replace("4", "B")
            print(board_2)
        elif input_b_1 == 5:
            board_2 = board_1.replace("5", "B")
            print(board_2)
        elif input_b_1 == 6:
            board_2 = board_1.replace("6", "B")
            print(board_2)
        elif input_b_1 == 7:
            board_2 = board_1.replace("7", "B")
            print(board_2)
        elif input_b_1 == 8:
            board_2 = board_1.replace("8", "B")
            print(board_2)
        elif input_b_1 == 9:
            board_2 = board_1.replace("9", "B")
            print(board_2)
        board_solution = board_2
        player_b_win()
    else:
        input_b_1 = int(input("Player B select\n"))
        if input_b_1 == 1:
            board_2 = board_1.replace("1", "B")
            print(board_2)
        elif input_b_1 == 2:
            board_2 = board_1.replace("2", "B")
            print(board_2)
        elif input_b_1 == 3:
            board_2 = board_1.replace("3", "B")
            print(board_2)
        elif input_b_1 == 4:
            board_2 = board_1.replace("4", "B")
            print(board_2)
        elif input_b_1 == 5:
            board_2 = board_1.replace("5", "B")
            print(board_2)
        elif input_b_1 == 6:
            board_2 = board_1.replace("6", "B")
            print(board_2)
        elif input_b_1 == 7:
            board_2 = board_1.replace("7", "B")
            print(board_2)
        elif input_b_1 == 8:
            board_2 = board_1.replace("8", "B")
            print(board_2)
        elif input_b_1 == 9:
            board_2 = board_1.replace("9", "B")
            print(board_2)
        board_solution = board_2
        player_b_win()
        


    input_a_2 = int(input("Player A select again\n"))
    if input_a_2 == 1:
        board_3 = board_2.replace("1", "A")
        print(board_3)
    elif input_a_2 == 2:
        board_3 = board_2.replace("2", "A")
        print(board_3)
    elif input_a_2 == 3:
        board_3 = board_2.replace("3", "A")
        print(board_3)
    elif input_a_2 == 4:
        board_3 = board_2.replace("4", "A")
        print(board_3)
    elif input_a_2 == 5:
        board_3 = board_2.replace("5", "A")
        print(board_3)
    elif input_a_2 == 6:
        board_3 = board_2.replace("6", "A")
        print(board_3)
    elif input_a_2 == 7:
        board_3 = board_2.replace("7", "A")
        print(board_3)
    elif input_a_2 == 8:
        board_3 = board_2.replace("8", "A")
        print(board_3)
    elif input_a_2 == 9:
        board_3 = board_2.replace("9", "A")
        print(board_3)
    board_solution = board_3
    player_a_win()
    

    if game_mode.upper() == "Y":
        choice_2 = choice(index)
        input_b_2 = choice_2
        # input_b_2 = int(input("Player B select again\n"))
        if input_b_2 == 1:
            board_4 = board_3.replace("1", "B")
            print(board_4)
        elif input_b_2 == 2:
            board_4 = board_3.replace("2", "B")
            print(board_4)
        elif input_b_2 == 3:
            board_4 = board_3.replace("3", "B")
            print(board_4)
        elif input_b_2 == 4:
            board_4 = board_3.replace("4", "B")
            print(board_4)
        elif input_b_2 == 5:
            board_4 = board_3.replace("5", "B")
            print(board_4)
        elif input_b_2 == 6:
            board_4 = board_3.replace("6", "B")
            print(board_4)
        elif input_b_2 == 7:
            board_4 = board_3.replace("7", "B")
            print(board_4)
        elif input_b_2 == 8:
            board_4 = board_3.replace("8", "B")
            print(board_4)
        elif input_b_2 == 9:
            board_4 = board_3.replace("9", "B")
            print(board_4)
        board_solution = board_4
        player_b_win()
    else:
        input_b_2 = int(input("Player B select again\n"))
        if input_b_2 == 1:
            board_4 = board_3.replace("1", "B")
            print(board_4)
        elif input_b_2 == 2:
            board_4 = board_3.replace("2", "B")
            print(board_4)
        elif input_b_2 == 3:
            board_4 = board_3.replace("3", "B")
            print(board_4)
        elif input_b_2 == 4:
            board_4 = board_3.replace("4", "B")
            print(board_4)
        elif input_b_2 == 5:
            board_4 = board_3.replace("5", "B")
            print(board_4)
        elif input_b_2 == 6:
            board_4 = board_3.replace("6", "B")
            print(board_4)
        elif input_b_2 == 7:
            board_4 = board_3.replace("7", "B")
            print(board_4)
        elif input_b_2 == 8:
            board_4 = board_3.replace("8", "B")
            print(board_4)
        elif input_b_2 == 9:
            board_4 = board_3.replace("9", "B")
            print(board_4)
        board_solution = board_4
        player_b_win()
        

    input_a_3 = int(input("Player A select again\n"))
    if input_a_3 == 1:
        board_5 = board_4.replace("1", "A")
        print(board_5)
    elif input_a_3 == 2:
        board_5 = board_4.replace("2", "A")
        print(board_5)
    elif input_a_3 == 3:
        board_5 = board_4.replace("3", "A")
        print(board_5)
    elif input_a_3 == 4:
        board_5 = board_4.replace("4", "A")
        print(board_5)
    elif input_a_3 == 5:
        board_5 = board_4.replace("5", "A")
        print(board_5)
    elif input_a_3 == 6:
        board_5 = board_4.replace("6", "A")
        print(board_5)
    elif input_a_3 == 7:
        board_5 = board_4.replace("7", "A")
        print(board_5)
    elif input_a_3 == 8:
        board_5 = board_4.replace("8", "A")
        print(board_5)
    elif input_a_3 == 9:
        board_5 = board_4.replace("9", "A")
        print(board_5)
    board_solution = board_5
    player_a_win()
    
    if game_mode.upper() == "Y":
        choice_3 = choice(index)
        input_b_3 = choice_3
        if input_b_3 == 1:
            board_6 = board_5.replace("1", "B")
            print(board_6)
        elif input_b_3 == 2:
            board_6 = board_5.replace("2", "B")
            print(board_6)
        elif input_b_3 == 3:
            board_6 = board_5.replace("3", "B")
            print(board_6)
        elif input_b_3 == 4:
            board_6 = board_5.replace("4", "B")
            print(board_6)
        elif input_b_3 == 5:
            board_6 = board_5.replace("5", "B")
            print(board_6)
        elif input_b_3 == 6:
            board_6 = board_5.replace("6", "B")
            print(board_6)
        elif input_b_3 == 7:
            board_6 = board_5.replace("7", "B")
            print(board_6)
        elif input_b_3 == 8:
            board_6 = board_5.replace("8", "B")
            print(board_6)
        elif input_b_3 == 9:
            board_6 = board_5.replace("9", "B")
            print(board_6)
        board_solution = board_6
        player_b_win()
    else:
        input_b_3 = int(input("Player B select again\n"))
        if input_b_3 == 1:
            board_6 = board_5.replace("1", "B")
            print(board_6)
        elif input_b_3 == 2:
            board_6 = board_5.replace("2", "B")
            print(board_6)
        elif input_b_3 == 3:
            board_6 = board_5.replace("3", "B")
            print(board_6)
        elif input_b_3 == 4:
            board_6 = board_5.replace("4", "B")
            print(board_6)
        elif input_b_3 == 5:
            board_6 = board_5.replace("5", "B")
            print(board_6)
        elif input_b_3 == 6:
            board_6 = board_5.replace("6", "B")
            print(board_6)
        elif input_b_3 == 7:
            board_6 = board_5.replace("7", "B")
            print(board_6)
        elif input_b_3 == 8:
            board_6 = board_5.replace("8", "B")
            print(board_6)
        elif input_b_3 == 9:
            board_6 = board_5.replace("9", "B")
            print(board_6)
        board_solution = board_6
        player_b_win()
        

    input_a_4 = int(input("Player A select again\n"))
    if input_a_4 == 1:
        board_7 = board_6.replace("1", "A")
        print(board_7)
    elif input_a_4 == 2:
        board_7 = board_6.replace("2", "A")
        print(board_7)
    elif input_a_4 == 3:
        board_7 = board_6.replace("3", "A")
        print(board_7)
    elif input_a_4 == 4:
        board_7 = board_6.replace("4", "A")
        print(board_7)
    elif input_a_4 == 5:
        board_7 = board_6.replace("5", "A")
        print(board_7)
    elif input_a_4 == 6:
        board_7 = board_6.replace("6", "A")
        print(board_7)
    elif input_a_4 == 7:
        board_7 = board_6.replace("7", "A")
        print(board_7)
    elif input_a_4 == 8:
        board_7 = board_6.replace("8", "A")
        print(board_7)
    elif input_a_4 == 9:
        board_7 = board_6.replace("9", "A")
        print(board_7)
    board_solution = board_7
    player_a_win()
    


    if game_mode.upper() == "Y":
        choice_4 = choice(index)
        input_b_4 = choice_4
        # input_b_4 = int(input("Player B select again\n"))
        if input_b_4 == 1:
            board_8 = board_7.replace("1", "B")
            print(board_8)
        elif input_b_4 == 2:
            board_8 = board_7.replace("2", "B")
            print(board_8)
        elif input_b_4 == 3:
            board_8 = board_7.replace("3", "B")
            print(board_8)
        elif input_b_4 == 4:
            board_8 = board_7.replace("4", "B")
            print(board_8)
        elif input_b_4 == 5:
            board_8 = board_7.replace("5", "B")
            print(board_8)
        elif input_b_4 == 6:
            board_8 = board_7.replace("6", "B")
            print(board_8)
        elif input_b_4 == 7:
            board_8 = board_7.replace("7", "B")
            print(board_8)
        elif input_b_4 == 8:
            board_8 = board_7.replace("8", "B")
            print(board_8)
        elif input_b_4 == 9:
            board_8 = board_7.replace("9", "B")
            print(board_8)
        board_solution = board_8
        player_b_win()
    else:
        input_b_4 = int(input("Player B select again\n"))
        if input_b_4 == 1:
            board_8 = board_7.replace("1", "B")
            print(board_8)
        elif input_b_4 == 2:
            board_8 = board_7.replace("2", "B")
            print(board_8)
        elif input_b_4 == 3:
            board_8 = board_7.replace("3", "B")
            print(board_8)
        elif input_b_4 == 4:
            board_8 = board_7.replace("4", "B")
            print(board_8)
        elif input_b_4 == 5:
            board_8 = board_7.replace("5", "B")
            print(board_8)
        elif input_b_4 == 6:
            board_8 = board_7.replace("6", "B")
            print(board_8)
        elif input_b_4 == 7:
            board_8 = board_7.replace("7", "B")
            print(board_8)
        elif input_b_4 == 8:
            board_8 = board_7.replace("8", "B")
            print(board_8)
        elif input_b_4 == 9:
            board_8 = board_7.replace("9", "B")
            print(board_8)
        board_solution = board_8
        player_b_win()
        




    input_a_5 = int(input("Player A select again\n"))
    if input_a_5 == 1:
        board_9 = board_8.replace("1", "A")
        print(board_9)
    elif input_a_5 == 2:
        board_9 = board_8.replace("2", "A")
        print(board_9)
    elif input_a_5 == 3:
        board_9 = board_8.replace("3", "A")
        print(board_9)
    elif input_a_5 == 4:
        board_9 = board_8.replace("4", "A")
        print(board_9)
    elif input_a_5 == 5:
        board_9 = board_8.replace("5", "A")
        print(board_9)
    elif input_a_5 == 6:
        board_9 = board_8.replace("6", "A")
        print(board_9)
    elif input_a_5 == 7:
        board_9 = board_8.replace("7", "A")
        print(board_9)
    elif input_a_5 == 8:
        board_9 = board_8.replace("8", "A")
        print(board_9)
    elif input_a_5 == 9:
        board_9 = board_8.replace("9", "A")
        print(board_9)
    board_solution = board_9
    player_a_win()
    
    choice = print("Do you want to play again?  Y/N \n")
    if choice.upper() == "Y":
        exit()
    else:
        continue
    # print(board_3[3] == "1") #1
    # print(board_3[7] == "2") #2
    # print(board_3[11] == "3") #3
    # print(board_3[17] == "4") #4
    # print(board_3[21] == "5") #5
    # print(board_3[25] == "6") #6
    # print(board_3[31] == "7") #7
    # print(board_3[35] == "8") #8
    # print(board_3[39] == "9") #9

    # def player_a_win():
    #     # name = 'board_' + '9'
    #     # print(name)
    #     # print(name[3])
    #     # print(board_9[3])
    #     if board_solution[3] == "A" and board_solution[7] == "A" and board_solution[11] == "A":
    #         print("You won")
    #     elif board_solution[17] == "A" and board_solution[21] == "A" and board_solution[25] == "A":
    #         print("You won")
    #     elif board_solution[31] == "A" and board_solution[35] == "A" and board_solution[39] == "A":
    #         print("You won")
    #     elif board_solution[3] == "A" and board_solution[17] == "A" and board_solution[31] == "A":
    #         print("You won")
    #     elif board_solution[7] == "A" and board_solution[21] == "A" and board_solution[35] == "A":
    #         print("You won")
    #     elif board_solution[11] == "A" and board_solution[25] == "A" and board_solution[39] == "A":
    #         print("You won")

    # def player_b_win():
    #     if board_solution[3] == "A" and board_solution[7] == "A" and board_solution[11] == "A":
    #         print("You won")
    #     elif board_solution[17] == "A" and board_solution[21] == "A" and board_solution[25] == "A":
    #         print("You won")
    #     elif board_solution[31] == "A" and board_solution[35] == "A" and board_solution[39] == "A":
    #         print("You won")
    #     elif board_solution[3] == "A" and board_solution[17] == "A" and board_solution[31] == "A":
    #         print("You won")
    #     elif board_solution[7] == "A" and board_solution[21] == "A" and board_solution[35] == "A":
    #         print("You won")
    #     elif board_solution[11] == "A" and board_solution[25] == "A" and board_solution[39] == "A":
    #         print("You won")
    # player_a_win()
    escape = input()