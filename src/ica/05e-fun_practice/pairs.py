def printPairs(n, m):
    """
    Print pairs of number, the first number varies from 0 to n-1
    and each first number is paired with each second number.  The second
    number varies from 0 to m-1
    :param n:
    :param m:
    :return:
    """
    for i in range(n):
        for j in range(m):
            print("(", i, j, ")")


printPairs(3, 5)
