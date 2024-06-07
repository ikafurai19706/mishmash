#coding: utf-8

symbols = {"spade": "♠", "heart": "\033[31m♥\033[0m", "d": "\033[31m♦\033[0m", "club": "♣"}
numbers = [" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " J", " Q", " K"]

def CardPrint(num, sym):
    print("""\
┌───┐\033[1B\033[5D\
│{} │\033[1B\033[5D\
│ {} │\033[1B\033[5D\
└───┘\033[3A"""
          .format(num, sym), end="")

title_logo = """\
┌─────┐┌─────┐┌─┐ ┌─┐
│ ┌─┐ ││ ┌─┐ ││ │┌┘ │
│ └─┘ ││ │ │ ││ └┘
│ ┌───┘│ │ │ ││ 
│ │    │ └─┘ ││ ┌┐ 
└─┘    └─────┘└─┘
"""
print("\033[2J\033[0;0H"+title_logo)
for i in symbols.values():
    for j in numbers:
        CardPrint(j, i)
    print("\033[4E", end="")