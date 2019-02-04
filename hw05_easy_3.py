# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import sys
filename = sys.argv[0]
with open(filename, 'rb') as f:
	filename = os.path.basename(filename)
	name = filename.split('.py')[0] + '_копия'
	with open(name + '.py', 'wb') as f1:
		f1.write(f.read())