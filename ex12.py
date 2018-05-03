# ex12.py
# prompting people

age = input("how old are you? ")
height = input("how tall are you? ")
weight = input("how much do you weigh? ")

print(f"so, you're {age} years old, {height} tall, and {weight} heavy.")

print('''\n\n\nDocumentation for input function:\n\n\n
python -m pydoc input
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
''')
