input_str = str(input("Введите предложение: "))
input_str = input_str.lower()
searchWord = str(input("Введите искомое слово: "))
print("Искомое слово появляется в предложении ",input_str.count(searchWord.lower())," раз(а)")
