from com_prefix.com_prefix import Longest_Common_Prefix


def test_com_prefix(com_prefix):
    for i in range(len(com_prefix)):
        assert Longest_Common_Prefix(com_prefix["input"][i]) == com_prefix["result"][i]
