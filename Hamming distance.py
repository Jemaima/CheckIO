def checkio(n, m):
    n_bin = bin_form(n)
    m_bin = bin_form(m)
    dist = [int(a != b) for a,b in zip(n_bin,m_bin)]
    return sum(dist)

# import numpy as np
# numpy variant
# def bin_form(a):
#     ans = np.empty(shape=(0))
#     while a > 0:
#         ans = np.append(ans, a % 2)
#         a = a // 2
#     ans = np.lib.pad(ans, (0, 10 - len(ans)), 'constant', constant_values=0)
#     return ans[::-1]


def bin_form(a):
    ans = []
    while a > 0:
        ans.append(a % 2)
        a = a // 2
    ans += [0]*(10 - len(ans))
    ans.reverse()
    return ans


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
