# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
	    pass
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
number_str = str(number)
fraction_str = number_str.split('.')[1]
fraction_list = list(map(lambda x: int(x), fraction_str))
whole_part_str = number_str.split('.')[0]
whole_part_int = int(whole_part_str)
counter = ndigits
if fraction_list[counter] > 5:
	fraction_list[counter - 1] += 1
	while counter > 0:
		if fraction_list[counter-1] == 10:
			fraction_list[counter-1] = 0
			if counter == 1:
				whole_part_int += 1
			else:
				fraction_list[counter - 2] += 1
			counter -= 1
		final_value = str(whole_part_int) + '.'
		counter2 = 0
		while counter2 < ndigits:
			final_value = final_value + str(fraction_list[counter2])
			counter2 += 1
return float(final_value)
print(my_round(2.1234567, 3))
print(my_round(2.1999967, 1))
print(my_round(2.9999967, 5))