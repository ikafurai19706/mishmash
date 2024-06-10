#coding: utf-8
from time import sleep
import usefulThings
from random import randint

reset = "\033[2J\033[0;0H"
symbols = ["♠", "\033[31m♥\033[0m", "\033[31m♦\033[0m", "♣"]
numbers = [" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " J", " Q", " K"]
title_logo = ["""
---------------------------------------
                                     
                                     
                                     
                                     
                                     
                                     
---------------------------------------\
""","""
---------------------------------------
  ┌─────┐┌─────┐┌─┐ ┌─┐┌─────┐┌─────┐
  │ ┌─┐ ││ ┌─┐ ││ │┌┘┌┘│ ┌───┘│ ┌─┐ │
  │ └─┘ ││ │ │ ││ └┘┌┘ │ └──┐ │ └─┘ │
  │ ┌───┘│ │ │ ││ ┌┐└┐ │ ┌──┘ │ ┌┐ ┌┘ 
  │ │    │ └─┘ ││ │└┐└┐│ └───┐│ │└┐└┐
  └─┘    └─────┘└─┘ └─┘└─────┘└─┘ └─┘
---------------------------------------\
""","""
-------------------------
                                     
                                     
                                     
                                     
                                     
                                     
-------------------------\
""","""
-------------------------
  ┌────┐        ┌──┐
  │ ┌┐ │        └┐ │
  │ └┘ └┐        │ │
  │ ┌─┐ │    ┌─┐ │ │
  │ └─┘ │┌─┐ │ └─┘ │┌─┐
  └─────┘└─┘ └─────┘└─┘
-------------------------\
"""]

def cardPrint(sym: int, num: int=0):
    if sym == -1:
        print(f"""\
┌───┐\033[1B\033[5D\
│XXX│\033[1B\033[5D\
│XXX│\033[1B\033[5D\
└───┘\033[3A""",
        end="")
    
    else:
        num = numbers[num]
        sym = symbols[sym]
        print(f"""\
┌───┐\033[1B\033[5D\
│{num} │\033[1B\033[5D\
│ {sym} │\033[1B\033[5D\
└───┘\033[3A""",
        end="")
    
def TitleLogoAnimation(gameType):
    print(reset, end="")
    for i in title_logo[1+gameType*2].split("\n"):
        print(i, flush=True)
        sleep(0.25)
    for i in range(5):
        sleep(0.4)
        print(reset + title_logo[i%2+gameType*2])


class Poker():
    def __init__(self,):
        self.start()

    def start():
        usefulThings.printLbyL(f"Welcome to Poker, {name}!")
        sleep(0.4)
        usefulThings.printLbyL("Which mode do you play?")
        input("(0: Solo, 1: Online): ")
        

class BlackJack():
    def __init__(self,):
        self.deck = [ (i, j) for i in range(4) for j in range(13) ]
        self.dealer_cards: list[tuple[int, int]] = []
        self.player_cards: list[tuple[int, int]] = []
        self.money = 500
        self.round = 0
        self.start()

    def drawCard(self):
        sym, num = self.deck.pop(randint(0, len(self.deck)-1))
        return sym, num

    def updateMoney(self, amount):
        self.money += amount
        print(f"\033[1;1HMoney: ${self.money}")

    def start(self,):
        print(reset)
        self.updateMoney(0)
        sleep(0.3)
        self.game()

    def dealer_draw(self):
        sym, num = self.drawCard()
        self.dealer_cards.append((sym, num))
        return sym,num
    
    def player_draw(self):
        sym, num = self.drawCard()
        self.player_cards.append((sym, num))
        return sym, num

    def game(self,):
        self.round += 1
        print(f"\033[1;30HRound: {self.round}")
        sleep(0.3)
        print("\033[3;2HDealer's hand")
        print("-" * 40 + "\n" * 5 + "-" * 40 + "\n")
        sleep(0.1)
        print(f"{name}'s hand")
        print("-" * 40 + "\n" * 5 + "-" * 40)
        sleep(0.5)
        while True:
            print("\033[5;4H", end="")
            for i in range(2):
                sym, num = self.dealer_draw()
                if i == 0: cardPrint(sym, num)
            cardPrint(-1)
            print("\033[13;4H", end="", flush=True)
            sleep(0.5)
            for i in range(2):
                sym, num = self.player_draw()
                cardPrint(sym, num)
            input()

            


##################################################

print(reset)
while True:
    name = input("Please enter your name (Up to 8 chars): ")
    if len(name) <= 8:
        break
    else:
        print("[Character count is over]",flush=True, end="")
        sleep(1)
        print("\r\033[2K\033[1A\033[2K", end="")

while True:
    gameType = input("Select a game to play(0: POKER, 1: B.J.): ")
    if gameType == "0" or gameType == "1":
        TitleLogoAnimation(int(gameType))
        Poker() if gameType == "0" else BlackJack()
        break
    else:
        print("[Invalid value]",flush=True, end="")
        sleep(1)
        print("\r\033[2K\033[1A\033[2K", end="")
