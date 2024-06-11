from msvcrt import getch
while True:
    print("\033[2J\033[0;0H\033[41m" + (" " * 5 + "\n") * 5)
    print("\033[2J\033[0;0H\033[47m" + (" " * 5 + "\n") * 5)
    print("\033[2J\033[0;0H\033[44m" + (" " * 5 + "\n") * 5)