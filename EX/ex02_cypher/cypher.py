"""Hello."""


def encode(message: str, key: int) -> str:
    """
    Encode a message using a Caesar cipher.

    :param message: message to be encoded
    :param key: key for encoding
    :return: encoded message
    """
    encrypt = ""
    for symbol in message:
        if symbol.isalpha():  # i
            num = ord(symbol)  # ord(i)=105
            num += key  # num=105+6=111 197
            if symbol.islower():  # if lower letter
                if num < ord('a'):  # 111<97 False
                    num += 26
                while num > ord('z'):  # 111>122 False
                    num -= 26
            #  a-z 97-122 65-90 A-Z
                encrypt += chr(num)  # encrypt = chr(111) = o
        else:
            encrypt += symbol  # encrypt = i

    return encrypt


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.
