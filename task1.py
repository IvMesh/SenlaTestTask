def IsPrime(n)
    i = 2
    j = 0
    while(True)
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

number =int(input(number))
if number%2 == 0:
    print("Данное число четное!")
else print("Данное число нечетное!")
IsPrime(number)
