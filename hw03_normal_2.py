# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
def sort_to_max(origin_list):
	pass
new_list = []
while len(origin_list)>0:
	number = origin_list.pop()
		if len(new_list) == 0 :
			new_list.append(number)
		elif number >= max(new_list):
			new_list.append(number)
		elif number <= min(new_list):
			new_list.insert(0, number)
		else:
		for i in range(len(new_list)):
		if number >= new_list[i] and number <= new_list[i+1]:
			new_list.insert(i+1, number)
		break
	return new_list
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
sorted_list = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(sorted_list)