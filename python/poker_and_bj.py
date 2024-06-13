#coding: utf-8
from time import sleep
from random import randint
from msvcrt import getch

import usefulThings

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
        end="", flush=True)
    
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
        sleep(0.1)
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
            self.round += 1
            print(f"\033[1;30HRound: {self.round}")
            self.dealer_cards.clear()
            self.player_cards.clear()
            de_sum = 0
            pl_sum = 0
            for i in range(2):
                sym, num = self.dealerDraw()
                print(f"\033[5;{4+5*i}H", end="", flush=True)
                if i == 0: cardPrint(sym, num)
            cardPrint(-1)
            de_sum = self.cardSum(self.dealer_cards)
            print(f"\033[3;2HDealer's hand: {self.dealer_cards[0][1] + 1 if self.dealer_cards[0][1] != 0 else 11} ", end="", flush=True)
            sleep(0.3)
            for i in range(2):
                sym, num = self.playerDraw()
                print(f"\033[13;{4+5*i}H", end="", flush=True)
                cardPrint(sym, num)
            pl_sum = self.cardSum(self.player_cards)
            print("\033[11;2H{}'s hand: {}{} \033[0m".format(
                name,
                ("\033[32m" if pl_sum == 21 else ""),
                ("Natural BlackJack" if pl_sum == 21 else pl_sum)
            ) + " " * 15, end="", flush=True)
            print("\033[24;1H", end="")
            print(self.dealer_cards)
            print(self.player_cards)
            button = ["\033[33m>\033[1m", " ", " "]
            while True:
                print(f"\033[19;2H{button[0]} Hit\033[0m    {button[1]} Stand\033[0m    {button[2]} Double\033[0m\n", flush=True)
                key = ord(getch())
                if key == 13:
                    if button[1] == " ":
                        sym, num = self.playerDraw()
                        print(f"\033[13;{4+5*(len(self.player_cards)-1)}H", end="", flush=True)
                        cardPrint(sym, num)
                        print(f"\033[25;1H{self.player_cards}")
                        pl_sum = self.cardSum(self.player_cards)
                        print("\033[11;2H{}'s hand: {}{} {}\033[0m".format(
                            name,
                            ("\033[31m" if pl_sum > 21 else "\033[32m" if pl_sum == 21 else ""),
                            pl_sum,
                            ("Bust" if pl_sum > 21 else "BlackJack" if pl_sum == 21 else "")
                        ) + " " * 15, end="", flush=True)
                        if pl_sum >= 21:
                            sleep(1)
                            break
                        elif button[2] != " ":
                            break
                    else:
                        break
                elif key == 224:
                    key = ord(getch())
                    if key == 77 and button[2] == " ":
                        button[0], button[1], button[2] = button[2], button[0], button[1]
                    elif key == 75 and button[0] == " ":
                        button[0], button[1], button[2] = button[1], button[2], button[0]
                    continue
            print(f"\033[5;9H", end="", flush=True)
            cardPrint(self.dealer_cards[1][0], self.dealer_cards[1][1])
            if pl_sum < 21:
                if de_sum < 17:
                    sleep(0.5)
                    sym, num = self.dealerDraw()
                    print(f"\033[5;{4+5*(len(self.player_cards))}H", end="", flush=True)
                    cardPrint(sym, num)
                    de_sum = self.cardSum(self.dealer_cards)
                    print("\033[3;2HDealer's hand: {}{} {}\033[0m".format(
                        name,
                        ("\033[31m" if de_sum > 21 else "\033[32m" if de_sum == 21 else ""),
                        de_sum,
                        ("Bust" if de_sum > 21 else "BlackJack" if de_sum == 21 else "")
                    ) + " " * 15, end="", flush=True)
            sleep(0.5)
            print("\033[5;1H\033[2K" + "\n\033[2K" * 3 + "\033[5;1H\033[2K" + "\n\033[2K" * 3
            , end="")




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
