"""Alala."""

from secret_garden import Decoder, SecretGarden

filename = 'pr08_example_data.txt'
key = 'Fat Chocobo'


def test_decode():
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.

    :param length: height of the trunk or leaf
    """
    d = Decoder(filename, key)
    assert d.decode()[0] == '-12;-1\n\nESS'
    assert len(d.decode()) == 7


def test_read_code_from_file():
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.

    :param length: height of the trunk or leaf
    """
    d = Decoder(filename, key)
    assert len(d.read_code_from_file()) == 7
    assert d.read_code_from_file()[5] == 'LDcpLSwGBk9BQVNTT1NPQUFBU0FBQUFB'


def test_decode_from_base64():
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.

    :param length: height of the trunk or leaf
    """
    d = Decoder(filename, key)
    assert d.decode_from_base64('MDsyCgpOTlNXV0U=') == "0;2\n\nNNSWWE"


def test_decode_messages():
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.

    :param length: height of the trunk or leaf
    """
    d = Decoder(filename, key)
    assert d.decode()[0] == '-12;-1\n\nESS'
    assert len(d.decode()) == 7


def test_find_secret_locations():
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.

    :param length: height of the trunk or leaf
    """
    sg = SecretGarden(filename, key)
    assert sg.find_secret_locations()[6] == (2, -6)
