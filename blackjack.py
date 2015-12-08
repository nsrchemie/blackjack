import random

class Card(object):
	"""A Card object that has a rank and suite e.g. 'Ace of Spades'
	
	Parameters
	----------
	Input:
	self-Instance of the object

	Output:
	self.suit-Associated card suite
	self.rank-Associated card value


	"""
	ranks = ['Ace','Jack','2','3','4','5','6','7','8','9','10','Queen','King']
	suites = ['Clubs','Spades','Hearts','Diamonds']
	def __init__(self, suit=0, rank=0,):
			self.suit = suit
			self.rank = rank

	def __str__(self):
		"""A class method to print the card, e.g. ' Ace of Spades'

		Parameters
		----------
		Input:
		self-Instance of the object

		Output:
		Formatted string statement
		"""
		return (self.ranks[self.rank] + " of " + self.suites[self.suit])

	def scoring(self):
		if self.rank == 11 or self.rank == 12 or self.rank == 1:
			return 10
		elif self.rank == 0:
			return 1
		else:
			return self.rank



class Deck(object):
	"""A Deck object that is initialized with a list attribute populated with all 52 unique instances of the Card object

	Parameters
	----------
	Input:
	self-Instance of the object

	Output:
	self.cards-List attribute containing 52 unique instances of a Card object
	"""
	def __init__(self):

		self.cards = []
		for  suit in range(4):
			for rank in range(0,13):
				self.cards.append(Card(suit,rank))

	def __str__(self):
		"""A class method to print out all the cards in the deck

		Parameters
		----------
		Input:
		self-Instance of the Deck object

		Output:
		s-A string of characters containing all the cards"""
		s = ""
		for i in range(len(self.cards)):
			s = s + " " * i + str(self.cards[i]) + "\n"
		return s 


	def shuffle(self):
		"""A function that takes an instance of a Deck object and randomizes the order of its cards

		Parameters
		----------

		Input:
		self-instance of a Deck object

		Output:
		True-Boolean value confirming randomization
		False-Boolean value confirming failure to randomize
		"""
		if self.cards:
			random.shuffle(self.cards)
			return True
		else:
			return False

	def draw_card(self):
		"""A function that removes one Card object from the Deck object

		Parameters
		----------
		Input:
		self-instance of a Deck object

		Output:
		The last Card object in the Deck
		"""
		return self.cards.pop()
		

	def cards_left(self):
		"""Function that returns how many Card objects remain in the Deck object
		Parameters
		----------
		Input:
		self-Instance of a Deck object

		Output:
		An integer corresponding to the length of the self.cards list attribute
		"""
		return len(self.cards)
		
	def bubbleSort(self):
			for i in range(len(self.cards)):
				if self.cards(Card(suit,rank)[i])>self.cards(Card(suit,rank)[i+1]):
					temp = self.cards(Card(suit, rank)[i])
					self.cards(Card(suit, rank))[i+1] = self.cards(Card(suit, rank))[i]
					self.cards(Card(suit, rank))[i+1] = temp

	def Deck_test(self):
		assert type(self.cards) == list
		assert str(self.cards[0]) == 'Ace of Clubs'


class Hand(object):
	"""A Hand object, corresponding to a Player/Dealer

	Parameters
	----------
	Input:
	self-Instance of a Hand object

	Output:
	self.pair-Instance attribute where dealt cards are stored
	self.score-Integer value corresponding to tabulated points from card values
	self.won-Boolean attribute to simply clarify if a player has won or lost

	"""
	def __init__(self, name):
		self.pair = []
		self.name = name
		self.hand_total = []

	def hand_draw(self, deck):
		"""A function that refers to a preinitialized instance of a Deck object and extracts one card that has been dealt from the Deck object using a Deck function

		Parameters
		----------
		Input:
		self-Instance of a Player/hand object
		deck-Instance of a Deck object

		Output:
		self.pair-An update list attribute containing a card pulled via a Deck method
		"""
		self.pair.append(deck.draw_card())


	def __str__(self):
		"""Class method formatting the ability to print the cards found in the Hand object

		Parameters
		----------
		Input:
		self-Instance of a Player/Hand

		Output:
		string-A formatted string of a list of Card objects
		"""
		pairlst = [(str(card)) for card in self.pair]
		return str(pairlst)

	def hand_score(self):
		self.hand_total = []
		if self.name == 'Player':
			for card in self.pair:
				self.hand_total.append(Card.scoring(card))
			for val in self.hand_total:
				if val == 1 and sum(self.hand_total) <= 21:
					val = 10
			if sum(self.hand_total) > 21:
				return 'You overdrew, Dealer wins!'
			else:
				print('Your hand contains {0} and your current total is {1}'.format(str(self), sum(self.hand_total)))
		if self.name == 'Dealer': 
		
			for card in self.pair:
				self.hand_total.append(Card.scoring(card))
			for val in self.hand_total:
				if val == 1 and sum(self.hand_total) <= 21:
					val = 10
			if sum(self.hand_total) > 21:
				return 'Dealer overdrew, you win!'
			

	

class Blackjack:
	"""A class object that when initialized creates a Deck object composed of 52 Card object instances, two Player/Hand object instances (Player and Dealer) """
	def __init__(self):
		pass
	def game(self):
		self.deck = Deck()
		self.deck.shuffle()
		self.player = Hand('Player')
		self.dealer = Hand('Dealer') 
		self.player.hand_draw(self.deck)
		self.player.hand_draw(self.deck)
		self.dealer.hand_draw(self.deck)
		self.dealer.hand_draw(self.deck)
		self.player.hand_score()
		self.dealer.hand_score()
		prompt = input('Your score is currently ' + str(sum(self.player.hand_total)) + '\n' + 'Would you like to Hit or Stay? ')
		if prompt == 'Hit':
			self.player.hand_draw(self.deck)
			self.player.hand_score()
			prompt = input('Your score is currently ' + str(sum(self.player.hand_total)) + '\n' + 'Would you like to Hit or Stay? ')
			if random.randint(0,1) == 1:
				self.dealer.hand_draw(self.deck)
				self.dealer.hand_score()
		if sum(self.player.hand_total) > 21:
			return 'Dealer wins, you overdrew!'
		elif sum(self.dealer.hand_total) > 21:
			return 'You Win!, Dealer overdrew!'
		if prompt == 'Hit':
			self.player.hand_draw(self.deck)
			self.player.hand_score()
			prompt = input('Your score is currently ' + str(sum(self.player.hand_total)) + '\n' + 'Would you like to Hit or Stay? ')
			if random.randint(0,1) == 1:
				self.dealer.hand_draw(self.deck)
				self.dealer.hand_score()
		if sum(self.player.hand_total) > 21:
			return 'Dealer wins, you overdrew!'
		elif sum(self.dealer.hand_total) > 21:
				return 'You Win!, Dealer overdrew!'
		else:
			if sum(self.player.hand_total) > 21:
				return 'Dealer wins, you overdrew!'
			elif sum(self.dealer.hand_total) > 21:
				return 'You Win!, Dealer overdrew!'
			else:
				if sum(self.player.hand_total) > sum(self.dealer.hand_total):
					return 'You Win!'
				elif sum(self.player.hand_total) < sum(self.dealer.hand_total):
					return 'Dealer Wins!'
				elif sum(self.dealer.hand_total) == sum(self.player.hand_total):
					return 'Its a draw!'

		
#blackjack = Blackjack()
			
			
#blackjack = Blackjack()

#		if sum(self.dealer.hand_total) <=21:
#			chance = random.randint(0,1)
#			if chance == 1:
#				self.dealer.hand_draw(self.deck)
		# assert self.dealer is not self.player
		# assert self.dealer.pair is not self.player.pair
		# assert len(self.dealer.pair) == len(self.player.pair) == 2
		# assert self.deck.cards_left() == 48

	# def results(player, dealer):
	# 	"""A function that compares integer values of Hand.score attributes and assigns boolean values for the player depending on their integer total compared to the dealer

	# 	Parameters
	# 	----------
	# 	Input:
	# 	player-Instance of the user as a Hand object
	# 	dealer-Instance of the computer as a Hand object to compete against

	# 	Output:
	# 	self.player.won-A boolean attribute pertaining to the user winning or losing
	# 	string-A number of combined characters signifying whether the user has won or not
	# 	"""
	# 	if self.player.score > self.dealer.score:
	# 		self.player.won = True
	# 		print('You lost!')
	# 	elif self.dealer.score > self.player.score:
	# 		self.player.won = False
	# 		print ('You won!')



	# def play_game(self):	
	# 	""""A function that provides the game logic and prompts after the various objects have been initialized"""

	# 	while not self.player.won:
	# 		if self.player.score > 21:
	# 			self.player.won = False
	# 		else:
	# 			choice = input("Hit or Stay?")
	# 		if choice.lower() == "stay":
	# 				self.player.won = True
	# 		elif choice.lower == "hit":
	# 			self.player.hand_draw(self.deck)
	# 		else:
	# 			print("No! Hit or Stay?")
	# 			continue

	# 	self.results()












		



		# def score(self):
		# """A function that evaluates the cards in the hand, breaks up the cards into list objects and then the ranks are filtered and compared against values to calculate scores

		# Parameters
		# ----------
		# Input:
		# brkenlst = A list of cards in the hand split into separate words for easier parsing and then sliced to get the ranks.

		# e.g. ['King of Spades', 'Ace of Clubs']   -->   [['King'], ['of'], ['spades'], ['Ace'], ['of'], ['Clubs'] ]   -->    [['King'],['Ace']]


		# Output:
		# self.score = An integer value
		# """
		# brkenlst = [[rank] for line in self.pairlst for rank in line.split()]
		# for element in brkenlst[::3]:
		# 	if element == '2':
		# 		self.score += 2
		# 	if element == '3':
		# 		self.score += 3
		# 	if element == '4':
		# 		self.score += 4
		# 	if element == '5':
		# 		self.score += 5
		# 	if element == '6':
		# 		self.score += 6
		# 	if element == '7':
		# 		self.score += 7
		# 	if element == '8':
		# 		self.score += 8
		# 	if element == '9':
		# 		self.score += 9
		# 	if element == '10':
		# 		self.score += 10
		# 	if element == 'Jack':
		# 		self.score += 10
		# 	if element == 'Queen':
		# 		self.score += 10
		# 	if element == 'King':
		# 		self.score += 10
		# 	if element == 'Ace' and self.score <= 10:
		# 		self.score += 10
		# 	if element == 'Ace' and self.score > 10:
		# 		self.score += 1