from search_insert.search_insert import Search_Insert


def test_search_inset(search_insert):
    for i in range(len(search_insert["nums"])):
        assert (
            Search_Insert(search_insert["nums"][i], search_insert["target"][i])
            == search_insert["output"][i]
        )
