"""Secret Garden."""

import base64


class Decoder:
    """Decoder class."""

    def __init__(self, file: str, key: str):
        """
        Decoder constructor.

        :param file: Input file
        :param key: Very secret key
        """
        self._file = file
        self._key = key

    def read_code_from_file(self) -> list:
        """
        Read file lines to a list.

        File comes from class constructor.

        :return: List of file lines
        """
        with open(self._file, encoding='utf-8') as file:
            lines = file.read().splitlines()
        return lines

    @staticmethod
    def decode_from_base64(data: str) -> str:
        """
        Decode base64 string to utf-8 string.

        :param data: Base64 format string
        :return: Utf-8 format string
        """
        return base64.b64decode(data).decode('UTF-8')

    def calculate_cipher_step(self) -> int:
        """
        Calculate cipher step.

        Cipher key comes from constructor.
        Formula is sum of UNICODE value of each letter.
        Example: "Hi" -> 72 + 105 -> 177

        :return: Cipher step as integer
        """
        counter = 0
        for a in self._key:
            for i in a:
                counter = counter + ord(i)
        return counter

    def decode(self) -> list:
        """
        Decode file with key.

        For correct answer you have to convert file lines from base64 to utf-8.

        To decode one line you have to take a UNICODE value of a letter, subtract cipher step and take mod of 255.
        After that you have to convert that number back to a character.
        Example: key = 'test', decoded_data = "+%'"
        '+' -> (43 - 448) % 255 -> 'i' -> ... -> 'ice'

        :return: List of decoded lines
        """
        count = 0
        list2 = []
        string = ""
        list3 = []
        for i in self.read_code_from_file():
            list2.append(self.decode_from_base64(str(i)))

        for num in list2:
            for a in num:
                formula = ((ord(a) - self.calculate_cipher_step()) % 255)
                be = chr(formula)
                string += be
                count += 1
                if count == len(num):
                    list3.append(string)
                    count = 0
                    string = ""
        return list3


class SecretGarden:
    """SecretGarden class."""

    def __init__(self, file: str, key: str):
        """
        SecretGarden constructor.

        :param file: Input file
        :param key: Very secret key
        """
        self._file = file
        self._key = key
        d = Decoder(self._file, self._key)
        self._data = d.decode()

    def decode_messages(self) -> list:
        """
        Use Decoder class to decode messages.

        :return: List of decoded lines
        """
        return self._data

    def find_secret_locations(self) -> list:
        """
        Find all secret locations.

        You have to use decoded messages here. These messages contain a starting coordinate on first line e.g. '1;4'.
        First number shows position on east-west scale and second number shows position on north-south scale.
        Second line is empty.
        Third line contains steps to reach to the secret location e.g. 'NEEWSS'.
        Possible steps are 'N' (north), 'E' (east), 'S' (south) and 'W' (west). Each step moves your position by 1.

        :return: List of tuples with secret location coordinates
        """
        list_list = []
        list2 = []
        for val in self.decode_messages():
            j = val.replace("\n\n", ';')
            list2.append(j)
        for i in list2:
            splited = i.split(";")
            a = int(splited[0])
            b = int(splited[1])
            c = splited[2]
            for letter in c:
                if letter == "N":
                    b += 1
                elif letter == "S":
                    b -= 1
                elif letter == "E":
                    a += 1
                elif letter == "W":
                    a -= 1
            list_list.append((a, b))
        return list_list


if __name__ == '__main__':
    d = Decoder('pr08_example_data.txt', 'Fat Chocobo')
    print(d.read_code_from_file())  # ['KS0uNyktBgZBT08=', ...]
    print(d.read_code_from_file()[0])
    print(d.decode_from_base64('MDsyCgpOTlNXV0U='))  # 0;2\n\nNNSWWE
    print(d.calculate_cipher_step())  # 70 + 97 + 116 + 32 + ... -> 1016
    print(d.decode())  # ['-12;-1\n\nESS', ...]
    sg = SecretGarden('pr08_example_data.txt', 'Fat Chocobo')
    print(sg.decode_messages())  # ['-12;-1\n\nESS', ...]
    print(sg.find_secret_locations())  # [(-11, -3), (20, -13), (1, -3), (-2, -5), (10, 4), (6, -13), (2, -6)]
