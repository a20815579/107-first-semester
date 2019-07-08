#印出遊戲畫面
a = [[" "]*7,[" "]*7,[" "]*7,[" "]*7,[" "]*7,[" "]*7]
c = 0
r = 0
while r <= 5:
	print("+---"*7 + "+")
	print("| " , end = "")
	while c <= 6:
		print(a[r][c] , end = " | ")
		c += 1
	r += 1
	c = 0
	print("")
print("+---"*7 + "+")
print("  0   1   2   3   4   5   6")

player = "x"
h = [5]*7		#每行被疊起的高度
same = [1]*4

while True:
	i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = 1
	#判斷輸入是否可以讓遊戲正確執行
	while True:
		if player == "x":
			c = input("Player X >> ")
		else:
			c = input("Player O >> ")
		if c.isdigit() == False:
			print("Invalid input, try again [0-6].")
		else:
			c = int(c)
			if not 0 <= c <= 6:
				print("Out of range, try again [0-6].")
			elif h[c] == -1:
				print("This column is full. Try another column.")
			else:
				break
	if player == "x":
		a[h[c]][c] = "X"
		player = "o"
	else:
		a[h[c]][c] = "O"
		player = "x"
	#判斷水平相同數(左右兩側)
	while c - i1 >= 0:
		if a[h[c]][c-i1] == a[h[c]][c]:
			same[0] += 1
		else:
			break
		i1 += 1
	while c + i2 <= 6:
		if a[h[c]][c+i2] == a[h[c]][c]:
			same[0] += 1
		else:
			break
		i2 += 1
	#判斷垂直相同數(上下兩側)
	while h[c] - i3 >= 0:
		if a[h[c]-i3][c] == a[h[c]][c]:
			same[1] += 1
		else:
			break
		i3 += 1
	while h[c] + i4 <= 5:
		if a[h[c]+i4][c] == a[h[c]][c]:
			same[1] += 1
		else:
			break
		i4 += 1
	#判斷斜線相同數(兩側)
	while c - i5 >= 0 and h[c] - i5 >= 0:
		if a[h[c]-i5][c-i5] == a[h[c]][c]:
			same[2] += 1
		else:
			break
		i5 += 1
	while c + i6 <= 6 and h[c] + i6 <= 5:
		if a[h[c]+i6][c+i6] == a[h[c]][c]:
			same[2] += 1
		else:
			break
		i6 += 1
	#判斷斜線相同數(兩側)
	while c - i7 >= 0 and h[c] + i7 <= 5:
		if a[h[c]+i7][c-i7] == a[h[c]][c]:
			same[3] += 1
		else:
			break
		i7 += 1
	while c + i8 <= 6 and h[c] - i8 >= 0:
		if a[h[c]-i8][c+i8] == a[h[c]][c]:
			same[3] += 1
		else:
			break
		i8 += 1
	h[c] -= 1
	c1 = 0
	r = 0
	#印出遊戲畫面
	while r <= 5:
		print("+---"*7 + "+")
		print("| " , end = "")
		while c1 <= 6:
			print(a[r][c1] , end = " | ")
			c1 += 1
		r += 1
		c1 = 0
		print("")
	print("+---"*7 + "+")
	print("  0   1   2   3   4   5   6")
	#四個連成一線
	if max(same) >= 4:
		break
	else:
		same = [1]*4
	#每行都滿
	if max(h) == -1:
		print("Draw")
		break
#減去在迴圈中多加的數
h[c] += 1
i1 -= 1
i2 -= 1
i3 -= 1
i4 -= 1
i5 -= 1
i6 -= 1
i7 -= 1
i8 -= 1
i = 0
#水平，垂直，斜線超過四個相同的變小寫
if i1 + i2 >= 3:
	while c - i1 + i <= c + i2:
		a[h[c]][c-i1+i] = a[h[c]][c-i1+i].lower()
		i += 1
i = 0
if i3 + i4 >= 3:
	while h[c] - i3 + i <= h[c] + i4:
		a[h[c]-i3+i][c] = a[h[c]-i3+i][c].lower()
		i += 1
i = 0
if i5 + i6 >= 3:
	while c - i5 + i <= c + i6:
		a[h[c]-i5+i][c-i5+i] = a[h[c]-i5+i][c-i5+i].lower()
		i += 1
i = 0
if i7 + i8 >= 3:
	while c - i7 + i <= c + i8:
		a[h[c]+i7-i][c-i7+i] = a[h[c]+i7-i][c-i7+i].lower()
		i += 1
r = 0
c1 = 0
#印出變小寫的結果和贏家
if max(same) >= 4:
	while r <= 5:
		print("+---"*7 + "+")
		print("| " , end = "")
		while c1 <= 6:
			print(a[r][c1] , end = " | ")
			c1 += 1
		r += 1
		c1 = 0
		print("")
	print("+---"*7 + "+")
	print("  0   1   2   3   4   5   6")
	if player == "x":
		print("Winner: O")
	else:
		print("Winner: X")