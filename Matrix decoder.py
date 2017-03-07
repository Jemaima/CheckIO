#    Help Sofia write a decrypter for the passwords that Nikola
# will encrypt through the cipher map. A cipher grille is
# a 4×4 square of paper with four windows cut out. Placing
# the grille on a paper sheet of the same size, the encoder
# writes down the first four symbols of his password inside
# the windows (see fig. below). After that, the encoder
# turns the grille 90 degrees clockwise. The symbols written
# earlier become hidden under the grille and clean paper
# appears inside the windows. The encoder then writes down
# the next four symbols of the password in the windows and
# turns the grille 90 degrees again. Then, they write down
# the following four symbols and turns the grille once more.
#    Lastly, they write down the final four symbols of the password.
# Without the same cipher grille, it is difficult to discern
# the password from the resulting square comprised of 16 symbols.
# Thus, the encoder can be confident that no hooligan will easily
# gain access to the locked door.


def recall_password(cipher_grille, ciphered_password):
    passw = ""
    for i in range(4):
        passw += (
            ''.join([y for row1, row2 in zip(cipher_grille, ciphered_password)
                     for x, y in zip(row1, row2) if x == 'X']))
        cipher_grille = rotate_matrix(cipher_grille)
    print(passw)
    return passw


def rotate_matrix(m):
    a = [x for x in m]
    for i in range(4):
        for j in range(4):
            a[i] = a[i][:j] + m[-(j + 1)][i] + a[i][j + 1:]
    return a


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('First example', recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd')

    print('Second example', recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy')
