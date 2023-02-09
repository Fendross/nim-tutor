'''
Testing file
'''

def test_xor(xor):
    print("Testing xor(bit1, bit2)...")

    num_tc = 4
    tc1 = (0, 0)
    tc2 = (0, 1)
    tc3 = (1, 0)
    tc4 = (1, 1)

    assert xor(*tc1), "Test 1 failed"
    assert not xor(*tc2), "Test 2 failed"
    assert not xor(*tc3), "Test 3 failed"
    assert xor(*tc4), "Test 4 failed"

    print("All " + str(num_tc) + " test cases for the xor function passed!")


def test_nim_sum(nim_sum):
    print("Testing nim_sum(s1, s2)...")

    num_tc = 5
    tc1 = ('100', '100')
    tc2 = ('001', '010')
    tc3 = ('111', '111')
    tc4 = ('1', '101010')
    tc5 = ('1', '00001')

    assert nim_sum(*tc1), "Test 1 failed"
    assert not nim_sum(*tc2), "Test 2 failed"
    assert nim_sum(*tc3), "Test 3 failed"
    assert not nim_sum(*tc4), "Test 4 failed"
    assert nim_sum(*tc5), "Test 5 failed"

    print("All " + str(num_tc) + " test cases for the nim_sum function passed!")
