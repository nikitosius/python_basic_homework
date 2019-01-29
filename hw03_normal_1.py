# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
	    pass
array = [1,1]
while len(array) < m:
	index_last1, index_last2 = len(array)-2, len(array)-1
	new_fib_number = array[index_last1] + array[index_last2]
	array.append(new_fib_number)
	return array[n:(m+1)]
print(fibonacci(5,10))