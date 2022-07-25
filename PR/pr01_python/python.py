"""Hello world.lalala."""

name = input("What is your name?")
python_release = 2008
year = int(input("Hello, " + name + "! What year were you born in?"))
a = python_release - year
b = year - python_release
if year <= python_release:
    print("You were " + str(a) + " years old when Python 3.0 was released.")
else:
    print("Python 3 was " + str(b) + " years old when you were born.")
