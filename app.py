from test_app import test_xor, test_nim_sum

'''
*** Nim Tutor ***
A guide on how to become as good as Nim's AI. Discover the beauty of the game theory behind it.
'''


def xor(bit1, bit2):
    if bit1 == bit2:
        return True
    return False

# TODO rename this function
def sort(s1, s2):
    info = []

    if len(s1) < len(s2):
        info.append(s1)
        info.append(s2)
    else:
        info.append(s2)
        info.append(s1)
    
    info.append(abs(len(s1) - len(s2)))

    return info


# TODO this only works if the Nim game has 2 rows, refactor it to account for mores
def nim_sum(s1, s2):
    is_position_secure = True

    if len(s1) != len(s2):
        s_list = sort(s1, s2)
        s = '0' * s_list[2] + s_list[0]

        for i in range(len(s)):
            if not xor(s[i], s_list[1][i]):
                is_position_secure = False
    else:
        for i in range(len(s1)):
            if not xor(s1[i], s2[i]):
                is_position_secure = False

    return is_position_secure


if __name__ == '__main__':
    test_xor(xor)
    test_nim_sum(nim_sum)
