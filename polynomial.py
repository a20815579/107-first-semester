p = input("Input the polynominals: ")
#把-變成+-以利後面切割
i = 1
while i < len(p):
	if p[i] == "-" and p[i-1] != "(" :
		p = p[:i] + "+" + p[i:]
		i += 2
	else:
		i += 1
#補上係數1*
i = 0
while i < len(p) - 1:
	if (p[i] == "(" or p[i] == "+" or p[i] == "-") and p[i+1].isalpha() == True:
		p = p[:i+1] + "1*" + p[i+1:]
		i += 3
	else:
		i += 1
#將指數轉換為多個字母,ex:x^2=xx
i = 0
while i < len(p) - 1:
	if p[i] == "^":
		if p[i+2].isdigit() == True:		#次方為兩位數
			e = int(p[i+1:i+3])
			p = p[:i] + p[i-1]*(e-1) + p[i+3:]
			i += e - 1
		else:		#次方為個位數
			e = int(p[i+1])
			p = p[:i] + p[i-1]*(e-1) + p[i+2:]
			i += e - 1
	else:
		i += 1
#轉為串列
p=p.split(")")
p.pop()
p="".join(p)
p=p.split("(")
del p[0]
#用+切割
i=0
while i < len(p):
	p[i] = p[i].split("+")
	i += 1
#用*切割係數和變數
i = 0
while i < len(p):
	j = 0
	while j < len(p[i]):
		p[i][j] = p[i][j].split("*")
		j += 1
	i += 1
#幫常數項的串列以空字串補成兩項
i = 0
while i < len(p):
	j = 0
	while j < len(p[i]):
		if len(p[i][j]) == 1:
			p[i][j].append("")
		j += 1
	i += 1
#運算(係數,變數)
while len(p) > 1:
	result = []
	i = 0
	while i < len(p[0]):
		j = 0
		while j < len(p[1]):
			coefficient = int(p[0][i][0])*int(p[1][j][0])
			variable = p[0][i][1] + p[1][j][1]
			result1 = [coefficient,variable]
			result += [result1]
			j += 1
		i += 1
	del p[:2]
	p.insert(0,result)
p = p[0]
#以.插入不同的變數之間
i = 0
while i < len(p):
	j = 0
	while j < len(p[i][1]) - 1:
		if p[i][1][j] != p[i][1][j+1]:
			p[i][1] = p[i][1][:j+1] + "." + p[i][1][j+1:]
			j += 2
		else:
			j += 1
	i += 1
#以.切割成串列
i = 0
while i < len(p):
	p[i][1] = p[i][1].split(".")
	i += 1
#合併相同變數
i = 0
while i < len(p):
	j = 0
	while j < len(p[i][1]) - 1:
		k = 1
		while j + k < len(p[i][1]): 
			if p[i][1][j][0] == p[i][1][j+k][0]:
				p[i][1][j] = p[i][1][j] + p[i][1][j+k]
				del p[i][1][j+k]
			else:
				k += 1
		j += 1
	i += 1
#把變數以字母順序排序和合併
i = 0
while i < len(p):
	p[i][1].sort()
	p[i][1] = "".join(p[i][1])
	i += 1
#同項合併
i = 0
while i < len(p) - 1:
	j = 1
	while i + j < len(p):
		if p[i][1] == p[i+j][1]:
			p[i][0] = int(p[i][0]) + int(p[i+j][0])
			del p[i+j]
		else:
			j += 1
	i += 1
#換回指數形式
i = 0
while i < len(p):
	j = 0
	while j < len(p[i][1]) - 1:
		k = 1
		e = 1
		while j + k < len(p[i][1]):
			if p[i][1][j] == p[i][1][j+k]:
				e += 1
			else:
				break
			k += 1
		if e > 1:
			p[i][1] = p[i][1][:j+1] + "^" + str(e) + p[i][1][j+e:]
			j += 3
		else:
			j += 1
	i += 1 
#以*合併小項
i = 0
while i < len(p):
	p[i][0] = str(p[i][0])	
	if p[i][1] == "":	#常數
		p[i] = p[i][0]
	else:
		p[i] = "*".join(p[i])
	i += 1
#用+合併結果
p = "+".join(p)
#把+-變成-
i = 0
while i < len(p):
	if p[i:i+2] == "+-":
		p = p[:i] + p[i+1:]
	else:
		i += 1
#去除係數1
i = 0
while i < len(p):
	if p[i:i+2] == "1*":
		p = p[:i] + p[i+2:]
	else:
		i += 1
print("Output Result:",p)