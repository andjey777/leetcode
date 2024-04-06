from remove_duplicates.remove_duplicates import Remove_Duplicates


def test_remove_duplicates(remove_duplicates):
    for i in range(len(remove_duplicates["input"])):
        assert Remove_Duplicates(remove_duplicates["input"][i]) == (
            remove_duplicates["k"][i],
            remove_duplicates["target"][i],
        )
