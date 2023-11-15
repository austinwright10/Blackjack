'''import needed modules'''
import os
import random


''' Project: Twenty One Game:
Course: CS1410
Name: Austin Wright
Due Date: 9/8/23

Description:
Twenty-One Game, or otherwise known as Blackjack

This is skeleton starter code for the Twenty-One Game.

Typical pseudocode for such a game would be:
1. initial deal
2. player's turn
3. If player gets twenty-one, immediate win 
4. dealer's turn
5. check for winner
6. print results '''


def show_card(number, suit, up):
    '''display the actual card'''
    if up:
        return f"""
         --------------
        |  {number}           |
        |              |
        |              |
        |      {suit}       |
        |              |
        |              |
        |           {number}  |
         --------------"""
    else: 
        return f"""
         --------------
        | {"?"}            |
        |              |
        |              |
        |              |
        |              |
        |              |
        |           {"?"}  |
         --------------"""

class Deck():
    '''deck class'''
    def __init__(self):
        '''holds values of each card that composes the deck'''
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self.suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.numeric_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    def random_card(self):
        '''randomly selects a suit alongside the suit value'''
        card_number = random.choice(self.cards)
        random_number = self.numeric_values[card_number]
        random_suit = self.suits_values[random.choice(self.suits)]
        card = Card(card_number, random_number, random_suit)
        return card

class Card:
    '''card class'''
    def __init__(self, card_value, number, suit):
        '''constructor, holds the values of the card'''
        self.card_value = card_value
        self.number = number
        self.suit = suit

    def __str__(self):
        '''returns the card as a string in ASCII format'''
        return show_card(self.card_value, self.suit, True)

class Hand:
    '''hand class'''
    def __init__(self):
        '''constructor, holds the cards that are in each hand'''
        self.cards = []
        self.ace_count = 0
   
    def add(self, card, deck):
        '''adds a card to the hand, if it's an Ace it'll check if it's an 11 or 1'''
        self.cards.append(card)
        if card.number == "A":
            self.ace_count += 1

    def __str__(self):
        '''returns the collection of cards as art'''
        cards = [show_card(card.card_value, card.suit, True) for card in self.cards]
        return " ".join(cards)

    def __len__(self):
        '''returns how many cards are in hand'''
        return len(self.cards)

    def calculate(self):
        '''return the total score of a hand'''
        total = sum(card.number for card in self.cards)
        while total > 21 and self.ace_count > 0:
            total -= 10
            self.ace_count -= 1
        return total

class Dealer:
    '''dealer class'''
    def __init__(self):
        '''class for the dealer: constructor'''
        self.hand = Hand()
        self.deck = Deck()

    def deal(self):
        '''deals a card from the deck'''
        return self.hand.__str__()

    def __str__(self):
        '''returns the dealer's hand and total score as a string'''
        print("Dealer's face-up card:")
        print(self.hand.cards[0], show_card(self.hand.cards[0].card_value, self.hand.cards[0].suit, False))
        print("Dealer's points: ", self.hand.cards[0].number)

class Player:
    '''player class'''
    def __init__(self):
        '''constructor, adds the hand class to the player'''
        self.hand = Hand()
   
    def __str__(self):
        '''#returns the player's hand and total score as a string'''
        print("Your hand: ")
        for card in self.hand.cards:
            print(card)
        print("Player's points: ", self.hand.calculate())

class Game:
    '''game class'''
    def __init__(self):
        '''constructor, runs the player and dealer classes'''
        self.player = Player()
        self.dealer = Dealer()

    def player_turn(self):
        '''implement code for the player's turn'''
        while True:
            if self.player.hand.calculate() == 21:
                print("Player wins!")
                print("Player's points:", self.player.hand.calculate())
                print("Dealer's points:", self.dealer.hand.calculate())
                break
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player.hand.add(self.dealer.deck.random_card(), self.dealer.deck)
                print("Your hand: ", self.player.hand)
                print("Player's points: ", self.player.hand.calculate())
                if self.player.hand.calculate() > 21:
                    print("Bust! You lose.")
                    break
            elif choice.lower() == "stand":
                break

    def dealer_turn(self):
        '''implement code for the dealer's turn'''
        while self.dealer.hand.calculate() < 17:
            self.dealer.hand.add(self.dealer.deck.random_card(), self.dealer.deck)
            if self.dealer.hand.calculate() >= 17:
                break

    def run(self):
        '''implements the pseudocode given in the docstring'''
        while True:
            self.player.hand = Hand()
            self.dealer.hand = Hand()

            for _ in range(2):
                self.player.hand.add(self.dealer.deck.random_card(), self.dealer.deck)
                self.dealer.hand.add(self.dealer.deck.random_card(), self.dealer.deck)

            self.player.__str__()
            self.dealer.__str__()

            self.player_turn()
         
            if self.player.hand.calculate() < 21:
                self.dealer_turn()
                print("Dealer's hand:")
                for card in self.dealer.hand.cards:
                    print(card)
                if self.dealer.hand.calculate() > 21:
                    print("Dealer bust! You win!")
                    print("Dealer's points:", self.dealer.hand.calculate()) 
                    print("Player's points:", self.player.hand.calculate())
                elif self.dealer.hand.calculate() > self.player.hand.calculate():
                    print("Dealer wins!")
                    print("Dealer's points:", self.dealer.hand.calculate())
                    print("Player's points:", self.player.hand.calculate())
                elif self.dealer.hand.calculate() == self.player.hand.calculate():
                    print("It's a tie!")
                    print("Dealer's points:", self.dealer.hand.calculate())
                    print("Player's points:", self.player.hand.calculate())
                else:
                    print("Player wins!")
                    print("Player's points:", self.player.hand.calculate())
                    print("Dealer's points:", self.dealer.hand.calculate())
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again.lower() == "no":
                break


def clear():
    """Clear the console."""
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux, where os.name is 'posix'
    else:
        _ = os.system('clear')

def main():
    '''calling the game to run'''
    game = Game()
    game.run()

if __name__ == '__main__':
    main()