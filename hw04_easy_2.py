# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit_1 = ['apple', 'orrange', 'pearch', 'lemon']
fruit_2 = ['orrange', 'lemon', 'qiwi', 'lame']
fruit = [i for i in fruit_1 if i in fruit_2]
print(fruit)