for i in range(2,101):
	fg = 0
	for j in range(2,i):
		if (i % j == 0):
			fg = 1
	if (fg == 0):
		print(i) 