def read_data():
    with open("./inputs/in4.txt") as file:
        numbers_called = [int(num) for num in file.readline().strip().split(",")]
        file.readline()
        board_strings = file.read().strip().split("\n\n")
        
        boards = []
        for current_board in board_strings:
            board = []
            current_board = current_board.split("\n")
            for row in current_board:
                row = row.split()
                row = [int(x) for x in row]
                board.append(row)
            boards.append(board)
    return numbers_called, boards

def update_board(board: list[list[int | str]], number_called: int) -> None:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number_called:
                board[i][j] = 'x'

def is_winner(board: list[list[int | str]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        if all([num == 'x' for num in board[i]]):
            return True
        
    for j in range(cols):
        if all([board[i][j] == 'x' for i in range(rows)]):
            return True
    return False

def calc_score(board: list[list[int | str]], number_called: int):
    rows = len(board)
    cols = len(board[0])
    total = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != 'x':
                total += board[i][j]
    return total * number_called

def play_part1():
    numbers_called, boards = read_data()
    
    i = 0
    winner = 0
    while not winner:
        number_called = numbers_called[i]
        for board in boards:
            update_board(board, number_called)
            if is_winner(board):
                winner = board
                break
        i += 1
    return winner, number_called

def play_part2():
    numbers_called, boards = read_data()
    
    i = 0
    board_winners = [0] * len(boards)
    while not all(board_winners):
        number_called = numbers_called[i]
        for j, board in enumerate(boards):
            if not board_winners[j]:
                update_board(board, number_called)
                if is_winner(board):
                    winner = board
                    board_winners[j] = 1
        i += 1
    return winner, number_called
    

def main():
    winner1, number_called1 = play_part1()
    print(f"The answer to part 1 is {calc_score(winner1, number_called1)}")
    winner2, number_called2 = play_part2()
    print(f"The answer to part 2 is {calc_score(winner2, number_called2)}")



if __name__ == "__main__":
    main()





