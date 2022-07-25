"""Meta-trees and meta-dragons."""

from turtle import Turtle
from sys import setrecursionlimit

setrecursionlimit(10000)
lala = 0


def tree(length):
    """
    Write a recursive turtle program to draw a binary tree.

    Start with a trunk 200px tall.
    Each new branch should be 3/5 as big as its trunk.
    Minimum branch size is 5px.
    Move turtle with: t.forward(), t.left(), t.right(), tree()

    :param length: height of the trunk or leaf
    """
    if length == 1:
        i = 1
    elif length == 2:
        i = 1 * 0.35
    elif length == 3:
        i = 1 * 0.35 * 0.35
    else:
        i = 1 * 0.35 * 0.35 * 0.35

    t.forward(200 * i)
    t.left(60)
    t.forward(120 * i)
    if length <= 3:
        t.left(60)
        tree(length + 1)
        t.left(240)
        tree(length + 1)
        t.left(240)
    else:
        t.left(180)
    t.forward(120 * i)
    t.left(60)
    t.forward(120 * i)
    if length <= 3:
        t.left(60)
        tree(length + 1)
        t.left(240)
        tree(length + 1)
        t.left(240)
    else:
        t.left(180)
    t.forward(120 * i)
    t.left(60)
    t.forward(200 * i)
    t.left(180)


stringg = ""
n = -1
trigger = 0
string2 = ""


def apply_dragon_rules(string):
    """
    Write a recursive function that replaces characters in string.

    Like so:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    global stringg
    global n
    global trigger
    n += 1
    string2 = ""

    if trigger == 1:
        n = -1
        string2 = stringg
        stringg = ""
        trigger = 0
        return string2
    if n == len(string):
        trigger += 1
        return apply_dragon_rules(string)
    if string[n] == "a":
        stringg += "aRbFR"
        return apply_dragon_rules(string)
    elif string[n] == "b":
        stringg += "LFaLb"
        return apply_dragon_rules(string)
    else:
        stringg += string[n]
        return apply_dragon_rules(string)


def curve(string, depth):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instructionset at iteration 'depth'
    """
    if depth >= 1:
        depth -= 1
        return curve(apply_dragon_rules(string), depth)
    if depth == 0:
        return string


string_format_curve = ""
string2_format_curve = ""
n_format_curve = 1
lala = 0
naruto = 0


def format_curve(string):
    """
    Use recursions to remove  a  and  b  symbols from the instruction string.

    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    global lala
    global string_format_curve
    global string2_format_curve
    n_format_curve = 1
    if len(string) != 0:
        if string[0] == "F":
            string_format_curve += "F"
            new_string = string[n_format_curve:]
            return format_curve(new_string)
        elif string[0] == "R":
            string_format_curve += "R"
            new_string = string[n_format_curve:]
            return format_curve(new_string)
        elif string[0] == "L":
            string_format_curve += "L"
            new_string = string[n_format_curve:]
            return format_curve(new_string)
        else:
            new_string = string[n_format_curve:]
            return format_curve(new_string)
    else:
        string2_format_curve = string_format_curve
        string_format_curve = ""
        return string2_format_curve


def draw_dragon(string, length):
    """Draw the dragon by reading the string recursively.

    Use t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    if len(string) != 0:
        if string[0] == "R":
            t.right(90)
            t.forward(length)
            return draw_dragon(string[1:], length)
        if string[0] == "L":
            t.left(90)
            t.forward(length)
            return draw_dragon(string[1:], length)
        if string[0] == "F":
            t.right(90)
            t.forward(length)
            return draw_dragon(string[1:], length)


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("#96004f")
    t.speed(0)
    t.pensize(2)
    t.left(90)
    tree(1)
