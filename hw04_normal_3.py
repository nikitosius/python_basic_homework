# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
import random
a = os.path.join('text.txt')
list_1 = [random.randint(0, 2500) for x in range(2500)]
number = list(map(str,list_1))
result = ''.join(number)
with open(a, mode='w', encoding='UTF-8') as file:
	file.write(result)
with open(a, mode='r', encoding='UTF-8') as file:
	string = file.readlines()
f = list(map(int,list(''.join(string))))
print(result)