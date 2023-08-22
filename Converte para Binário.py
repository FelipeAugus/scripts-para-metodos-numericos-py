def multPartDec(Dec):
	Dec = Dec - int(Dec)
	Dec *= 2
	return Dec

def convPBin(num):
	Lint = []
	Ldec = []
	Nint = int(num)
	Ndec = num-Nint
	
	if Nint != 0:
		while Nint != 1 :
			if Nint%2 == 1: Lint.append('1')
			else: Lint.append('0') 
			Nint //= 2
		Lint.append('1')

	if Ndec != 0:
		casas = 0
		Ldec.append('0')
		while Ndec != 0 and casas != 10:
			Ndec = multPartDec(Ndec)
			if int(Ndec) == 1: Ldec.append('1')
			else: Ldec.append('0') 
			casas+=1
	
	print(Lint,',',Ldec)

N = float(input('Num: '))
convPBin(N)
