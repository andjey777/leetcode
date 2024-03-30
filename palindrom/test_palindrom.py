from palindrom.palindrom import Palindrome_Number


def test_palindrom(palindrom):
    for i in range(len(palindrom)):
        assert Palindrome_Number(palindrom[i]) == True


def test_not_palindrom(not_palindrom):
    for i in range(len(not_palindrom)):
        assert Palindrome_Number(not_palindrom[i]) == False
