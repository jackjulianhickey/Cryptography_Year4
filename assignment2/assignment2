import struct
import copy


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


def convert_to_dec(s):
    s_ord = []

    for i in range(len(s)):
        s_ord += [ord(s[i])]

    return s_ord


def padding(message):
    # Stores newly created message with padding
    message_return = []

    # splits the message up into 4 bytes as input block is 4 bytes in size
    message_split = [message[i:i + 4] for i in range(0, len(message), 4)]

    # Number of blocks
    n_items = len(message_split)

    # Checks length of the last block
    len_of_last_item = len(message_split[n_items - 1])

    # If the last block is 4 bytes it adds another block to the end that is also 4 bytes
    if len_of_last_item == 4:
        message_split.append('\\x00\\x00\\x00\\x04')
        return message_split
    # Else it just adds the required padding
    else:
        padding_nums_to_add = 4 - len_of_last_item
        last_item = message_split[n_items - 1]
        # Adds the padding required
        last_item += struct.pack(">H", padding_nums_to_add)

        for i in range(len(message_split)):
            if i == (n_items - 1):
                message_return.append(last_item)
            else:
                message_return.append(message_split[i])
        return message_return


def shift_nums(input):
    return input[3:] + input[:3]


def block_cipher(input, key):
    # Get the first 4 bytes of the shift_register
    initilsation_vector = input[:4]
    # xor to the shift register and the key
    result_dec = xor_dec(initilsation_vector, key)
    # Shift the bytes 3 places to the left
    result_shift = shift_nums(result_dec)
    return result_shift


def xor_dec_byte(input_byte, plaintext_byte_dec):
    result = [input_byte ^ plaintext_byte_dec]
    return result


def convert_to_dec_byte(plaintext_byte):
    return ord(plaintext_byte)


def xor_two_bytes(input_byte, plaintext_byte):
    # convert the plaintext to its decimal
    plaintext_byte_dec = convert_to_dec_byte(plaintext_byte)
    # xor the plaintext decimal with the first result from the block cipher
    result_dec = xor_dec_byte(input_byte, plaintext_byte_dec)
    return result_dec


def xor_two_bytes_decryption(input_byte, decryption_byte):
    # xor the encrypted byte with the block cipher byte
    result_dec = xor_dec_byte(input_byte, decryption_byte[0])
    return result_dec


def update_shift_register(shift_register, byte_result):
    # Add the encrypted byte to the end of the shift register
    shift_register.append(byte_result[0])
    # Remove the first element from the shift register
    shift_register = shift_register[1:]
    return shift_register


def encryption(key, user_message, IV):
    # stores the encrypted message
    encrypted_message = []
    # copies IV into new element shift register
    shift_register = IV
    print "******** ADDING PADDING ********\n"
    # Adds padding based on ANSI X9.23 to the message
    message_with_padding = padding(user_message)

    print "******** MESSAGE WITH PADDING ********"
    print message_with_padding, "\n"

    print "******** STARTING CFB ENCRYPTION ********\n"
    # converts the string to key to its decimal format
    key = convert_to_dec(key)
    # Iterate through each char of the message
    for i in range(len(message_with_padding)):
        for x in range((len(message_with_padding[i]))):
            # Perform the block cipher on the shift_register and the key
            result = (block_cipher(shift_register, key))
            # XOR the first character of the plaintext with the first byte of the result of the block cipher
            byte_result = (xor_two_bytes(result[0], message_with_padding[i][x]))
            # Add the encrypted byte to the encrypted message list
            encrypted_message.append(byte_result)
            # Update the shift register with  the encrypted byte
            shift_register = update_shift_register(shift_register, byte_result)
    return encrypted_message


def decrypt_to_char(decrypted_message_no_padding):
    result = []
    for i in range(len(decrypted_message_no_padding)):
        result.append(chr(decrypted_message_no_padding[i][0]))
    return "".join(result)


def remove_padding(decrypted_message):
    result = []
    end_element_num = len(decrypted_message)
    num_of_padding_elements = decrypted_message[end_element_num - 1]

    result = decrypted_message[: len(decrypted_message) - num_of_padding_elements[0]]

    return result


def decryption(key, encrypted_message, IV):
    # Stores the decrypted bytes
    decrypted_message = []
    # copy of the IV
    shift_register = IV

    # Convert the key from string to decimal
    key = convert_to_dec(key)

    print "******** STARTING CFB DECRYPTION PROCESS ********\n"
    # Iterate through the encrypted bytes
    for i in range(len(encrypted_message)):
        #  Perform the block cipher on the shift_register and the key
        result = block_cipher(shift_register, key)
        # XOR the first byte of the encrypted message with the first byte of the result of the block cipher
        byte_result = (xor_two_bytes_decryption(result[0], encrypted_message[i]))
        # Append the resulting byte to the decrypted message list
        decrypted_message.append(byte_result)
        # Update the shift register with the encrypted byte
        shift_register = update_shift_register(shift_register, encrypted_message[i])
    print "******** DECRYPTED MESSAGE IN DECIMALS ********"
    print decrypted_message, "\n"

    print "******** REMOVING PADDING ********\n"
    decrypted_message_no_padding = remove_padding(decrypted_message)
    print "******** PADDING REMOVED ********"
    print decrypted_message_no_padding, "\n"
    return decrypt_to_char(decrypted_message_no_padding)


def main(key, user_message, IV):
    # Shallow copy of the IV
    shift_register = copy.copy(IV)
    print "******** STARTING ENCRYPTION ********\n"
    # Starts the encryption process
    encrypted_message = encryption(key, user_message, shift_register)
    print "******** ENCRYPTED MESSAGE ********"
    print encrypted_message, "\n"

    # Shallow copy of the IV
    shift_register = copy.copy(IV)
    print "******** STARTING DECRYPTION ********\n"
    decrypted_message = decryption(key, encrypted_message, shift_register)
    print "******** DECRYPTED MESSAGE IN CHARACTERS ********"
    print decrypted_message, "\n"


if __name__ == '__main__':
    # Key based on last four digits of my student ID "R00109729"
    key = "9729"
    # user_message to encrypt
    user_message = 'I love long input!'

    # IV based on student ID. Removed first 2 digits as they were 0
    IV = 109729
    IV = map(int, str(IV))

    main(key, user_message, IV)
