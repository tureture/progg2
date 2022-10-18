""" Exam tasks for modul 4 for exam 2022-05-30

Exam code:                  Important to fill in this!!!!


"""

# A9
from random import shuffle
def hands_of_cards(n):
	return [hand_of_cards() for _ in range(n)]

def hand_of_cards():
	cards=list(range(1,53))
	shuffle(cards)
	return cards[:5]

# A10
import concurrent.futures as future
def compute_one_pair_ratio(n,n_processes):
	n_hands=n_processes*[n//n_processes]

	with future.ProcessPoolExecutor() as ex:
		all_hands = ex.map(hands_of_cards, n_hands)
	all_hands=list(all_hands)

	with future.ProcessPoolExecutor() as ex:
		all_one_pair = ex.map(number_of_one_pair, all_hands)
	n_one_pair=sum(list(all_one_pair))
	return n_one_pair/n

def number_of_one_pair(lst):
	n_one_pair=0
	for hand in lst:
		vals=[(card-1)%13+1 for card in hand]
		vals.sort()
		valseq=[]
		for i in range(4):
			if vals[i]==vals[i+1]:
				valseq.append(i+1)
		if len(valseq)==1:
			n_one_pair+=1
	return n_one_pair

# B4
def compute_all_ratios(n,n_processes):
	n_hands=n_processes*[n//n_processes]

	with future.ProcessPoolExecutor() as ex:
		all_hands = ex.map(hands_of_cards, n_hands)
	all_hands=list(all_hands)

	with future.ProcessPoolExecutor() as ex:
		result = ex.map(number_of_poker_hands, all_hands)
	result=list(result)
	res=result[0]
	for k in res:
		for i in range(1,n_processes):
			res[k]+=result[i][k]
	for k in res:
		res[k]/=n
	return res

def number_of_poker_hands(lst):
	n_hands=len(lst)
	hands={ 'n_none':0,
			'n_one_pair':0,
			'n_two_pairs':0,
			'n_tripples':0,
			'n_straight':0,
			'n_flush':0,
			'n_full_house':0,
			'n_quadruple':0,
			'n_straight_flush':0,
			'n_royal_flush':0}
	for hand in lst:
		hand.sort()
		vals=[(card-1)%13+1 for card in hand]
		vals.sort()
		valseq=[]
		for i in range(4):
			if vals[i]==vals[i+1]:
				valseq.append(i+1)
		if len(valseq)==1:
			hands['n_one_pair']+=1
		elif len(valseq)==2:
			if valseq[1]-valseq[0]==1:
				hands['n_tripples']+=1
			else:
				hands['n_two_pairs']+=1
		elif len(valseq)==3:
			if valseq==[1,2,3] or valseq==[2,3,4]:
				hands['n_quadruple']+=1
			else:
				hands['n_full_house']+=1
		if isstraight(vals):
			if isflush(hand):
				if vals[0]==1 and vals[1]==10:
					hands['n_royal_flush']+=1
				else:
					hands['n_straight_flush']+=1  
			else:
				hands['n_straight']+=1
		else:
			if isflush(hand):
				hands['n_flush']+=1 
	tot_hands=0
	for k in hands:
		tot_hands+=hands[k]
	hands['n_none']=n_hands-tot_hands
	return hands

def isstraight(vals):
	is_straight=False
	count=0
	for i in range(4):
		if vals[i]==vals[i+1]-1:
			count+=1
	if count==4:
		is_straight=True 
	else:
		if count==3 and vals[0]==1 and vals[1]==10:
			is_straight=True
	return is_straight

def isflush(hand):
	is_flush=False
	if hand[4]<14:
		is_flush=True
	elif hand[0]>13 and hand[4]<27:
		is_flush=True
	elif hand[0]>26 and hand[4]<40:
		is_flush=True
	elif hand[0]>39:
		is_flush=True
	return is_flush

if __name__ == '__main__':
	# A9
	print(hands_of_cards(5))

	# A10
	print(compute_one_pair_ratio(10000,4))

	# Test code to create all possible poker hands (2598960), of which 1098240 are one pair
	# from itertools import combinations
	# def all_hands_of_cards():
	# 	return [list(x) for x in combinations(list(range(1,53)), 5)]
	# print(number_of_one_pair(all_hands_of_cards()))

	# B4
	res=compute_all_ratios(10000,4)

	# present results in terminal
	for k in res: 
		if res[k]>0:
			print(f'{k[2:]} : {res[k]}')

	# present results using matplotlib using a bar plot
	import matplotlib.pyplot as plt
	import matplotlib.colors as pltc # to define colors
	import math #to plot log10 values
	hands=[]
	ratios=[]
	for k in res: 
		if res[k]>0:
			hands.append(k[2:]) #we remove 'n_' to make it look better
			ratios.append(res[k]*100) #here use percentages instead of ratios (both work fine)
	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])
	log10ratios=[math.log10(r) for r in ratios] #log10 of percentages to have "reasonably" visualizable sized bars
	ax.bar(hands,log10ratios,color=pltc.TABLEAU_COLORS) #plot with different colors
	for i, r in enumerate(ratios): #place some text in the plot
		if log10ratios[i]>0:
			ax.text(i-0.25, -0.1, hands[i])
			ax.text(i-0.25, -0.22, str(round(r,2)) + '%')
		else:
			ax.text(i-0.25, 0.17, hands[i])
			ax.text(i-0.25, 0.05, str(round(r,2)) + '%')
	plt.show()

	# Test code to create all possible poker hands (2598960), and calculate how many of each poker hand that occurs, compare with https://en.wikipedia.org/wiki/Poker_probability
	# from itertools import combinations
	# def all_hands_of_cards():
	# 	return [list(x) for x in combinations(list(range(1,53)), 5)]
	# res=number_of_poker_hands(all_hands_of_cards())
	# for k in res: 
	# 	print(f'{k} : {res[k]}')

