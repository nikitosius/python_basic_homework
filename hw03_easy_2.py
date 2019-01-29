# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky_ticket(ticket_number):
	pass
ticket_number_str = str(ticket_number)
if len(ticket_number_str) != 6:
	return False
summ1 = int(ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])
summ2 = int(ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])
if summ1 == summ2:
	return True
else:
	return False
print(lucky_ticket(123006))