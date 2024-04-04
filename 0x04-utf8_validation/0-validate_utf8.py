#!/usr/bin/python3
"""
    validUTF8
"""


def validUTF8(data):
    """
        determines if a given data set represents
        a valid UTF-8 encoding

        :param data
    """
    if data == []:
        return True

    data_binary = [bin(num)[2:].zfill(8) for num in data]

    for bin_num in data_binary:
        if bin_num.startswith("0"):
            continue
        if not bin_num.startswith("10"):
            return False

    data_decodechars = [int(bin_num, 2) for bin_num in data_binary]
    for code_point in data_decodechars:
        if 0xD800 <= code_point <= 0xDFFF:
            return False
        if code_point > 0x10FFFF:
            return False

    data_decodestr = "".join(chr(char) for char in data_decodechars)
    encoded_data = data_decodestr.encode("utf-8")
    if data_binary != [bin(byte)[2:].zfill(8) for byte in encoded_data]:
        return False

    length_expected = 0
    for i, bin_num in enumerate(data_binary):
        if i == 0:
            if bin_num.startswith("110"):
                length_expected = 2
            elif bin_num.startswith("1110"):
                length_expected = 3
            elif bin_num.startswith("11110"):
                length_expected = 4
            else:
                continue
        elif bin_num.startswith("10"):
            length_expected -= 1
        else:
            return False

    if length_expected > 0:
        return False

    return True
