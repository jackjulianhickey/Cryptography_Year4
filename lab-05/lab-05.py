import binascii
import struct


def convert_to_hex(s):
    list_to_return = []
    # s = int(s)
    print s
    for i in range(len(s)):
        list_to_return.append(hex(s[i]))
    return list_to_return


def xor_strings(s1, s2):
    s1_ord = convert_to_dec(s1)
    s2_ord = convert_to_dec(s2)

    result = xor_dec(s1_ord, s2_ord)
    result_hex = convert_to_hex(result)

    return result_hex
    #
    # for i in range(len(result_char)):
    #     print result_char[i],
    # s1_ord = convert_to_dec(s1)
    # # key_ord = convert_to_dec(key)
    #
    # s1_hex = convert_to_hex(s1)
    # # key_hex = convert_to_hex(key)
    # print s1_hex
    # print key
    #
    # result = []
    #
    # for i in range(len(key_hex)):
    #     for x in range(len(s1_hex)):
    #         result.append(hex(bytes(s1_hex[x]) ^ bytes(key_hex[i])))
    #
    # print result

    # result = xor_dec(s1_ord, key_ord)
    #
    # result_hex = convert_to_hex(result)
    #
    # # result_hex = convert_dec_to_hex(result)
    # # result_char = convert_bin_char(result_bin)
    #
    # result_char = convert_dec_to_char(result)
    #
    # print "result", result_hex
    #
    # print "char"
    # for i in range(len(result_char)):
    #     print result_char[i],
    # print "\n"


def convert_to_dec(s):
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

    for i in range(len(dec)):
        result.append(chr(dec[i]))

    return result


def convert_string_to_bin(s):
    s_bin = ''
    for i in range(len(s)):
        s_bin += format(s[i], '08b') + " "
    return s_bin


def xor_dec(s1, s2):
    result = []

    if len(s1) < len(s2):
        s1_len = len(s1)
        s2_len = len(s2)

        dif = s2_len - s1_len

        s2 = s2[:dif]

    for i in range(len(s2)):
        result.append(s1[i] ^ s2[i])
    return result


def hex_decoding(s):
    result = s.decode("hex")
    return result


def xor_2_strings(s1, key):
    s1_decode = hex_decoding(s1)
    # key_decode = hex_decoding(key)
    print s1_decode

    # xor_strings(s1_decode, key_decode)


def padding(user_message):
    message_return = []

    message_split = [user_message[i:i + 8] for i in range(0, len(user_message), 8)]

    n_items = len(message_split)

    len_of_last_item = len(message_split[n_items - 1])

    if len_of_last_item == 8:
        message_split.append('\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x08')
        return message_split
    else:
        padding_nums_to_add = 8 - len_of_last_item
        last_item = message_split[n_items - 1]
        last_item += struct.pack(">H", padding_nums_to_add)

        for i in range(len(message_split)):
            if i == (n_items - 1):
                message_return.append(last_item)
            else:
                message_return.append(message_split[i])
        return message_return


def ecb_mode(key, message_with_padding):
    result = []
    for i in range(len(message_with_padding)):
        result.append(xor_strings(message_with_padding[i], key))
    print "******* ECB MODE ENCRYPTION *******"
    print result


def ctr_mode(key, message_with_padding, IV):
    pass

def main(key, user_message, IV):
    message_with_padding = padding(user_message)
    print "Plaintext blocks with padding:"
    print message_with_padding

    ecb_encrypted_message = ecb_mode(key, message_with_padding)

    ctr_mode(key, message_with_padding, IV)


if __name__ == '__main__':
    key = ("ABCDEF1234567890".decode("hex"))
    print key
    # user_message = raw_input("Enter your message: ")
    user_message = 'COMP8004COMP8004 Plain'

    IV = 1

    main(key, user_message, IV)
