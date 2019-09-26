input_str = str(input("Введите предложение: "))
print("Кол-во слов в предложении:", len(input_str.split()))
print("Предложение с заглавными первыми символами: ",input_str.title())
sortStr = ""
for i in sorted(input_str.split()):
	sortStr = sortStr + " " + i
print("Отсортированное предложение:", sortStr)
