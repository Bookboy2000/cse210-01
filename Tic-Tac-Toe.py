def main():
    game = True
    o = True
    x = False
    o_games = 0
    x_games = 0
    num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
    print("This is a first to 3 wins match.")
    print()

    while game == True:
        print(f"Scores: o [{o_games} : {x_games}] x")
        print()
        print(*num_list, sep= "/")
        if o == True:
            user = str(input("\no's turn. Choose 1-9: "))
            assign_o(user, num_list)
            o_games = find_outcome_o(num_list, o_games)
            x = True
            o = False
        elif x == True:
            user = str(input("\nx's turn. Choose 1-9: "))
            assign_x(user, num_list)
            x_games = find_outcome_x(num_list, x_games)
            o = True
            x = False



def assign_o(user, num_list):
    if user == "6":
        user = "6\n"
    elif user == "3":
        user = "3\n"
    for i in range (len(num_list)):
        if user == num_list[i]:
            if i == 6 or i == 3:
                num_list[i] = "o\n"
            else:
                num_list[i] = "o"


def assign_x(user, num_list):
    if user == "6":
        user = "6\n"
    elif user == "3":
        user = "3\n"
    for i in range (len(num_list)):
        if user == num_list[i]:
            if i == 6 or i == 3:
                num_list[i] = "x\n"
            else:
                num_list[i] = "x"


def find_outcome_o(num_list, o_games):
    # HERE IS THE ISSUE
    for i in range (len(num_list)):
        if num_list[1] and num_list[2] and num_list[3] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[4] and num_list[5] and num_list[6] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[7] and num_list[8] and num_list[9] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[1] and num_list[4] and num_list[7] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[2] and num_list[5] and num_list[8] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[3] and num_list[6] and num_list[9] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[1] and num_list[5] and num_list[9] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif num_list[3] and num_list[5] and num_list[7] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        else:
            pass

    
def find_outcome_x(num_list, x_games):
    for i in range (len(num_list)):
        if num_list[1] and num_list[2] and num_list[3] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[4] and num_list[5] and num_list[6] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[7] and num_list[8] and num_list[9] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[1] and num_list[4] and num_list[7] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[2] and num_list[5] and num_list[8] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[3] and num_list[6] and num_list[9] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[1] and num_list[5] and num_list[9] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif num_list[3] and num_list[5] and num_list[7] == "x" or "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        else:
            pass
        





    #if user == num1:
        #num1 = "o"
    #elif user == num2:
        #num2 = "o"
    #elif user == num3:
        #num3 = "o"
    #elif user == num4:
        #num4 = "o"
    #elif user == num5:
        #num5 = "o"
    #elif user == num6:
        #num6 = "o"
    #elif user == num7:
        #num7 = "o"
    #elif user == num8:
        #num8 = "o"
    #elif user == num9:
        #num9 = "o"
    #else:
        #print("\nSorry, that box is unavailable.")






main()