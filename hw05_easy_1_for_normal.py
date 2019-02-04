# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# create folders 
import os
def create_dir(dirname):
	try:
		os.mkdir(dirname)
	except Exception:
		print('Something wrong with create ' + dirname)
	
def create_dirs():
	for i in range(1,9):
		create_dir('dir_' + str(i))
	
def remove_dir(dir):
	try:
		os.rmdir(dir)
	except Exception:
		print('Something wrong with remove ' + dir)
	
def remove_dirs():
	for i in range(1,9):
		remove_dir('dir_' + str(i))

def print_dirs():
	for item in os.listdir():
		if os.path.isdir(item):
			print(item)