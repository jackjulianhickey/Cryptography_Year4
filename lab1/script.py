import binascii


def xor_ints(i1, i2):
    i1_bin = format(i1, '04b')
    i2_bin = format(i2, '04b')
    result = i1 ^ i2
    result_bin = format(result, '04b')
    print "i1 (binary) " + i1_bin
    print "i2 (binary) " + i2_bin
    print "result (binary) " + result_bin
    print "result was", result


def xor_strings(s1, s2):
    s1_ord = convert_to_hex(s1)
    s2_ord = convert_to_hex(s2)

    print "s1 numeric", s1_ord
    print "s2 numeric", s2_ord

    s1_bin = convert_string_to_bin(s1_ord)
    s2_bin = convert_string_to_bin(s2_ord)

    print "s1 (binary)", s1_bin
    print "s2 (binary)", s2_bin

    result = xor_hex(s1_ord, s2_ord)
    result_bin = convert_string_to_bin(result)

    # result_hex = convert_dec_to_hex(result)
    # result_char = convert_bin_char(result_bin)

    result_char = convert_dec_to_char(result)

    print "result (binary)", result_bin
    print "result", result

    for i in range(len(result_char)):
        print result_char[i],


def convert_to_hex(s):
    s_ord = []

    for i in range(len(s)):
        s_ord += [ord(s[i])]

    return s_ord


def convert_bin_char(bin):
    n = int(bin)
    char = binascii.unhexify('%x' % n)
    return char


def convert_dec_to_hex(d):
    arr = []
    for i in range(len(d)):
        arr.append(format(d[i], '02x'))
    return arr


def convert_dec_to_char(dec):
    result = []

    for i in range( len(dec) ):
        result.append(chr(dec[i]))

    return result


def convert_string_to_bin(s):
    s_bin = ''
    for i in range(len(s)):
        s_bin += format(s[i], '08b') + " "
    return s_bin


def xor_hex(s1, s2):
    result = []

    if len(s1) < len(s2):
        s1_len = len(s1)
        s2_len = len(s2)

        dif = s2_len - s1_len

        for i in range(dif):
            s1.insert(0, 0)

    if len(s1) > len(s2):
        s1_len = len(s1)
        s2_len = len(s2)

        dif = s1_len - s2_len

        for i in range(dif):
            s2.insert(0, 0)

    for i in range(len(s2)):
        result.append(s1[i] ^ s2[i])
    return result


def hex_decoding(s):
    result = s.decode("hex")
    return result


def xor_2_strings(s1, s2):
    s1_decode = hex_decoding(s1)
    s2_decode = hex_decoding(s2)

    xor_strings(s1_decode, s2_decode)

if __name__ == '__main__':
    # xor_ints(11, 3)
    #
    # xor_strings("COMP8004COMP8004 Plain", "ABCDEF1234567890")

    xor_2_strings("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
