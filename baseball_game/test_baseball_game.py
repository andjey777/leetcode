from baseball_game.baseball_game import Baseball_Game


def test_len_last_word(baseball_game):
    for i in range(len(baseball_game["input"])):
        assert Baseball_Game(baseball_game["input"][i]) == baseball_game["result"][i]
