n = 101
while n > 100:
	n = int(input("Количество чисел(число не должно превышать 100):"))
	if n > 100:
		print("Введенное значение превышает максималоьное значение! Повторите ввод.")
arr = []
for i in range(n):
	arr.append(input("Введите число: "))
print("Последовательность чисел: ",arr)
count = 0
for i in range(n):
	if str(arr[i]) == str(arr[i])[::-1]:
		count = count + 1
print("Количество чисел полиндромов: ",count)
