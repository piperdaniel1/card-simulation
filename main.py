from card import Deck, Card, Pinochle_Deck, PinochleCard

def calculate_pair_odds():
    my_deck = Deck()
    pairs = 0
    total = 0

    for _ in range(100000):
        cards = []

        for _ in range(3):
            cards.append(my_deck.deal())
        
        if cards[0].rank == cards[1].rank or cards[1].rank == cards[2].rank or cards[0].rank == cards[2].rank:
            pairs += 1

        for card in cards:
            my_deck.add_card(card)
        
        my_deck.shuffle()
        
        total += 1
        print(f"Simulating hand #{total}", end="\r")

    print(f"{pairs} pairs out of {total}, which is {round((pairs / total) * 100, 2)} percent.")

def calculate_run_odds():
    my_deck = Pinochle_Deck()
    my_deck.shuffle()
    runs = 0
    total = 0

    for _ in range(1000000):
        cards = []

        for _ in range(24):
            cards.append(my_deck.deal())
        
        hand = Pinochle_Deck(cards)

        if hand.contains_double_run():
            runs += 1
        
        for card in cards:
            my_deck.add_card(card)
        
        my_deck.shuffle()
        
        total += 1
        print(f"Simulating hand #{total}", end="\r")

    print(f"{runs} runs out of {total}, which is {round((runs / total) * 100, 5)} percent.")

def calculate_double_pinochle_odds():
    my_deck = Pinochle_Deck()
    my_deck.shuffle()
    double_pinochles = 0
    total = 0

    for _ in range(1000000):
        cards = []

        for _ in range(15):
            cards.append(my_deck.deal())
        
        hand = Pinochle_Deck(cards)

        if hand.contains_double_pinochle():
            double_pinochles += 1
        
        for card in cards:
            my_deck.add_card(card)
        
        my_deck.shuffle()
        
        total += 1
        print(f"Simulating hand #{total}", end="\r")

    print(f"{double_pinochles} double pinochles out of {total}, which is {round((double_pinochles / total) * 100, 2)} percent.")
    
if __name__ == "__main__":
    #calculate_pair_odds()
    #calculate_run_odds()
    calculate_double_pinochle_odds()