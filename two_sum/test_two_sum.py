from two_sum.two_sum import Two_Sum


def test_two_sum(two_sum):
    for i in range(len(two_sum["input"])):
        assert Two_Sum(two_sum["input"][i], two_sum["target"][i]) == two_sum["result"][i]
