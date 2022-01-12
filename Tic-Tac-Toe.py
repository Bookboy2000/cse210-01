def main():
    game = True
    o = True
    x = False
    o_games = 0
    x_games = 0
    num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
    print("This is a first to 3 wins match.")

    while game == True:
        print(f"\nScores: o [{o_games} : {x_games}] x")
        print()
        print(*num_list, sep= "/")
        if o == True:
            user = str(input("\no's turn. Choose 1-9: "))
            assign_o(user, num_list)
            num_list, o_games = find_outcome_o(num_list, o_games)
            num_list = test_draw(num_list)
            if o_games == 3:
                print("\n   * * * * * * * * * * * * * *   ")
                print("~~~Player x has won the match!~~~")
                print("   * * * * * * * * * * * * * *   ")
                print("\n If you would like to play again kill this terminal and restart.")
                game = False
            x = True
            o = False
        elif x == True:
            user = str(input("\nx's turn. Choose 1-9: "))
            assign_x(user, num_list)
            num_list, x_games = find_outcome_x(num_list, x_games)
            num_list = test_draw(num_list)
            if x_games == 3:
                print("\n   * * * * * * * * * * * * * *   ")
                print("~~~Player x has won the match!~~~")
                print("   * * * * * * * * * * * * * *   ")
                print("\n If you would like to play again kill this terminal and restart.")
                game = False
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
    for i in range (len(num_list)):
        if num_list[1] == "o" and num_list[2] == "o" and num_list[3] == "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[4] == "o" and num_list[5] == "o" and num_list[6] == "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[7] == "o" and num_list[8] == "o" and num_list[9] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[1] == "o" and num_list[4] == "o" and num_list[7] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[2] == "o" and num_list[5] == "o" and num_list[8] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[3] == "o\n" and num_list[6] == "o\n" and num_list[9] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[1] == "o" and num_list[5] == "o" and num_list[9] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        elif num_list[3] == "o\n" and num_list[5] == "o" and num_list[7] == "o":
            print("\nPlayer o has won a game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, o_games

        else:
            num_list = num_list
            o_games += 0
            return num_list, o_games

    
def find_outcome_x(num_list, x_games):
    for i in range (len(num_list)):
        if num_list[1] == "x" and num_list[2] == "x" and num_list[3] == "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[4] == "x" and num_list[5] == "x" and num_list[6] == "x\n":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[7] == "x" and num_list[8] == "x" and num_list[9] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[1] == "x" and num_list[4] == "x" and num_list[7] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[2] == "x" and num_list[5] == "x" and num_list[8] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[3] == "x\n" and num_list[6] == "x\n" and num_list[9] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[1] == "x" and num_list[5] == "x" and num_list[9] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games

        elif num_list[3] == "x\n" and num_list[5] == "x" and num_list[7] == "x":
            print("\nPlayer x has won a game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return num_list, x_games
            

        else:
            x_games += 0
            num_list = num_list
            return num_list, x_games


def test_draw(num_list):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    is_there = any([num in num_list for num in nums])
    if is_there == False:
        num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
        print("\n\nDraw! Try again")
        return num_list
    else:
        num_list = num_list
        return num_list


main()