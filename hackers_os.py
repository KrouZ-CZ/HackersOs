from os import system as cmd
from progress.bar import IncrementalBar
from consolemenu import SelectionMenu
import os
import random
import time
import hashlib

cmd('mode con: cols=80 lines=21')
cmd('title HACKERS OS')
if cmd('cd data') != 0:
	cmd('mkdir data')
cmd('cls')

def logo():
	if os.path.exists('data\\key.txt'):
		while True:
			file = open('data\\key.txt', 'r')
			passwd = file.read()
			file.close()
			cmd('cls')
			print('')
			print('              HACKER OS 2.0v')
			print('              Enter password')
			pas = input('              >')
			hashs = hashlib.md5(pas.encode())
			if hashs.hexdigest() == passwd:
				print('              Success!')
				break
	else:
		print('')
		print('              HACKER OS 1.4v')
		print('         come up with a password')
		pas = input('              >')
		hashs = hashlib.md5(pas.encode())
		file = open('data\\key.txt', 'w')
		file.write(hashs.hexdigest())
		file.close()

def select():
	cmd('cls')
	a_list=['Gmail','Vk','Telegram','What`s App','Discord','Minecraft','Steam','Geometry dash','Logs']
	menu = SelectionMenu(a_list,"Select to hack")
	menu.show()
	menu.join()
	selection = menu.selected_option
	return selection
def goto(sel):
	if int(sel) == 0:
		Gmail()
	if int(sel) == 1:
		Vk()
	if int(sel) == 2:
		Tl()
	if int(sel) == 3:
		Wa()
	if int(sel) == 4:
		DI()
	if int(sel) == 5:
		MC()
	if int(sel) == 6:
		St()
	if int(sel) == 7:
		GD()
	if int(sel) == 8:
		log()
def Gmail():
	cmd('cls')
	mail = input('Enter gmail: ')
	time.sleep(0.5)
	print('Gmail to hack --> ' + mail + '@gmail.com')
	time.sleep(0.3)
	print('[+] Connecting to --> gmail.com')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=100, suffix='%(percent)d%%')
	for i in range(random.randint(1, 100)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Find looking for data about gmail', max=50, suffix='%(percent)d%%')
	for i in range(50):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Data detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the password', max=200, suffix='%(percent)d%%')
	for i in range(random.randint(1, 200)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Password decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/Gmail] ' + mail + '@gmail.com' + passgen('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8, 12)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def Vk():
	cmd('cls')
	nu = input('Enter telephon number: ')
	time.sleep(0.5)
	chose = '+7 (' + nu[1:4] + ') ' + nu[4:7] + '-' + nu[7:9] + '-' + nu[9:11]
	print('Number to hack --> ' + chose)
	time.sleep(0.3)
	print('[+] Connecting to --> vk.com')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=120, suffix='%(percent)d%%')
	for i in range(random.randint(1, 120)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search code of vk', max=100, suffix='%(percent)d%%')
	for i in range(random.randint(1, 100)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the code', max=40, suffix='%(percent)d%%')
	for i in range(40):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/VK]   ' + nu + passgen('0123456789', 4, 4)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def Tl():
	cmd('cls')
	nu = input('Enter telephon number: ')
	time.sleep(0.5)
	chose = '+7 (' + nu[1:4] + ') ' + nu[4:7] + '-' + nu[7:9] + '-' + nu[9:11]
	print('Number to hack --> ' + chose)
	time.sleep(0.3)
	print('[+] Connecting to --> telegram')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=250, suffix='%(percent)d%%')
	for i in range(random.randint(1, 250)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Find code of telegram', max=80, suffix='%(percent)d%%')
	for i in range(80):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the code', max=80, suffix='%(percent)d%%')
	for i in range(80):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/Teleg]  ' + nu + passgen('0123456789', 5, 5)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def Wa():
	cmd('cls')
	nu = input('Enter telephon number: ')
	time.sleep(0.5)
	chose = '+7 (' + nu[1:4] + ') ' + nu[4:7] + '-' + nu[7:9] + '-' + nu[9:11]
	print('Number to hack --> ' + chose)
	time.sleep(0.3)
	print('[+] Connecting to --> What`s App')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=20, suffix='%(percent)d%%')
	for i in range(random.randint(1, 20)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search code of WA', max=50, suffix='%(percent)d%%')
	for i in range(random.randint(1, 50)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the code', max=50, suffix='%(percent)d%%')
	for i in range(50):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/WA]  ' + nu + passgen('0123456789', 6, 6)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def DI():
	cmd('cls')
	gmail = input('Enter gmail: ')
	time.sleep(0.5)
	print('Gmail to hack --> ' + gmail + '@gmail.com')
	time.sleep(0.3)
	print('[+] Connecting to --> gmail.com')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=100, suffix='%(percent)d%%')
	for i in range(random.randint(1, 100)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search code of DS', max=20, suffix='%(percent)d%%')
	for i in range(20):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the code', max=40, suffix='%(percent)d%%')
	for i in range(40):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/DS]  ' + gmail + '@gmail.com' + passgen('0123456789', 6, 6)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def MC():
	cmd('cls')
	nick = input('Enter minecraft nick: ')
	time.sleep(0.5)
	print('Nick to hack --> ' + nick)
	time.sleep(0.3)
	print('[+] Connecting to --> minecraft.net')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=150, suffix='%(percent)d%%')
	for i in range(random.randint(1, 150)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search gmail of nick', max=40, suffix='%(percent)d%%')
	for i in range(40):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Gmail detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking gmail', max=100, suffix='%(percent)d%%')
	for i in range(100):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Gmail hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search code on gmail', max=20, suffix='%(percent)d%%')
	for i in range(20):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Decrypting the code', max=40, suffix='%(percent)d%%')
	for i in range(40):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Code decrypted')
	time.sleep(0.5)
	print('')
	c = '[HACKED/MC]  ' + nick + passgen('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8, 12)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def St():
	cmd('cls')
	nick = input('Enter steam nick: ')
	time.sleep(0.5)
	print('Nick to hack --> ' + nick)
	time.sleep(0.3)
	print('[+] Connecting to --> steam.com')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=150, suffix='%(percent)d%%')
	for i in range(random.randint(1, 150)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Search  Steam name of nick', max=100, suffix='%(percent)d%%')
	for i in range(random.randint(1, 100)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Name detected')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking password', max=100, suffix='%(percent)d%%')
	for i in range(random.randint(1, 100)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Password hacked')
	time.sleep(0.5)
	print('')
	c = '[HACKED/Steam] __' + nick + '__' + passgen('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8, 12)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def GD():
	cmd('cls')
	nick = input('Enter geometry dash nick: ')
	a_list=['Moderator', 'Elder moderator', 'Account']
	menu = SelectionMenu(a_list,"Select to hack")
	menu.show()
	menu.join()
	select = menu.selected_option
	time.sleep(0.5)
	print('Nick to hack --> ' + nick)
	time.sleep(0.3)
	print('[+] Connecting to --> geometry dash')
	time.sleep(0.5)
	bar = IncrementalBar('[*] Hacking servers', max=50, suffix='%(percent)d%%')
	for i in range(random.randint(1, 50)):
		bar.next()
		time.sleep(0.1)
	bar.finish()
	time.sleep(0.5)
	print('[+] Servers has hacked')
	time.sleep(0.5)
	if select == 0:
		bar = IncrementalBar('[*] Gives moderator', max=20, suffix='%(percent)d%%')
		for i in range(20):
			bar.next()
			time.sleep(0.1)
		bar.finish()
		time.sleep(0.5)
		print('[+] Moderator gives')
		time.sleep(0.5)
	elif select == 1:
		bar = IncrementalBar('[*] Gives elder moderator', max=20, suffix='%(percent)d%%')
		for i in range(20):
			bar.next()
			time.sleep(0.1)
		bar.finish()
		time.sleep(0.5)
		print('[+] Elder Moderator gives')
		time.sleep(0.5)
	elif select == 2:
		bar = IncrementalBar('[*] Hacking password', max=100, suffix='%(percent)d%%')
		for i in range(random.randint(1, 100)):
			bar.next()
			time.sleep(0.1)
		bar.finish()
		time.sleep(0.5)
		print('[+] Password hacked')
		time.sleep(0.5)
	print('')
	if select == 0:
		c = '[HACKED/GD]  ' + nick + ' moderator gives'
	elif select == 1:
		c = '[HACKED/GD]  ' + nick + ' elder moderator gives'
	elif select == 2:
		c = '[HACKED/GD]  ' + nick + passgen('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8, 12)
	print(c)
	print('')
	cmd('echo ' + c + ' >> data\\log.txt')
	input('To return, press enter')
def log():
	file = open('data\\log.txt', 'r')
	print(file.read())
	file.close()
	input('To return, press enter')
def passgen(chars, min, max):
	length = random.randint(min, max)
	password = ":"
	for i in range(length):
		password += random.choice(chars)
	return password
if __name__ == '__main__':
	logo()
	while True:
		goto(select())
