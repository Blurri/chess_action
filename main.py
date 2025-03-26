BOARD_SIZE = 8

# Sample board with empty cells represented by '.'
def create_board():
    board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Place example player pieces
    board[7][0] = 'R'  # Rook
    board[7][1] = 'N'  # Knight
    board[6][0] = 'P'  # Pawn

    # Place example enemies
    board[0][7] = 'r'  # Enemy Rook
    board[1][7] = 'p'  # Enemy Pawn

    return board

# Print board with row/column labels
def print_board(board):
    print("  A B C D E F G H")
    for i, row in enumerate(board):
        print(f"{8 - i} " + " ".join(row))
    print()

# Main loop (just displays the board for now)
def main():
    board = create_board()
    print_board(board)

if __name__ == "__main__":
    main()