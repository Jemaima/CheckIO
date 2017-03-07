def checkio(m):
    ans = False
    dirs = [[1, 0], [0, 1], [1, 1], [1, -1]]
    for i in range(len(m)):
        for j in range(len(m)):
            seq_len = 1
            for d in dirs:
                if (try_make_seq(m, i, j, seq_len, d)):
                    ans = True
                    break
    print(ans)
    return ans


def try_make_seq(m, i, j, l, dir):
    if l == 4:
        return True
    else:
        try:
            if m[i + dir[0]][j + dir[1]] == m[i][j] and i >= 0 and j >= 0:
                l += 1
                return try_make_seq(m, i + dir[0], j + dir[1], l, dir)
        except:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

    assert checkio([
        [6, 9, 1, 1, 6, 2],
        [5, 9, 7, 8, 2, 5],
        [2, 1, 1, 7, 9, 8],
        [1, 8, 1, 4, 7, 4],
        [7, 8, 5, 4, 5, 1],
        [6, 4, 8, 8, 1, 8]
    ]) == False, "Diagonal"
