# Poker hands

from collections import Counter



# C S H D
# e.g. hand = [5H,5C,6S,7S,KD]


def rank(card):
	return ranks[card[0]] if len(card)==2 else ranks[card] 


def compare_ranks(rank_list1,rank_list2):
	for r1,r2 in zip(rank_list1,rank_list2):
		if r1 !=r2:
			return r1 < r2
	assert False, "Same Rank"



def is_royal_flush(hand,get_rank=False):
	if get_rank:
		return [1]
	#same suit
	values = ''.join(hand)[::2]
	for char in "TJQKA":
		if char not in values:
			return False
	return is_flush(hand)

def is_straight_flush(hand,get_rank=False):
	if get_rank:
		return highest_cards_sorted(hand,get_rank=True)
	return is_flush(hand) and is_straight(hand) 

def is_four_kind(hand,get_rank=False):
	c= Counter([card[0] for card in hand])
	(ch1, count1), (ch2,count2) = c.most_common(2)

	if get_rank:
		return [rank(ch1)]*4 + [rank(ch2)] 

	return count1 == 4

def is_full_house(hand,get_rank=False):
	c= Counter([card[0] for card in hand])
	(ch1, count1), (ch2,count2) = c.most_common(2)

	if get_rank:
		return [rank(ch1)]*3 + [rank(ch2)]*2 

	return count1 == 3 and count2 == 2


def is_flush(hand,get_rank=False):
	if get_rank:
		return highest_cards_sorted(hand,get_rank=True)

	return all(hand[0][1] == card[1] for card in hand)


def is_straight(hand,get_rank=False):
	if get_rank:
		return highest_cards_sorted(hand,get_rank=True)

	sorted_cards = "23456789AJKQT"
	value_substring = ''.join(sorted(hand))[::2]
	return value_substring in sorted_cards


def is_three_kind(hand,get_rank=False):
	c= Counter([card[0] for card in hand])
	(ch1, count1), (ch2,_), (ch3,_) = c.most_common(3)


	if get_rank:
		return [rank(ch1)]*3 + sorted([rank(ch2),rank(ch3)])

	return count1 == 3


def is_two_pairs(hand,get_rank=False):
	c= Counter([card[0] for card in hand])
	(ch1, count1), (ch2, count2), (ch3,_) = c.most_common(3)

	if get_rank:
		return sorted([rank(ch1)]*2 + [rank(ch2)]*2)+[rank(ch3)] 

	return count1 == count2 == 2


def is_one_pair(hand,get_rank=False):
	c= Counter([card[0] for card in hand])
	pair_val, pair_count = c.most_common(1)[0]

	if get_rank:
		sub_hand = [card for card in hand if card[0] != pair_val ]
		return [rank(pair_val)]*2 + highest_cards_sorted(sub_hand,get_rank=True)

	return pair_count == 2


def split_hands(hands):
	cards = hands.split(' ')
	return cards[:5], cards[5:]


def highest_cards_sorted(hand,get_rank=False):
	if get_rank:
		return sorted([rank(card) for card in hand])
	return True

def does_player_one_win(hands):
	if len(hands) < 28:
		return 0

	hand1, hand2 = split_hands(hands)
	for f in is_valueList:
		if f(hand1) and f(hand2):
			return compare_ranks(f(hand1,get_rank=True),f(hand2,get_rank=True))
		if f(hand1):
			return 1
		if f(hand2):
			return 0	

test_hands = [
	"5H 5C 6S 7S KD 2C 3S 8S 8D TD",
	"5D 8C 9S JS AC 2C 5C 7D 8S QH",
	"2D 9C AS AH AC 3D 6D 7D TD QD",
	"4D 6S 9H QH QC 3D 6D 7H QD QS",
	"2H 2D 4C 4D 4S 3C 3D 3S 9S 9D",
	"5H 8C 6S 7S 9D 2C 3S 8S 8D TD",
]
test_winners = [0,1,0,1,1,1]

is_valueList = [
	is_royal_flush,
	is_straight_flush,
	is_four_kind,
	is_full_house,
	is_flush,
	is_straight,
	is_three_kind,
	is_two_pairs,
	is_one_pair,
	highest_cards_sorted
]

ranks = {
	"2":13,
	"3":12,
	"4":11,
	"5":10,
	"6":9,
	"7":8,
	"8":7,
	"9":6,
	"T":5,
	"J":4,
	"Q":3,
	"K":2,
	"A":1,
}


def main():
	for hands, winner in zip(test_hands,test_winners):
		assert does_player_one_win(hands) == winner

	with open('054.txt') as f:
		hands = f.read().split('\n')
	assert sum(does_player_one_win(hands) for hands in hands) == 376

if __name__ == '__main__':
	main()
