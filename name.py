import random
from time import sleep
import numbError as n
a = input("Введите вашу фамилию имя и отчество через пробел ").lower()
shet_byk = n.intError("Введите колво букв которое\nбудет в имени(макс: 15)",1,15,1)
a = a.split(" ")
glasn = "аеёиоуыэюя"
soglasn = "бвгджзйклмнпрстфхцчшщъь"
shet = 1
if n.intError("На какую букву начинается слово:\n1 - гласная\n2 - согласная") == 1:
	isGlash = False
else:
	isGlash = True
	shet_byk += 1
while shet <= 500:
	if isGlash == False:
		i = 0
	else:
		i = 1
	a_elem = random.choice(a)
	name = []
	while i < shet_byk:
		randNumber = random.randint(1,3)
		if randNumber == 2:
			a_elem = random.choice(a)
		a_elem_simb = random.choice(a_elem)
		if a_elem_simb in soglasn and i % 2 != 0 and a_elem_simb != "ъ" and a_elem_simb != "ь":
			i += 1
			name.append(a_elem_simb)
		if a_elem_simb in glasn and i % 2 == 0 and a_elem_simb != "ы":
			name.append(a_elem_simb)
			i += 1
	name = "".join(name)
	print(name)
	shet += 1
	sleep(1)
	f = open("names.txt","a",encoding = "utf-8")
	f.write(name+"\n")
	f.close()

