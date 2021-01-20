def matrix(income):
    game_matrix = []
    first_line = []
    second_line = []
    third_line = []
    for _i in income:
        if len(first_line) < 3:
            first_line.append(_i)
        elif len(second_line) < 3:
            second_line.append(_i)
        else:
            third_line.append(_i)
    game_matrix.append(first_line)
    game_matrix.append(second_line)
    game_matrix.append(third_line)
    return game_matrix


def printing(field):
    first_line = "---------"
    second_line = "| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |"
    third_line = "| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |"
    fourth_line = "| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |"
    fifth_line = "---------"
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)


def judgement(game):
    xs = 0
    os = 0
    other = 0
    state = ""
    first_column = [game[0][0], game[1][0], game[2][0]]
    second_column = [game[0][1], game[1][1], game[2][1]]
    third_column = [game[0][2], game[1][2], game[2][2]]
    # Counting symbols
    for raw in game:
        for symbol in raw:
            if symbol == "X":
                xs += 1
            elif symbol == "O":
                os += 1
            else:
                other += 1
    # Checking raw
    for raw in game:
        if raw[0] == raw[1] and raw[0] == raw[2] and raw[0] == "X":
            state += "X"
        if raw[0] == raw[1] and raw[0] == raw[2] and raw[0] == "O":
            state += "O"
    # Checking columns
    if first_column[0] == first_column[1] and first_column[1] == first_column[2]:
        if first_column[0] == "X":
            state += "X"
        if first_column[0] == "O":
            state += "O"
    if second_column[0] == second_column[1] and second_column[1] == second_column[2]:
        if second_column[0] == "X":
            state += "X"
        if second_column[0] == "O":
            state += "O"
    if third_column[0] == third_column[1] and third_column[1] == third_column[2]:
        if third_column[0] == "X":
            state += "X"
        if third_column[0] == "O":
            state += "O"
    # Checking diagonals
    if game[0][0] == game[1][1] and game[0][0] == game[2][2]:  # First one
        if game[0][0] == "X":
            state += "X"
        if game[0][0] == "O":
            state += "O"
    if game[0][2] == game[1][1] and game[0][2] == game[2][0]:  # Second one
        if game[0][2] == "X":
            state += "X"
        if game[0][2] == "O":
            state += "O"
    # Choosing the winner
    if len(state) > 1 or xs - os > 1 or os - xs > 1:
        return "Impossible"
    elif state == "" and other != 0:
        return "Game not finished"
    elif state == "" and other == 0:
        return "Draw"
    else:
        if state == "X":
            return "X wins"
        else:
            return "O wins"


def coord_request(turn):
    numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    needed_numbers = ["1", "2", "3"]
    coordinates = input("Enter the coordinates: ")
    coord_list = coordinates.split()
    # checking if the coordinates are numbers in needed range
    _i = 0
    while _i < len(coord_list):
        if coord_list[_i] not in numbers_list:
            print("You should enter numbers!")
            return coord_request(turn)
        elif coord_list[_i] not in needed_numbers:
            print("Coordinates should be from 1 to 3!")
            return coord_request(turn)
        _i += 1

    # checking the position and making a first turn
    position1 = int(coord_list[0]) - 1
    position2 = int(coord_list[1]) - 1
    new_game_field = game_field
    place = new_game_field[position1][position2]
    if place != "X" and place != "O":
        if turn % 2 == 0:
            new_game_field[position1][position2] = "X"
            turn = turn + 1
        else:
            new_game_field[position1][position2] = "O"
    else:
        print("This cell is occupied! Choose another one!")
        return coord_request(turn)
    return new_game_field


situation = "_________"
game_field = matrix(situation)
printing(game_field)
for i in range (9):
    game_field = coord_request(i)
    printing(game_field)
    if judgement(game_field) != "Game not finished":
        break
print(judgement(game_field))
