# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# create folders 
import os
for i in range(9):
	try:
		os.mkdir('dir_' + str(i + 1))
	except FileExistsError:
		print ('Файл уже создан')