print("Name   : Sahil Gurav")
print("USN    : 1AY24AI093")
print("Section: O\n")
def isValidChessBoard(board):
    """
    Checks if a given dictionary represents a valid chess board.
    Args:
        board: A dictionary where keys are chess board positions (e.g., '1h', '6c')
               and values are chess pieces (e.g., 'bking', 'wqueen').
    Returns:
        True if the board is valid, False otherwise.
    """
    if not board:
        return True      
    valid_pieces = {'wking', 'wqueen', 'wrook', 'wknight', 'wbishop', 'wpawn',
                    'bking', 'bqueen', 'brook', 'bknight', 'bbishop', 'bpawn'}
    valid_rows = {'1', '2', '3', '4', '5', '6', '7', '8'}
    valid_cols = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    piece_counts = {}
    for position, piece in board.items():
        if not (position[0] in valid_rows and position[1] in valid_cols):
            return False 
        if piece not in valid_pieces:
            return False 
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
    if piece_counts.get('wking', 0) != 1 or piece_counts.get('bking', 0) != 1:
        return False 
    if piece_counts.get('wpawn', 0) > 8 or piece_counts.get('bpawn', 0) > 8:
        return False 
    return True  
board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
board2 = {'1a': 'wking', '2b': 'bking', '3c': 'wqueen', '4d': 'wrook', '5e': 'bbishop', '6f': 'wpawn', '7g': 'bpawn', '8h': 'wknight', '9i': 'bking'} # Invalid position
board3 = {'1a': 'wking', '2b': 'bking', '3c': 'wqueen', '4d': 'wrook', '5e': 'bbishop', '6f': 'wpawn', '7g': 'bpawn', '8h': 'wknight', '1b': 'wking'} # Two white kings
board4 = {'1a': 'wking', '2b': 'bking', '3c': 'wqueen', '4d': 'wrook', '5e': 'bbishop', '6f': 'wpawn', '7g': 'bpawn', '8h': 'wknight', '1c': 'wpawn', '1d': 'wpawn', '1e': 'wpawn', '1f': 'wpawn', '1g': 'wpawn', '1h': 'wpawn', '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn'} # 9 white pawns
print(f"Board 1 is valid: {isValidChessBoard(board1)}")  
print(f"Board 2 is valid: {isValidChessBoard(board2)}")  
print(f"Board 3 is valid: {isValidChessBoard(board3)}")  
print(f"Board 4 is valid: {isValidChessBoard(board4)}")  
empty_board = {}
print(f"Empty board is valid: {isValidChessBoard(empty_board)}") 
