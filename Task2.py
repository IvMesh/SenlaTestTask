def GCD(n1,n2):
	while n1 != 0 and n2 != 0:
		if n1 > n2:
			n1 = n1 % n2
		else:
			n2 = n2 % n1
	return n1 + n2

def LCM(n1,n2):
	multiply = n1 * n2
	while n1 != 0 and n2 != 0:
		if n1 > n2:
			n1 = n1 % n2
		else:
			n2 = n2 % n1
	return multiply // (n1 + n2)

while 1:
	try:
		number1 = int(input("1 число = "))
		number2 = int(input("2 число = "))
		print("НОД = ", GCD(number1,number2))
		print("НОК = ", LCM(number1,number2))
		break
	except ValueError:
		print("При введении числа допущена ошибка! Повторите ввод!")
