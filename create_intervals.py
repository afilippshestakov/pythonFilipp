def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """
    # your code here
    if not data:
        return []
    data = list(data)
    data.sort()
    result_lst = []
    inizio = data[0]
    pre = inizio
    for x in data[1:]:
        if x == pre + 1:
            pre = x
        else:
            result_lst.append((inizio, pre))
            inizio = x
            pre = x
    result_lst.append((inizio, pre))
    return result_lst


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(create_intervals({1,3,5,7}))
    assert create_intervals({1,3,5,7}) == [(1, 1), (3, 3), (5, 5), (7, 7)]
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")