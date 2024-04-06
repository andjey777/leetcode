from len_last_word.len_last_word import Len_last_Word


def test_len_last_word(len_last_word):
    for i in range(len(len_last_word["str"])):
        assert Len_last_Word(len_last_word["str"][i]) == len_last_word["len"][i]
