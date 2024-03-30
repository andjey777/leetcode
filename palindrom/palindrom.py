def Palindrome_Number(n: int):
    n = str(n)
    length = len(n)
    for i in range(0, length // 2):
        if n[i] != n[length - i - 1]:
            return False
    return True
