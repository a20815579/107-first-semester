import random
import time

column = ["a","b","c","d","e","f","g","h","i"]
rule = "Enter the column followed by the row (ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f)." 

def plot_table(player_list):
	#給定玩家遊戲格後，列印出table
	print("     ", end = "")
	for i in range(9):
		print(column[i], end = "   ")
	print()
	for r in range(9):
		print("   " + "+---"*9 + "+")
		print(" " + str(r+1), end = " | ")
		for c in range(9):
			print(player_list[r*9+c], end = " | ")
		print()
	print("   " + "+---"*9 + "+")
	print()

def new_game():
	'''
	開始一個新的遊戲，創造一個玩家遊戲格，並列印出空白遊戲格，且說明規則。
	返回空白遊戲格，地雷數以及命中地雷數。
	'''
	player_list = [" "]*81
	plot_table(player_list)
	print(rule)
	print()
	mines = 10
	correct_mines = 0
	unfold_list = []
	return player_list,mines,correct_mines,unfold_list

def check_valid():
	'''
	讓玩家輸入位置，檢查是否符合格式。
	返回位置(字串)以及其位置
	'''
	while True:
		input_s = input("Enter the cell (%d mines left): " % mines) 	
		if len(input_s) != 2 and len(input_s) != 3 and input_s != "help":
			plot_table(player_list)
			print("Invalid cell.",rule)
			print()
			continue
		#輸入正確
		elif input_s == "help":
			plot_table(player_list)
			print(rule)
			print()
			continue
		elif len(input_s) == 3:
			if input_s[2] != "f" or not input_s[0] in column:
				plot_table(player_list)
				print("Invalid cell.",rule)
				print()
				continue
			if not input_s[1].isdigit() or input_s[1] == "0":
				plot_table(player_list)
				print("Invalid cell.",rule)
				print()
				continue
			#輸入正確
			else:
				input_no = (int(input_s[1]) - 1)*9 + column.index(input_s[0])
				return input_s,input_no
				break
		else:
			if not input_s[0] in column:
				plot_table(player_list)
				print("Invalid cell.",rule)
				print()
				continue
			if not input_s[1].isdigit() or input_s[1] == "0":
				plot_table(player_list)
				print("Invalid cell.",rule)
				print()
				continue
			#輸入正確
			else:
				input_no = (int(input_s[1]) - 1)*9 + column.index(input_s[0])
				return input_s,input_no
				break

def creat_ans(input_no):
	'''
	剩餘80位置隨機抽取10個放入地雷
	並計算個位置的數值
	返回答案list
	'''
	#隨機決定地雷位置
	ans_list = ["X"]*10 + [" "]*70
	random.shuffle(ans_list)
	ans_list.insert(input_no," ")
	#計算附近地雷數
	for i in range(9):
		near_mine = 0
		if i == 0:
			if ans_list[i] != "X":
				if ans_list[i+1] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				if ans_list[i+10] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		elif i == 8:
			if ans_list[i] != "X":
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				if ans_list[i+8] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		else:
			if ans_list[i] != "X":
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i+1] == "X":
					near_mine += 1
				if ans_list[i+8] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				if ans_list[i+10] == "X":
					near_mine += 1
				ans_list[i] = near_mine
	for i in range(9,72):
		near_mine = 0
		if i % 9 == 0:
			if ans_list[i] != "X":
				if ans_list[i-9] == "X":
					near_mine += 1
				if ans_list[i-8] == "X":
					near_mine += 1
				if ans_list[i+1] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				if ans_list[i+10] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		elif i % 9 == 8:
			if ans_list[i] != "X":
				if ans_list[i-9] == "X":
					near_mine += 1
				if ans_list[i-10] == "X":
					near_mine += 1
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i+8] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		else:
			if ans_list[i] != "X":
				if ans_list[i-10] == "X":
					near_mine += 1
				if ans_list[i-9] == "X":
					near_mine += 1
				if ans_list[i-8] == "X":
					near_mine += 1
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i+1] == "X":
					near_mine += 1
				if ans_list[i+8] == "X":
					near_mine += 1
				if ans_list[i+9] == "X":
					near_mine += 1
				if ans_list[i+10] == "X":
					near_mine += 1
				ans_list[i] = near_mine
	for i in range(72,81):
		near_mine = 0
		if i == 72:
			if ans_list[i] != "X":
				if ans_list[i-9] == "X":
					near_mine += 1
				if ans_list[i-8] == "X":
					near_mine += 1
				if ans_list[i+1] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		elif i == 80:
			if ans_list[i] != "X":
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i-10] == "X":
					near_mine += 1
				if ans_list[i-9] == "X":
					near_mine += 1
				ans_list[i] = near_mine
		else:
			if ans_list[i] != "X":
				if ans_list[i-1] == "X":
					near_mine += 1
				if ans_list[i-10] == "X":
					near_mine += 1
				if ans_list[i-9] == "X":
					near_mine += 1
				if ans_list[i-8] == "X":
					near_mine += 1
				if ans_list[i+1] == "X":
					near_mine += 1
				ans_list[i] = near_mine	
	return ans_list


def check_0_list(input_no,player_list,ans_list,unfold_list):
	'''
	輸入位置，玩家遊戲格，答案list
	判斷位置是否為0，且是否九宮格內有0，只要有0的地方周圍都要print出來
	並print出遊戲格
	最後返回玩家遊戲格
	'''
	#選到的格子不是0，只改那個格子
	if ans_list[input_no] != 0:
		player_list[input_no] = ans_list[input_no]
	#是0，顯示周圍的數字，若又有0，繼續檢查附近，已重複的格子不用再加進unfold_list
	else:
		unfold_list.append(input_no)
		i = 0
		while i < len(unfold_list):
			if ans_list[unfold_list[i]] == 0:
				if unfold_list[i] == 0:
					if not unfold_list[i]+1 in unfold_list:
						unfold_list.append(unfold_list[i]+1)
					if not unfold_list[i]+9 in unfold_list:
						unfold_list.append(unfold_list[i]+9)
					if not unfold_list[i]+10 in unfold_list:
						unfold_list.append(unfold_list[i]+10)
				elif unfold_list[i] in range(1,8):
					if not unfold_list[i]-1 in unfold_list:
						unfold_list.append(unfold_list[i]-1)
					if not unfold_list[i]+1 in unfold_list:
						unfold_list.append(unfold_list[i]+1)
					if not unfold_list[i]+8 in unfold_list:
						unfold_list.append(unfold_list[i]+8)
					if not unfold_list[i]+9 in unfold_list:
						unfold_list.append(unfold_list[i]+9)
					if not unfold_list[i]+10 in unfold_list:
						unfold_list.append(unfold_list[i]+10)
				elif unfold_list[i] == 8:
					if not unfold_list[i]-1 in unfold_list:
						unfold_list.append(unfold_list[i]-1)
					if not unfold_list[i]+9 in unfold_list:
						unfold_list.append(unfold_list[i]+9)
					if not unfold_list[i]+8 in unfold_list:
						unfold_list.append(unfold_list[i]+8)
				elif unfold_list[i] in range(9,72):
					if unfold_list[i] % 9 == 0:
						if not unfold_list[i]-9 in unfold_list:
							unfold_list.append(unfold_list[i]-9)
						if not unfold_list[i]-8 in unfold_list:
							unfold_list.append(unfold_list[i]-8)
						if not unfold_list[i]+1 in unfold_list:
							unfold_list.append(unfold_list[i]+1)
						if not unfold_list[i]+9 in unfold_list:
							unfold_list.append(unfold_list[i]+9)
						if not unfold_list[i]+10 in unfold_list:
							unfold_list.append(unfold_list[i]+10)
					elif unfold_list[i] % 9 == 8:
						if not unfold_list[i]-9 in unfold_list:
							unfold_list.append(unfold_list[i]-9)
						if not unfold_list[i]-10 in unfold_list:						
							unfold_list.append(unfold_list[i]-10)
						if not unfold_list[i]-1 in unfold_list:
							unfold_list.append(unfold_list[i]-1)
						if not unfold_list[i]+9 in unfold_list:
							unfold_list.append(unfold_list[i]+9)
						if not unfold_list[i]+8 in unfold_list:
							unfold_list.append(unfold_list[i]+8)
					else:
						if not unfold_list[i]-8 in unfold_list:
							unfold_list.append(unfold_list[i]-8)
						if not unfold_list[i]-9 in unfold_list:
							unfold_list.append(unfold_list[i]-9)
						if not unfold_list[i]-10 in unfold_list:							
							unfold_list.append(unfold_list[i]-10)
						if not unfold_list[i]-1 in unfold_list:
							unfold_list.append(unfold_list[i]-1)
						if not unfold_list[i]+1 in unfold_list:											
							unfold_list.append(unfold_list[i]+1)
						if not unfold_list[i]+9 in unfold_list:
							unfold_list.append(unfold_list[i]+9)
						if not unfold_list[i]+8 in unfold_list:
							unfold_list.append(unfold_list[i]+8)
						if not unfold_list[i]+10 in unfold_list:
							unfold_list.append(unfold_list[i]+10)
				elif unfold_list[i] == 72:
					if not unfold_list[i]-9 in unfold_list:
						unfold_list.append(unfold_list[i]-9)
					if not unfold_list[i]-8 in unfold_list:
						unfold_list.append(unfold_list[i]-8)
					if not unfold_list[i]+1 in unfold_list:
						unfold_list.append(unfold_list[i]+1)
				elif unfold_list[i] in range(73,80):
					if not unfold_list[i]-10 in unfold_list:
						unfold_list.append(unfold_list[i]-10)
					if not unfold_list[i]-9 in unfold_list:						
						unfold_list.append(unfold_list[i]-9)
					if not unfold_list[i]-8 in unfold_list:
						unfold_list.append(unfold_list[i]-8)
					if not unfold_list[i]-1 in unfold_list:
						unfold_list.append(unfold_list[i]-1)
					if not unfold_list[i]+1 in unfold_list:
						unfold_list.append(unfold_list[i]+1)
				elif unfold_list[i] == 80:
					if not unfold_list[i]-9 in unfold_list:
						unfold_list.append(unfold_list[i]-9)
					if not unfold_list[i]-10 in unfold_list:
						unfold_list.append(unfold_list[i]-10)
					if not unfold_list[i]-1 in unfold_list:
						unfold_list.append(unfold_list[i]-1)
			i += 1
		for i in range(len(unfold_list)):
			player_list[unfold_list[i]] = ans_list[unfold_list[i]]		
	return player_list


def put_flag(input_s,input_no,mines,correct_mines):
	'''
	輸入字串，位置，地類剩餘數，命中地雷數
	如果玩家輸入為長度3的字串，進行插旗子，拿旗子，或是判斷不能放旗子
	返回玩家遊戲格，剩餘地雷數，命中地雷數
	'''
	if len(input_s) == 3:
		#拿旗子
		if player_list[input_no] == "F":
			player_list[input_no] = " "
			mines += 1
			if ans_list[input_no] == "X":
				correct_mines -= 1
			plot_table(player_list)
		#插旗子
		elif player_list[input_no] == " ":
			player_list[input_no] = "F"
			mines -= 1
			if ans_list[input_no] == "X":
				correct_mines += 1
			#如果correct_mines=10，不用印player_list，因為後面已經會印ans_list
			if correct_mines != 10:
				plot_table(player_list)
		#該格已有顯示的數字
		else:
			plot_table(player_list)
			print("Cannot put a flag there")
			print()		
	return player_list,mines,correct_mines

def win_or_not(correct_mines):
	'''
	輸入命中地雷數
	如果命中地雷數到達10，則print出玩家花費時間
	返回是否贏得遊戲
	'''
	if correct_mines == 10:
		tEnd = time.time()	#記錄結束時間
		consume = tEnd - tStart
		minute = consume // 60
		second = round(consume % 60)
		print("You win. It took you %d minutes and %d seconds." % (minute,second))
		print()
		win_or_not = True
	else:
		win_or_not = False
	return win_or_not

def play_again(ans_list):
	'''
	輸入答案list
	列印出答案，詢問玩家是否重新一局
	返回是否開新局
	'''
	print("     ", end = "")
	for i in range(9):
		print(column[i], end = "   ")
	print()
	for r in range(9):
		print("   " + "+---"*9 + "+")
		print(" " + str(r+1), end = " | ")
		for c in range(9):
			print(ans_list[r*9+c], end = " | ")
		print()
	print("   " + "+---"*9 + "+")
	print()
	ask = input("Play again? (y/n): ")
	if ask == "y":
		play_again = True
	else:
		play_again = False
	return play_again

def flag_there(input_no):
	'''
	輸入位置，
	判斷是否已擺放旗子，回傳是否
	'''
	if player_list[input_no] == "F":
		plot_table(player_list)
		print("There is a flag there")
		print()
		flag_there = True
	else:
		flag_there = False
	return flag_there

def already_shown(input_no):
	'''
	輸入位置
	回傳是否已出現
	'''
	if type(player_list[input_no]) == int:
		plot_table(player_list)
		print("The cell is already shown")
		print()
		already_shown = True
	else:
		already_shown = False
	return already_shown

#主程式
game = True
while game:
	tStart = time.time() #開始計時
	player_list,mines,correct_mines,unfold_list = new_game() 
	input_s,input_no = check_valid() 
	ans_list = creat_ans(input_no)
	player_list = check_0_list(input_no,player_list,ans_list,unfold_list)
	plot_table(player_list)
	while True: 
		input_s,input_no = check_valid()
		player_list,mines,correct_mines = put_flag(input_s,input_no,mines,correct_mines)		
		if win_or_not(correct_mines):
			game = play_again(ans_list)
			break
		if len(input_s) == 2:
			if flag_there(input_no) or already_shown(input_no):
				continue
			elif ans_list[input_no] == "X":
				print("\n \nGame Over\n")
				game = play_again(ans_list)
				break
			else:
				player_list = check_0_list(input_no,player_list,ans_list,unfold_list)
				plot_table(player_list)