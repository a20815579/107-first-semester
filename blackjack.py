import random
#產生一副隨機的鋪克牌
def Preprocessing():
	rank = ["ACE","2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING"]
	suit = ["SPADE","HEART","DIAMOND","CLUB"]
	deck = []
	for r in rank:
		for s in suit:
			deck.append(r+"-"+s)
	random.shuffle(deck)
	return deck
#隨機發給玩家和莊家各兩張牌
def Settle_the_Stage(deck):
	player = []
	dealer = []
	for i  in range(2):
		card = random.choice(deck)
		player.append(card)
		deck.remove(card)
		card = random.choice(deck)
		dealer.append(card)
		deck.remove(card)
	return player,dealer
#計算手牌總和，如果有ACE，考慮是否大於21點決定當1還是11
def Compute_the_Total_Value(player,dealer):
	pl_total = 0
	de_total = 0
	ACE_number = 0
	for i in player:
		if i[0].isdigit() == True:
			if i[1].isdigit() == True:
				pl_total += int(i[0:2])
			else:
				pl_total += int(i[0])
		elif i[:3] == "ACE":
			ACE_number += 1
		else:
			pl_total += 10
	if ACE_number >= 1:
		if pl_total + 11 + ACE_number - 1 <= 21:
			pl_total += 11 + ACE_number - 1
		else:
			pl_total += ACE_number
	ACE_number = 0
	for i in dealer:
		if i[0].isdigit() == True:
			if i[1].isdigit() == True:
				de_total += int(i[0:2])
			else:
				de_total += int(i[0])
		elif i[:3] == "ACE":
			ACE_number += 1
		else:
			de_total += 10
	if ACE_number >= 1:
		if de_total + 11 + ACE_number - 1 <= 21:
			de_total += 11 + ACE_number - 1
		else:
			de_total += ACE_number
	return pl_total,de_total
#印出玩家和莊家的點數，根據不同的點數印出不同的句子，並詢問玩家是否要再抽牌，有抽牌的話計算點數，重新迴圈
def Game_Logic(player,dealer,pl_total,de_total):
	print()
	while True:
		if pl_total == 21:
			print("Your current value is Blackjack! (21)")
		elif pl_total < 21:
			print("Your current value is %d" %(pl_total))
		else:
			print("Your current value is Bust! (>21)")
		print("with the hand:",end = " ")
		for i in range(len(player)-1):
			print(player[i],end = ", ")
		print(player[len(player)-1])
		print()
		if pl_total > 21:
			break
		else:
			ans = input("Hit or stay? (Hit = 1, Stay = 0): ")
			if ans == "0":
				print()
				break
			else:
				card = random.choice(deck)
				player.append(card)
				deck.remove(card)
				print("You draw %s" %(card))	
				print()
				pl_total,de_total = Compute_the_Total_Value(player,dealer)
	while True:
		if de_total == 21:
			print("Dealer's current value is Blackjack! (21)")
		elif de_total < 21:
			print("Dealer's current value is %d" %(de_total))
		else:
			print("Dealer's current value is Bust! (>21)")
		print("with the hand:",end = " ")
		for i in range(len(dealer)-1):
			print(dealer[i],end = ", ")
		print(dealer[len(dealer)-1])
		print()
		#莊家點數未達17點繼續抽牌，超過17點則停止
		if de_total < 17:
			card = random.choice(deck)
			dealer.append(card)
			deck.remove(card)
			print("Dealer draws %s" %(card))	
			print()
			pl_total,de_total = Compute_the_Total_Value(player,dealer)
		else:
			break
	return pl_total,de_total
#根據21點遊戲規則判斷贏家
def Determine_the_Winner(pl_total,de_total):
	if (pl_total > 21 and de_total > 21) or (pl_total == de_total):
		print("*** You tied the dealer, nobody wins. ***")
	elif (pl_total > de_total and pl_total <= 21) or (pl_total <= 21 and de_total > 21):
		print("*** You beats the dealer! ***")
	else:
		print("*** Dealer wins! ***")
	print()
#詢問是否重新一局
def play_or_not():
	play_yn = input("Want to play again? (y/n): ")
	if play_yn == "y":
		print()
		print("-"*40)
		play_tf = True
	else:
		play_tf = False
	return play_tf
#遊戲主程式
game = True
while game:
	deck = Preprocessing()
	player,dealer = Settle_the_Stage(deck)
	pl_total,de_total = Compute_the_Total_Value(player,dealer)
	pl_total,de_total = Game_Logic(player,dealer,pl_total,de_total)
	result = Determine_the_Winner(pl_total,de_total)
	game = play_or_not()