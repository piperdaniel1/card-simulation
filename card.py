import random

class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        return "{} of {}".format(ranks[self.rank - 1], suits[self.suit])
    
    def __gt__(self, other) -> bool:
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit and self.rank > other.rank:
            return True
        else:
            return False
        
    def __lt__(self, other) -> bool:
        if self.suit < other.suit:
            return True
        elif self.suit == other.suit and self.rank < other.rank:
            return True
        else:
            return False
    
    def __eq__(self, other) -> bool:
        if self.suit == other.suit and self.rank == other.rank:
            return True
        else:
            return False
    
    def __ne__(self, other) -> bool:
        if self.suit != other.suit or self.rank != other.rank:
            return True
        else:
            return False
    
    def __le__(self, other) -> bool:
        return self < other or self == other
    
    def __ge__(self, other) -> bool:
        return self > other or self == other

class PinochleCard(Card):
    def __init__(self, suit, rank) -> None:
        super().__init__(suit, rank)
    
    def __str__(self) -> str:
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["9", "Jack", "Queen", "King", "Ten", "Ace"]

        return "{} of {}".format(ranks[self.rank - 1], suits[self.suit])

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    
    # build the deck
    def build(self) -> None:
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()
    
    def sort(self) -> None:
        self.cards.sort()
    
    def add_card(self, card) -> None:
        self.cards.append(card)

    def __len__(self) -> int:
        return len(self.cards)
    
    def __str__(self) -> str:
        deck = ""
        for card in self.cards:
            deck += str(card) + "\n"
        return deck

class Pinochle_Deck(Deck):
    def __init__(self, cards = None):
        if cards is None:
            self.cards = []
            self.build()
        else:
            self.cards = cards
    
    def build(self):
        for suit in range(4):
            for rank in range(0, 12):
                self.cards.append(PinochleCard(suit, rank % 6 + 1))
    
    def contains_run(self):
        self.sort()
        current_suit = self.cards[0].suit
        current_run = 0

        longest_run = 0

        for i in range(len(self.cards) - 1):
            if self.cards[i].rank + 1 == self.cards[i + 1].rank and self.cards[i].suit == self.cards[i + 1].suit and self.cards[i].rank != 1:
                current_run += 1
            elif self.cards[i].suit == self.cards[i + 1].suit:
                continue
            else:
                if current_run > longest_run:
                    longest_run = current_run

                current_run = 0
        
        if current_run > longest_run:
            longest_run = current_run
        
        return longest_run >= 4
    
    def contains_double_run(self):
        self.sort()
        current_run = 0

        longest_run = 0

        for i in range(len(self.cards) - 1):
            if self.cards[i].rank + 1 == self.cards[i + 1].rank and self.cards[i].suit == self.cards[i + 1].suit and self.cards[i].rank != 1:
                current_run += 1
            elif self.cards[i].suit == self.cards[i + 1].suit and self.cards[i].rank != 1:
                current_run += 1
            elif self.cards[i].suit == self.cards[i + 1].suit:
                continue
            else:
                if current_run > longest_run:
                    longest_run = current_run

                current_run = 0
        
        if current_run > longest_run:
            longest_run = current_run
        
        return longest_run >= 9

    def contains_double_pinochle(self):
        self.sort()
        jacks_of_diamonds = 0
        queens_of_spades = 0

        longest_run = 0

        for i in range(len(self.cards)):
            if self.cards[i].rank == 2 and self.cards[i].suit == 2:
                jacks_of_diamonds += 1
            elif self.cards[i].rank == 3 and self.cards[i].suit == 3:
                queens_of_spades += 1
            
        if jacks_of_diamonds == 2 and queens_of_spades == 2:
            return True
        
        return False