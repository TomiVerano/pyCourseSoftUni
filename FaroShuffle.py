
deck_cards = input().split()
shuffle_count = int(input())
for shuffle in range(shuffle_count):
    final_deck = []
    middle_index = len(deck_cards) // 2
    left_deck = deck_cards[0:middle_index]
    right_deck = deck_cards[middle_index:]
    for deck_card_index in range(len(left_deck)):
        final_deck.append(left_deck[deck_card_index])
        final_deck.append(right_deck[deck_card_index])
    deck_cards = final_deck
print(deck_cards)
