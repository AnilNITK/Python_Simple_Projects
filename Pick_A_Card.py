import random
cards=['Hearts','Diamonds','Spades','Clubs']
ranks=[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
def pick_card(cards,rank):
    card=random.choice(cards)
    rank=random.choice(ranks)
    print(f"The {rank} of {card}")
pick_card(cards,ranks)
