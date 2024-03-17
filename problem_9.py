#9. Palindrome Number
#Given an integer x, return true if x is a palindrome, and false otherwise.

#n = input("N: ")
n = str(121)
len = len(n)
polin = True
for i in range(0, len // 2):
    if n[i] != n[len - i - 1]:
        polin = False

if polin == True:
    print(True)
else:
    print(False)
