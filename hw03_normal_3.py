# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter1(f, lst):
	return [x for x in lst if f(x)]
	
def my_filter2(f,lst):
new_list = []
for val in lst:
	if f(val): new_list.append(val) 
return new_list
	
sample = [1,4,3,65,9,35,3,78,12]
print(my_filter1(lambda x: x % 3 == 0, sample))
print(my_filter2(lambda x: x % 3 == 0, sample))