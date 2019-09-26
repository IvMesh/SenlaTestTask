def IsPrime(n):
    i = 2
    j = 0
    while(True):
        if(i*i <=n and j!=1):
            if(n%i == 0):
                j = j+1
            i=i+1
        elif(j==1):
            print("Число составное!")
            return False
        else:
            print("Число простое!")
            return True

def IsOdd(n):
	if(number%2 == 0):
		print("Данное число четное!")
		return False
	else: 
		print("Данное число нечетное!")
		return True
while 1:
	try:	
		number =int(input("Введите число: "))
		IsOdd(number)
		IsPrime(number)
		break
	except ValueError:
		print("При введении числа допущена ошибка! Повторите ввод!")
