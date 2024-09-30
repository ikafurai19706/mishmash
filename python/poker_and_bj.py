#coding: utf-8
from time import sleep
from random import randint
from msvcrt import getch

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
        end="", flush=True)
    
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
        print(f"\033[2;31HDeck: {len(self.deck)}")
        return sym, num

    def updateMoney(self, amount):
        self.money += amount
        print(f"\033[1;1HMoney: ${self.money}")

    def draw(self):
        num = randint(0, 12)
        sym = randint(0, 3)
        self.deck[sym][num] += 1
        return num, sym

    def start(self,):
        print(reset)
        self.updateMoney(0)
        sleep(0.3)
        self.game()

    def dealerDraw(self):
        sym, num = self.drawCard()
        self.dealer_cards.append((sym, num))
        return sym,num
    
    def playerDraw(self):
        sym, num = self.drawCard()
        self.player_cards.append((sym, num))
        return sym, num
    
    def cardSum(self, hand):
        sum = 0
        exist_ace = False
        for _, num in hand:
            if num == 0 and not exist_ace:
                sum += 11
                exist_ace = True
            elif num > 9:
                sum += 10
            else:
                sum += num + 1
        if exist_ace and sum > 21:
            sum -= 10
        return sum

    def game(self,):
        self.round += 1
        print(f"\033[1;30HRound: {self.round}")
        sleep(0.3)
        print(f"\033[2;31HDeck: {len(self.deck)}")
        sleep(0.3)
        usefulThings.printLbyL("\033[3;2HDealer's hand", interval=0.05)
        sleep(0.1)
        usefulThings.printLbyL("-" * 40 + "\n" * 5 + "-" * 40 + "\n", interval=0.01)
        sleep(0.3)
        usefulThings.printLbyL(f" {name}'s hand", interval=0.05)
        sleep(0.1)
        usefulThings.printLbyL("-" * 40 + "\n" * 5 + "-" * 40, interval=0.01)
        sleep(0.3)
        while True:
            self.dealer_cards.clear()
            self.player_cards.clear()
            de_sum = 0
            pl_sum = 0
            for i in range(2):
                sym, num = self.dealerDraw()
                print(f"\033[5;{4+5*i}H", end="", flush=True)
                if i == 0: cardPrint(sym, num)
            cardPrint(-1)
            cardPrint(-1)
            




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
