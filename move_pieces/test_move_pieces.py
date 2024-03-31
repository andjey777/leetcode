from move_pieces.move_pieces import Move_Pieces

def test_move_pieces(move_pieces):
    for i in range(len(move_pieces["input"])):
        assert Move_Pieces(move_pieces["input"][i], move_pieces["target"][i]) == True

def test_not_move_pieces(not_move_pieces):
    for i in range(len(not_move_pieces["input"])):
        assert Move_Pieces(not_move_pieces["input"][i], not_move_pieces["target"][i]) == False
