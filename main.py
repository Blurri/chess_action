BOARD_SIZE = 8

def create_board():
    board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Player pieces
    board[4][3] = 'P'  # Pawn on D4
    board[5][4] = 'N'  # Knight on E3

    # Enemy pieces
    board[3][2] = 'p'  # Enemy Pawn on C5
    board[2][5] = 'r'  # Enemy Rook on F6

    return board

def print_board(board):
    print("  A B C D E F G H")
    for i, row in enumerate(board):
        print(f"{8 - i} " + " ".join(row))
    print()

def algebraic_to_coords(pos):
    col = ord(pos[0].upper()) - ord('A')
    row = 8 - int(pos[1])
    return row, col

def is_on_board(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

def get_possible_moves(piece, row, col, board):
    moves = []

    if piece == 'P':
        # Pawn moves forward (up the board)
        if is_on_board(row - 1, col) and board[row - 1][col] == '.':
            moves.append((row - 1, col))
        # Pawn attacks diagonally
        for dc in [-1, 1]:
            r, c = row - 1, col + dc
            if is_on_board(r, c) and board[r][c].islower():
                moves.append((r, c))

    elif piece == 'N':
        # Knight movement (L-shapes)
        knight_moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1),
        ]
        for dr, dc in knight_moves:
            r, c = row + dr, col + dc
            if is_on_board(r, c) and (board[r][c] == '.' or board[r][c].islower()):
                moves.append((r, c))

    return moves

def move_piece(board, from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col]
    target = board[to_row][to_col]

    if target.islower():
        print(f">>> {piece} captured enemy {target} at {chr(to_col + ord('A'))}{8 - to_row}!")

    board[to_row][to_col] = piece
    board[from_row][from_col] = '.'
    
def find_pieces(board, is_enemy=False):
    pieces = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if is_enemy and piece.islower():
                pieces.append((row, col, piece))
            elif not is_enemy and piece.isupper():
                pieces.append((row, col, piece))
    return pieces

def enemy_turn(board):
    enemies = find_pieces(board, is_enemy=True)
    players = find_pieces(board, is_enemy=False)

    for row, col, piece in enemies:
        # Check if any player piece is adjacent (simple attack rule)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if is_on_board(r, c) and board[r][c].isupper():
                    print(f"!!! {piece} attacks and captures {board[r][c]} at {chr(c + ord('A'))}{8 - r}")
                    board[r][c] = piece
                    board[row][col] = '.'
                    return  # One enemy acts per turn for now

        # No adjacent attack? Move toward the closest player
        if not players:
            return

        # Find closest player
        target_row, target_col, _ = min(
            players,
            key=lambda p: abs(p[0] - row) + abs(p[1] - col)
        )

        # Decide direction
        dr = 0 if target_row == row else (1 if target_row > row else -1)
        dc = 0 if target_col == col else (1 if target_col > col else -1)

        new_row = row + dr
        new_col = col + dc

        if is_on_board(new_row, new_col) and board[new_row][new_col] == '.':
            board[new_row][new_col] = piece
            board[row][col] = '.'
            print(f"... {piece} moves to {chr(new_col + ord('A'))}{8 - new_row}")
            return  # Again: only 1 enemy moves per turn for simplicity


def main():
    board = create_board()

    while True:
        print_board(board)

        from_pos = input("Select a piece to move (e.g. A2): ").strip()
        if len(from_pos) != 2:
            print("Invalid input.")
            continue

        from_row, from_col = algebraic_to_coords(from_pos)
        if not is_on_board(from_row, from_col):
            print("Out of bounds.")
            continue

        piece = board[from_row][from_col]
        if piece not in ['P', 'N']:
            print("Not a movable player piece.")
            continue

        moves = get_possible_moves(piece, from_row, from_col, board)
        if not moves:
            print("No valid moves.")
            continue

        print("Possible moves:")
        for idx, (r, c) in enumerate(moves):
            print(f"{idx}: {chr(c + ord('A'))}{8 - r}")

        move_choice = input("Select move index: ").strip()
        if not move_choice.isdigit() or not (0 <= int(move_choice) < len(moves)):
            print("Invalid choice.")
            continue

        to_row, to_col = moves[int(move_choice)]
        move_piece(board, from_row, from_col, to_row, to_col)

        enemy_turn(board)

if __name__ == "__main__":
    main()