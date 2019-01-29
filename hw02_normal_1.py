list_1 = [2, -5, 8, 9, -25, 25, 4]
list_2 = []
print(list_1)
for element in list_1:
	print(type(element**.5))
	if type(element**.5) is float and int(element**.5) == element**.5:
		list_2.append(int(element**.5))
	print(list_2)