'''Write a program to
i) Shuffle the deck of cards.
ii)To choose one single card from deck.
iii)To create a random sample of size 2 from the available deck of cards'''

import random
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [(suit, rank) for suit in suits for rank in ranks]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)

def choose_a_card(deck):
    return random.choice(deck)

def create_random_sample(deck,size=2):
    return random.sample(deck, size)
63

deck=create_deck()
print("deck of cards are:\n")
for i in list(deck):
    print(i)
shuffle_deck(deck)
print("After shuffling:")
for i in list(deck):
    print(i)
choicecard=choose_a_card(deck)
print("Chosen card is :",choicecard)

samplelist=create_random_sample(deck,size=2)
print("sample of size two is:",samplelist)


