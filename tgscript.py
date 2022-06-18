# -*- coding: utf-8
#██╗░░████████╗░██████╗░░██████╗░█████╗░██████╗░██╗██████╗░████████╗░░░██████╗░██╗░░░██╗
#╚██╗░╚══██╔══╝██╔════╝░██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝░░░██╔══██╗╚██╗░██╔╝
#░╚██╗░░░██║░░░██║░░██╗░╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░░░░██████╔╝░╚████╔╝░
#░██╔╝░░░██║░░░██║░░╚██╗░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░░░░██╔═══╝░░░╚██╔╝░░
#██╔╝░░░░██║░░░╚██████╔╝██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░██╗██║░░░░░░░░██║░░░
#╚═╝░░░░░╚═╝░░░░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░

import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os
import colorama
from colorama import Fore, Back, Style
import json, pickle

app = Client('admin', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

colorama.init()
print(Fore.GREEN + Style.BRIGHT + ">>> Руководство по авторизации в скрипте @no_gold")
print("")
print(Fore.BLUE + Style.BRIGHT + ">> Ввод своих данных:")
print(Fore.WHITE + Style.RESET_ALL + "1. Вводите свой номер телефона")
print("2. Ввод Y для подтверждения номера")
print("3. Вводите код который придёт в телеграме")
print("4. Пароль от двухэтапной авторизации (если он есть) ")
print("(Если вы авторизовывались то просто подождите)")
print(Fore.YELLOW + "")

app.start()
app.stop()

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

print(Fore.BLUE + Style.BRIGHT +'''
▀█▀ █▀▀ █▀ █▀▀ █▀█ █ █▀█ ▀█▀   █▀█ █▄█
░█░ █▄█ ▄█ █▄▄ █▀▄ █ █▀▀ ░█░ ▄ █▀▀ ░█░''')
print(Fore.RED + Style.BRIGHT +'''				v.1.3.0
''')

print(Fore.GREEN + Style.BRIGHT + ">>> Информация: ")
print(Fore.YELLOW + Style.BRIGHT +"Напишите в любой телеграм чат команду -help, \nдля просмотра всех команд!")
print("\nАвтор скрипта -\nTelegram: @no_gold\nIG: @im_l.e.g.e.n.d\nВ других соц.сетях нас нет!\n")

print(Fore.GREEN + Style.BRIGHT + ">> Скорость: ")

while True:
		try:
			cool = int(input(f" {Fore.WHITE + Style.RESET_ALL} <*> Введите скорость от 3 до 10 (Норма 8): {Fore.LIGHTBLACK_EX}"))
			if cool > 10:
				print(Fore.RED + Style.BRIGHT + "\n[!] Слишком медленно!")
			else:
				if cool < 3:
					print(Fore.RED + Style.BRIGHT +"\n[!] Слишком быстро!")
				else:
					if cool == str():
						print(Fore.RED + Style.BRIGHT +"\n[!] Вы не ввели скорость!")
					else:
						print(Fore.GREEN + Style.BRIGHT + "Готово! Скрипт запущен.")
						print(Fore.WHITE + Style.RESET_ALL + "Напишите в любой чат телеграмма -help \n(В закрытых чатах команда не работает)")
						break

		except Exception as e:
			try:
				print(Fore.LIGHTRED_EX + f"\nОшибка - {Fore.RED}{e}{Fore.WHITE}\n")
			finally:
				e = None
				del e

global number
number = 0

nobody_id = 1064093359
version = '1.3.0'

banana = '\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️📒📒📒📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️📒📒📒📒⬜️⬜️ \n⬜️⬛️📒📒📒📒📒⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️📒📒📒📒⬜️⬜️ \n⬜️⬛️📒📒📒📒📒⬜️⬜️⬜️ \n⬜️⬜️⬜️📒📒📒⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️📒📒📒📒⬜️⬜️ \n⬜️⬛️📒📒📒📒📒⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️📒📒📒📒⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️📒📒📒📒⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️📒📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒📒⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️📒⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🚪🚪🚪⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🚪⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️ \n⬜️⬜️⬜️⬜️🟨🟨🟨🟨⬜️⬜️ \n⬜️⬛️🟨🟨🟨🟨🟨⬜️⬜️⬜️ \n⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️ \n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\n'

@app.on_message(filters.command('banana', prefixes='.') & filters.me)
async def valentine(app, message):
	global number
	try:
		txt = banana.split('\n\n')
		e = True
		try:
			etime = int(message.text.split('.banana', maxsplit=1)[1])
		except Exception as e:
			try:
				print(f" {Fore.YELLOW} Ошибка - {e}")
				await message.edit('<b>Вы не ввели число!\nПример:</b> <code>.banana 0</code>')
			finally:
				e = None
				del e

		else:
			for i in txt:
				time = etime
				if e == True:
					e = False
				elif time > 10:
					try:
						await message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
						await asyncio.sleep(0.5)
						await message.delete()
					except:
						pass

				else:
					try:
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
					except:
						pass

			else:
				number = number + 1
	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
		finally:
			e = None
			del e

prelove = '\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️❤️❤️❤️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️☁️❤️☁️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️❤️❤️❤️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️☁️❤️☁️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️❤️❤️❤️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️☁️☁️☁️❤️☁️☁️\n☁️☁️☁️❤️☁️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️☁️☁️❤️☁️☁️❤️☁️\n☁️❤️☁️☁️☁️☁️☁️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️☁️❤️☁️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️☁️☁️☁️❤️❤️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️☁️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️❤️❤️☁️❤️❤️☁️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️❤️❤️❤️❤️❤️❤️❤️☁️\n☁️☁️❤️❤️❤️❤️❤️☁️☁️\n☁️☁️☁️❤️❤️❤️☁️☁️☁️\n☁️☁️☁️☁️❤️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n'

@app.on_message(filters.command('prelove', prefixes='.') & filters.me)
async def valentine(app, message):
	global number
	try:
		try:
			txt = prelove.split('\n\n')
			e = True
			etime = int(message.text.split('.prelove ', maxsplit=1)[1])
		except Exception as e:
			try:
				print(f" {Fore.YELLOW} Ошибка - {e}")
				await message.edit('<b>Вы забыли указать скорость!\n Пример:</b> <code>.prelove 5</code>')
			finally:
				e = None
				del e

		else:
			for i in txt:
				time = etime
				if e == True:
					e = False
				elif time > 10:
					try:
						await message.edit('<b>Error: Нельзя ставить больше 10с!</b>')
						await asyncio.sleep(0.5)
						await message.delete()
					except:
						pass

				else:
					try:
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(time)
						await message.edit(f"{i}")
						await asyncio.sleep(4)
					except:
						pass

			else:
				number = number + 1

	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
		finally:
			e = None
			del e

@app.on_message(filters.command("gifspam", prefixes=".") & filters.me)
def sendgif(app, message):
	global number
	number = number + 1
	for _ in range(int(message.command[1])):
		sleep(0.01)
		app.send_document(message.chat.id, "https://tenor.com/view/spam-toon-toonio-%D1%82%D1%83%D0%BD%D0%B8%D0%BE-pomidorkin-gif-24712213")

@app.on_message(filters.command("dead", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = textded.split("\n")
	e = True
	etime = int(msg.text.split('.dead ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'❤️{i} ❤️')
				sleep(time/cool)
				msg.edit(f'🧡 {i} 🧡')
				sleep(time/cool)
				msg.edit(f'💛 {i} 💛')
				sleep(time/cool)
				msg.edit(f'💚 {i} 💚')
				sleep(time/cool)
				msg.edit(f'💙 {i} 💙')
				sleep(time/cool)
				msg.edit(f'💜 {i} 💜')
				sleep(time/cool)
				msg.edit(f'🖤 {i} 🖤')
				sleep(time/cool)
				msg.edit(f'🤍 {i} 🤍')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

textded = '''
<b> Я дед инсайд </b>
<b> Мне 9 лет </b>
<b> И я хочу в Психокидс </b>
'''

@app.on_message(filters.command("space", prefixes=".") & filters.me)
async def valentine(app, msg):
	await msg.edit(f'''
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡''')
	sleep(0.5)
	await msg.edit(f'''
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ ''')
	sleep(0.5)
	await msg.edit(f'''
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ ''')
	sleep(0.5)
	await msg.edit(f'''
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ ''')
	sleep(0.5)
	await msg.edit(f'''
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * ''')
	sleep(0.5)
	await msg.edit(f'''
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ ''')
	sleep(0.5)
	await msg.edit(f'''
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* ''')
	sleep(0.5)
	await msg.edit(f'''
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.''')
	sleep(0.5)
	await msg.edit(f'''
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡''')
	sleep(5)
	await msg.edit(f'''
		🍃 author: @no_gold''')
	sleep(5)
	await msg.delete()
	global number
	number = number + 1



@app.on_message(filters.command("heart2", prefixes=".") & filters.me)
async def valentine(app, msg):
	heart2 = 0
	while heart2 <= 1:
		await msg.edit(f'''
			❤''')
		sleep(0.5)
		await msg.edit(f'''
			🧡''')
		sleep(0.5)
		await msg.edit(f'''
			💛''')
		sleep(0.5)
		await msg.edit(f'''
			💚''')
		sleep(0.5)
		await msg.edit(f'''
			💙''')
		sleep(0.5)
		await msg.edit(f'''
			💜''')
		sleep(0.5)
		await msg.edit(f'''
			🤎''')
		sleep(0.5)
		await msg.edit(f'''
			🖤''')
		sleep(0.5)
		await msg.edit(f'''
			🤍''')
		sleep(0.5)
		await msg.edit(f'''
			💖''')
		sleep(0.5)
		await msg.edit(f'''
			💗''')
		sleep(0.5)
		await msg.edit(f'''
			💘''')
		sleep(0.5)
		await msg.edit(f'''
			💝''')
		sleep(0.5)
		heart2 += 1
	if heart2 >= 2:
		sleep(5)
		await msg.edit(f'''
			🍃 author: @no_gold''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1

@app.on_message(filters.command("zaika", prefixes=".") & filters.me)
async def valentine(app, msg):
	zaika = 0
	zaika2 = 0
	while zaika < 100:
		await msg.edit(f'''
			💖 Поиск зайки... {zaika}%''')
		zaika += 1
	if zaika >= 100:
		await msg.edit(f'''
			✅ Зайка успешно найдена!''')
		sleep(1)
		while zaika2 < 100:
			await msg.edit(f'''
				🤔 Подбираю слова что-бы описать тебя... {zaika2}%''')
			zaika2 += 1
		if zaika2 >= 100:
			await msg.edit(f'''
				❤ Ты самый лучший человек которого я видел!''')
			sleep(5)
			await msg.edit(f'''
				🍃 author: @no_gold''')
			sleep(5)
			await msg.delete()
	global number
	number = number + 1

@app.on_message(filters.command("penis", prefixes=".") & filters.me)
async def valentine(app, msg):
	penis = 0
	penis2 = random.randint(1, 20)

	await msg.edit(f'''
		☑ Увеличение пениса запущено.''')
	sleep(1)
	await msg.edit(f'''
		☑ Увеличение пениса запущено..''')
	sleep(1)
	await msg.edit(f'''
		☑ Увеличение пениса запущено...''')
	sleep(1)

	while penis < 100:
		await msg.edit(f'''
			📈 Увеличение пениса завершено на {penis}%''')
		penis += 1
	if penis >= 100:
		await msg.edit(f'''
			✅ Ваш пенис увеличен на {penis2} см!''')
		sleep(5)
		await msg.edit(f'''
			🍃 author: @no_gold''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1

@app.on_message(filters.command("vzlom", prefixes=".") & filters.me)
async def valentine(app, msg):
	vzlom = 0

	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся.''')
	sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся..''')
	sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся...''')
	sleep(1)

	while vzlom < 100:
		await msg.edit(f'''
			❗ Происходит взлом аккаунта... {vzlom}%''')
		vzlom += 1
	if vzlom >= 100:
		await msg.edit(f'''
			✅ Взлом акканута успешно завершен!''')
		sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных.''')
		sleep(0.5)
		await msg.edit(f'''
			📱 Передача данных в базу данных..''')
		sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных...''')
		sleep(0.5)
		await msg.edit(f'''
			✅ Аккаунт успешно взломан!''')
		sleep(0.5)
		await msg.edit(f'''
			🍃 author: @no_gold''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1

@app.on_message(filters.command("vzlomip", prefixes=".") & filters.me)
async def valentine(app, msg):
	vzlomip = 0

	await msg.edit(f'''
		💾 Поиск айпи начался.''')
	sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался..''')
	sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался...''')
	sleep(1)

	while vzlomip < 100:
		await msg.edit(f'''
			❗ Происходит поиск IP... {vzlomip}%''')
		vzlomip += 1
	if vzlomip >= 100:
		await msg.edit(f'''
			✅ IP-адрес успешно найдён!''')
		sleep(5)
		await msg.edit(f'''
			🍃 author: @no_gold''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1

@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def valentine(client, message):
	global number
	number = number + 1
	text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
	await message.edit(str(text))
	await asyncio.sleep(2)
	kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпекса</b>"
	await message.edit(str(text2))
	await asyncio.sleep(3)
	text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
	await message.edit(str(text3))
	await asyncio.sleep(5)
	drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
			   f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
			   f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
			   f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
	drug = random.choice(drugsss)
	await message.edit(drug)
	await asyncio.sleep(5)

@app.on_message(filters.command("mum", prefixes=".") & filters.me)
async def mum(client, message):
	global number
	number = number + 1
	mamka = [f'<b>❌ Мамаша не найдена</b>',f'<b> ✅ МАМАША НАЙДЕНА</b>' ]
	text = "<b>🔍 Поиск твоей мамки начался...</b>"
	await message.edit(str(text))
	await asyncio.sleep(3.0)
	text2 = "<b>🔍 Ищем твою мамашу на Авито... </b>"
	await message.edit(str(text2))
	await asyncio.sleep(1)
	text3 = random.choice(mamka)
	await message.edit(str(text3))
	await asyncio.sleep(3.0)
	text4 = "<b>🔍 Поиск твоей мамаши на свалке... </b>"
	await message.edit(str(text4))
	await asyncio.sleep(3.0)
	text5 = random.choice(mamka)
	await message.edit(str(text5))
	await asyncio.sleep(5.0)

@app.on_message(filters.command("xuy", prefixes=".") & filters.me)
async def valentine(app, message):
	await message.edit(f'''<b>🍆🍆
🍆🍆🍆
  🍆🍆🍆
	🍆🍆🍆
	 🍆🍆🍆
	   🍆🍆🍆
		🍆🍆🍆
		 🍆🍆🍆
		  🍆🍆🍆
		  🍆🍆🍆
	  🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
	🍆🍆        🍆🍆</b>''')


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def valentine(_, msg):
	global number
	number = number + 1
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = ""
	typing_symbol = "█"
	while (tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05)

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

textded1 = '''
<b>спокойной ночи зайка 💚</b>
<b>спокойной ночи солнышко 💛</b>
<b>спокойной ночи котёнок ❤</b>️
<b>спокойной ночи цветочек 💙</b>
<b>спокойной ночи ангелочек 💜</b>
<b>спокойной ночи принцесса 💓</b>
<b>спокойной ночи красотка 💕</b>
<b>спокойной ночи милашка 💖</b>
<b>спокойной ночи симпатяжка 💗</b>
<b>спокойной ночи бусинка 💘</b>
<b>❤я❤</b>️
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''


@app.on_message(filters.command("compli", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = comp.split("\n")
	e = True
	etime = int(msg.text.split('.compli ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command("compliment", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = comp1.split("\n")
	e = True
	etime = int(msg.text.split('.compliment ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = textded1.split("\n")
	e = True
	etime = int(msg.text.split('.night ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}'
					)
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1


textded2 = '''
<b>Доброе утро зайка 💚</b>
<b>Доброе утро солнышко 💛</b>
<b>Доброе утро котёнок ❤</b>️
<b>Доброе утро цветочек 💙</b>
<b>Доброе утро ангелочек 💜</b>
<b>Доброе утро принцесса 💓</b>
<b>Доброе утро красотка 💕</b>
<b>Доброе утро милашка 💖</b>
<b>Доброе утро симпатяжка 💗</b>
<b>Доброе утро бусинка 💘</b>
<b>❤я❤</b>️
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

@app.on_message(filters.command("day", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = textded2.split("\n")
	e = True
	etime = int(msg.text.split('.day ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}'
					)
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command("dr", prefixes=".") & filters.me)
def valentine(app, msg):
	msg.edit(f'С днём рождения! Желаю тебе...')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	👑 чтобы вся жизнь была полна радости
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	☀️ счастья
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🏋️‍♂️ здоровья
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🌈 улыбок
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	💚 любви
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🔥 приятных сюрпризов
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🥇 Высоких достижений
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🍃 Душевной гармонии
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🌹 Процветания
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	📈 Карьерного роста
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🤝 Хороших друзей
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	💪 Больше силы, чувств, смелости
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🎲 Везения, мира, добра
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🌃 Чтобы сбывались даже самые необычные желания
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	🎇 И чтобы каждое начатое дело заканчивалось успешно!
	''')

	global number
	number = number + 1

@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'
	
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	number = number + 1
	app.send_message(message.chat.id,f'<b>Ты гуль?</b>')
	sleep(2)
	app.send_message(message.chat.id,f'<i>Я тоже</i>')
	sleep(5)
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number
	number = number + 1

	if not spams:
		msg.edit(f'''
			**Error: Что-то пошло не так...\nИспользование: .spam <кол-во спама> <слово>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

@app.on_message(filters.command("help", prefixes="-") & filters.me)
def valentine(app, message):
	message.delete()
	app.send_message(message.chat.id,"""
📙<b> Команды:</b> \n<b> - https://teletype.in/@pr0n1x/commands-tgscriptss</b> \n

💎 <b>Приобрести PREMIUM анимацию: </b>\n <b>- https://telegra.ph/vip-tgscriptss-03-26</b> \n
		""", disable_web_page_preview=True)

@app.on_message(filters.command("mems", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_message(msg.chat.id, f'''
	✨ Меню голосовых мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".сукаблядьнахуй"
	 2) Команда: ".блядьуходиотсюда"
	 3) Команда: ".татышоахуэл"
	 4) Команда: ".блядьнахуй"
	 5) Команда: ".щясзарежу"
	 6) Команда: ".гдетыблядь"
	 7) Команда: ".даунобосаный"
	 8) Команда: ".ктокуда"
	 9) Команда: ".уменяестьплан"
	 10) Команда: ".ятрахнутебя"

	
	(Все команды нужно писать без ковычек)
	Автор скрипта: @no_gold
		''')
	global number
	number = number + 1

@app.on_message(filters.command("сукаблядьнахуй", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/syka-blyad-nahyi.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("блядьуходиотсюда", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/blyat-vixodi-otsyda.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("татышоахуэл", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/ta-ti-sho-oxyel.mp3")

@app.on_message(filters.command("блядьнахуй", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/nahui-blyat.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("щясзарежу", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/schas-zareju.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("гдетыблядь", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems/gde-tyi.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("даунобосаный", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems//daun-obosannyii-mat-tvoyu-v-kanavu-kidal.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("ктокуда", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems//kto-kuda-a-ya-po-delam.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("уменяестьплан", prefixes=".") & filters.me)
def sykatest(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems//u-menya-est-takoi-plan.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("ятрахнутебя", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "mems//ya-traxny-tebya.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("gachi", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_message(msg.chat.id, f'''
	💪 Меню голосовых **GACHY** мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".300"
	 2) Команда: ".woo"
	 3) Команда: ".fuckyou"
	 4) Команда: ".dungeonmaster"
	 5) Команда: ".spank"
	 6) Команда: ".iamsorry"
	 7) Команда: ".ass"
	 8) Команда: ".boynextdoor"
	 9) Команда: ".letsgo"
	
	(Все команды нужно писать без ковычек)
	Автор скрипта: @no_gold
	''')
	global number
	number = number + 1

@app.on_message(filters.command("300", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/fisting-is-300-.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("woo", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/woo.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("fuckyou", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/fuck-you1.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("dungeonmaster", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/dungeon-master.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("spank", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/spank.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("iamsorry", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/oh-shit-iam-sorry.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("ass", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/stick-your-finger-in-my-ass.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("boynextdoor", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/boy-next-door.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("letsgo", prefixes=".") & filters.me)
def gachi(app, msg):
	msg.delete()
	app.send_voice(msg.chat.id, "gachi/come-on-lets-go.mp3")
	global number
	number = number + 1

@app.on_message(filters.command("video", prefixes=".") & filters.me)
def video(app, msg):
	msg.delete()
	app.send_message(msg.chat.id, f'''
	🎞 Меню видео-мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".диско"
	 2) Команда: ".ебаныйврот"
	 3) Команда: ".фортилипабаджи"
	 4) Команда: ".мамескажи"
	 5) Команда: ".мнепоебать"
	 6) Команда: ".сасать"
	 7) Команда: ".чтоэтотакое"
	 8) Команда: ".твояматьш"
	 9) Команда: ".япопулярный"
	 10) Команда: ".тыпиздабол"
	 11) Команда: ".хватитдрочить"
	
	(Все команды нужно писать без ковычек)
	Автор скрипта: @no_gold
	''')
	global number
	number = number + 1

@app.on_message(filters.command("диско", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/discko.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("ебаныйврот", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/ebaniy-v-rot.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("фортилипабаджи", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/fortnite-ili-pubg.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("мамескажи", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/mame-ckaji.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("мнепоебать", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/mne-poebat.MP4")
	global number
	number = number + 1

@app.on_message(filters.command("сасать", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/sasatb.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("чтоэтотакое", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/sho-eto-takoe.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("твояматьш", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/tvoya-matb-sh.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("япопулярный", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/ya-popylarniy.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("тыпиздабол", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/syda-po-formyle.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("хватитдрочить", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_video(msg.chat.id, "video/xvatit-drochit.mp4")
	global number
	number = number + 1

@app.on_message(filters.command("gifs", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_message(msg.chat.id, f'''
	✨ Меню gif мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".понимания"
	 2) Команда: ".клоун"
	 3) Команда: ".ктопинганул"
	 4) Команда: ".ладно"
	 5) Команда: ".nosex"
	 6) Команда: ".переделывай"
	 7) Команда: ".пизда"
	 8) Команда: ".пошёлнахуй"
	 9) Команда: ".спокойнойночи"
	 10) Команда: ".хуйстобой"
	 11) Команда: ".сверхукринж"
	 12) Команда: ".разговор"
	 13) Команда: ".всемпохуй"

	
	(Все команды нужно писать без ковычек)
	Автор скрипта: @no_gold
		''')
	global number
	number = number + 1

@app.on_message(filters.command("всемпохуй", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/vsem-poxui.gif")
	global number
	number = number + 1

@app.on_message(filters.command("разговор", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/razgovor.gif")
	global number
	number = number + 1

@app.on_message(filters.command("понимания", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/100ponimania-0osyjdenia.gif")
	global number
	number = number + 1

@app.on_message(filters.command("клоун", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/kloyn.gif")
	global number
	number = number + 1

@app.on_message(filters.command("ктопинганул", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/kto-pinganyl.gif")
	global number
	number = number + 1

@app.on_message(filters.command("ладно", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/ladno.gif")
	global number
	number = number + 1

@app.on_message(filters.command("nosex", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/no-sex.gif")
	global number
	number = number + 1

@app.on_message(filters.command("переделывай", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/peredelivai.gif")
	global number
	number = number + 1

@app.on_message(filters.command("пизда", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/pizda.gif")
	global number
	number = number + 1

@app.on_message(filters.command("пошёлнахуй", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/poshel-naxui.gif")
	global number
	number = number + 1

@app.on_message(filters.command("спокойнойночи", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/spokoinoi-nochi.gif")
	global number
	number = number + 1

@app.on_message(filters.command("хуйстобой", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/xui-s-toboi.gif")
	global number
	number = number + 1

@app.on_message(filters.command("сверхукринж", prefixes=".") & filters.me)
def mems(app, msg):
	msg.delete()
	app.send_animation(msg.chat.id, "gifs/sverxy-kringe.gif")
	global number
	number = number + 1

@app.on_message(filters.command("bank", prefixes=".") & filters.me)
def betaloves(_, msg):
	bank = 0
	bank1 = random.randint(1, 2500)

	msg.edit(f'''
	Идёт взлом банковской карты.''')
	sleep(0.7)
	msg.edit(f'''
	Идёт взлом банковской карты..''')
	sleep(0.7)
	msg.edit(f'''
	Идёт взлом банковской карты...''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных.''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных..''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных...''')
	sleep(0.7)
	while bank <= 99:
		bank += 1
		msg.edit(f'''
		взлом завершён на {bank}%''')
	if bank >= 99:
		msg.edit(f'''
		Взлом банковской карты успешно завершён!\nСо счёта снято {bank1} руб.''')
		
	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("profile", prefixes=".") & filters.me)
def help(app, message):
	global number
	number = number + 1

	if message.from_user.id in {nobody_id}:
		app.send_message(message.chat.id, f"""
			💾<b> Профиль\n\n</b> <b>Пользователь:</b><code> {message.from_user.first_name}</code>\n<b> Статус: </b> <code>Admin @no_gold</code>\n\n<b> Префикс: </b> <code>{prefix}</code>\n<b> Chat_ID: </b><code> {message.chat.id}</code>\n<b> User_ID: </b><code> {message.from_user.id}</code>\n<b> Версия: </b><code> {version}</code>\n<b> Анимаций по старту:</b> <code>{number}</code>\n </b>""")
	else:
		app.send_message(message.chat.id, f"""
			💾<b> Профиль\n\n</b> <b>Пользователь:</b><code> {message.from_user.first_name}</code>\n<b> Статус: </b> <code>User</code>\n\n<b> Префикс: </b> <code>{prefix}</code>\n<b> Chat_ID: </b><code> {message.chat.id}</code>\n<b> User_ID: </b><code> {message.from_user.id}</code>\n<b> Версия: </b><code> {version}</code>\n<b> Анимаций по старту:</b> <code>{number}</code>\n </b>""")


		app.send_message(message.chat.id, f'''
			🍃 author: @no_gold''')
		sleep(3)
		msg.delete()

@app.on_message(filters.command("maslo", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"<b>я</b>")  # red
		sleep(time)
		msg.edit(f"<b>я люблю</b>")  # orange
		sleep(time)
		msg.edit(f"<b>я люблю когда</b>")  # orange
		sleep(time)
		msg.edit(f"<b>я люблю когда волосатые</b>")  # red
		sleep(time)
		msg.edit(f"<b>я люблю когда волосатые мужики</b>")  # orange
		sleep(time)
		msg.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  # red
		sleep(time)
		msg.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  # orange
		sleep(5)
		global number
		number = number + 1

@app.on_message(filters.command("football", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")  # red
		sleep(2)
		msg.edit(f"<b>⏳ Подготовка к игре.</b>")  # orange
		sleep(2)
		msg.edit(f"<b>⌛ Подготовка к игре..</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⏳ Подготовка к игре...</b>")  # red
		sleep(time)
		msg.edit(f"<b>⚽ Удар.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⚽ Удар..</b>")  # red
		sleep(time)
		msg.edit(f"<b>⚽ Удар...</b>")  # orange
		sleep(time)
		msg.edit(random.choice(foot))
		sleep(5)
		global number
		number = number + 1

foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]

@app.on_message(filters.command("kill", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
		sleep(3)
		msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
		sleep(2)
		msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
		sleep(time)
		msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
		sleep(time)
		msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск..</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск...</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск..</b>")
		sleep(time)
		msg.edit(f"<b>👀 Поиск...</b>")
		sleep(time)
		msg.edit(random.choice(kill))
		sleep(5)
		global number
		number = number + 1

kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]



@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = jopa.split("\n")
	e = True
	etime = int(msg.text.split('.jopa ', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command("love", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = love.split("\n")
	e = True
	etime = int(msg.text.split('.love', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(_, msg):
	txt = zxc.split("\n")
	e = True
	etime = int(msg.text.split('.zxc', maxsplit=1)[1])
	for i in txt:
		time = etime
		if e == True:
			e = False
		elif time > 10:
			try:
				msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
				sleep(0.5)
				msg.delete()
			except:
				pass
		else:
			try:
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
				msg.edit(f'{i}')
				sleep(time/cool)
			except:
				pass
	global number
	number = number + 1

@app.on_message(filters.command('ziga', prefixes='.') & filters.me)
async def betaloves(app, message):
	try:
		hearts = [
		 '🧡', '💛', '💚', '💙', '💜']
		try:
			mode = int(message.text.split('.ziga', maxsplit=1)[1])
			if mode > 2:
				await message.edit('<b> У команды всего 2 режима!</b>')
			if mode == 2:
				time = 0.6
				for i in range(1):
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍\n🤍{random.choice(hearts)}🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍{random.choice(hearts)}{random.choice(hearts)}{random.choice(hearts)}🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit(f"\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍{random.choice(hearts)}🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(2)

			if mode == 1:
				time = 0.6
				for i in range(1):
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🧡🧡🧡🧡🤍🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🤍🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🤍🤍🧡🤍🤍🤍🤍\n🤍🧡🤍🤍🧡🤍🤍🧡🤍\n🤍🧡🧡🤍🧡🧡🧡🧡🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💛💛💛💛🤍💛💛🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍🤍🤍🤍💛🤍🤍💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛🤍🤍💛🤍🤍🤍🤍\n🤍💛🤍🤍💛🤍🤍💛🤍\n🤍💛💛🤍💛💛💛💛🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💚💚💚💚🤍💚💚🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍🤍🤍🤍💚🤍🤍💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚🤍🤍💚🤍🤍🤍🤍\n🤍💚🤍🤍💚🤍🤍💚🤍\n🤍💚💚🤍💚💚💚💚🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💙💙💙💙🤍💙💙🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍🤍🤍🤍💙🤍🤍💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙🤍🤍💙🤍🤍🤍🤍\n🤍💙🤍🤍💙🤍🤍💙🤍\n🤍💙💙🤍💙💙💙💙🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍💜💜💜💜🤍💜💜🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍🤍🤍🤍💜🤍🤍💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜🤍🤍💜🤍🤍🤍🤍\n🤍💜🤍🤍💜🤍🤍💜🤍\n🤍💜💜🤍💜💜💜💜🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍❤️❤️❤️❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍❤️❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
					await asyncio.sleep(time)
					await message.edit('\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')

		except Exception as e:
			try:
				print(f" {Fore.YELLOW} Ошибка - {e}")
				await message.edit('<b>Вы не указали режим .ziga!\nПример:</b><code> .ziga 1</code>')
			finally:
				e = None
				del e

	except FloodWait as e:
		try:
			await asyncio.sleep(e.x)
		finally:
			e = None
			del e

@app.on_message(filters.command('nick', '.') & filters.me)
async def ment(app, message):
	try:
		count = ''.join(message.command[1])
		string = ' '.join(message.command[2:])
		if count == '1':
			if 'сменить' in message.text:
				string = string.replace('сменить', ' ')
				with open('chars.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)
				else:
					await app.update_profile(first_name=string, last_name='', bio='')
					await message.edit('<b>Генерирую шрифт...</b>')
					await asyncio.sleep(2)
					await message.edit('<b>Отправка...</b>')
					await asyncio.sleep(0.7)
					await message.edit(f"<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>")

			else:
				with open('chars.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)

				await message.edit('<b>Генерирую шрифт...</b>')
				await asyncio.sleep(2)
				await message.edit('<b>Отправка...</b>')
				await asyncio.sleep(0.7)
				await message.edit(f"<b>Ваш никнэйм готов!</b>\n<code>{string}</code>")
		if count == '2':
			if 'сменить' in message.text:
				string = string.replace('сменить', ' ')
				with open('chars1.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)
				else:
					await app.update_profile(first_name=string, last_name='', bio='')
					await message.edit('<b>Генерирую шрифт...</b>')
					await asyncio.sleep(2)
					await message.edit('<b>Отправка...</b>')
					await asyncio.sleep(0.7)
					await message.edit(f"<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>")

			else:
				with open('chars1.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)

				await message.edit('<b>Генерирую шрифт...</b>')
				await asyncio.sleep(2)
				await message.edit('<b>Отправка...</b>')
				await asyncio.sleep(0.7)
				await message.edit(f"<b>Ваш никнэйм готов!</b>\n<code>{string}</code>")
		if count == '3':
			if 'сменить' in message.text:
				string = string.replace('сменить', ' ')
				with open('chars2.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)
				else:
					await app.update_profile(first_name=string, last_name='', bio='')
					await message.edit('<b>Генерирую шрифт...</b>')
					await asyncio.sleep(2)
					await message.edit('<b>Отправка...</b>')
					await asyncio.sleep(0.7)
					await message.edit(f"<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>")

			else:
				with open('chars2.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)

				await message.edit('<b>Генерирую шрифт...</b>')
				await asyncio.sleep(2)
				await message.edit('<b>Отправка...</b>')
				await asyncio.sleep(0.7)
				await message.edit(f"<b>Ваш никнэйм готов!</b>\n<code>{string}</code>")
		if count == '4':
			if 'сменить' in message.text:
				string = string.replace('сменить', ' ')
				with open('chars3.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)
				else:
					await app.update_profile(first_name=string, last_name='', bio='')
					await message.edit('<b>Генерирую шрифт...</b>')
					await asyncio.sleep(2)
					await message.edit('<b>Отправка...</b>')
					await asyncio.sleep(0.7)
					await message.edit(f"<b>Ваш никнэйм готов!\nА так же применён!</b> <code>{string}</code>")

			else:
				with open('chars3.json', 'r') as (file):
					chars = json.load(file)
				for normal, font_char in chars.items():
					string = string.replace(normal, font_char)

				await message.edit('<b>Генерирую шрифт...</b>')
				await asyncio.sleep(2)
				await message.edit('<b>Отправка...</b>')
				await asyncio.sleep(0.7)
				await message.edit(f"<b>Ваш никнэйм готов!</b>\n<code>{string}</code>")
	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
			await message.edit('Инструкция:\n1 - 𝔸\n2 - 𝕬\n3 - 𝓐\n4 - Ⓐ\nПример:<code>.nick 3 text</code>')
		finally:
			e = None
			del e

unoo = '\n⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇\n'

@app.on_message(filters.command('uno', prefixes='.') & filters.me)
async def betaloves(_, msg):
	current = ''
	for chunk in unoo.splitlines():
		current += f"{chunk}\n"
		if not chunk.strip():
			pass
		else:
			await msg.edit(current)
			await asyncio.sleep(0.6)
	else:
		pass

piz = '\n█████████████████████████\n█────█───█────█────█────█\n█─██─██─████──███──█─██─█\n█────██─███──███──██────█\n█─█████─██──███──███─██─█\n█─████───█────█────█─██─█\n█████████████████████████\n'

@app.on_message(filters.command('pizza', prefixes='.') & filters.me)
async def betaloves(_, msg):
	current = ''
	for chunk in piz.splitlines():
		current += f"{chunk}\n"
		if not chunk.strip():
			pass
		else:
			await msg.edit(current)
			await asyncio.sleep(0.6)
	else:
		pass

pika = '\n░█▀▀▄░░░░░░░░░░░▄▀▀█\n░█░░░▀▄░▄▄▄▄▄░▄▀░░░█\n░░▀▄░░░▀░░░░░▀░░░▄▀\n░░░░▌░▄▄░░░▄▄░▐▀▀\n░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█\n░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█\n▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█\n█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀\n░▀▄░░▀░░▀▀▀░░▀░░░▄█▀\n░░░█░░░░░░░░░░░▄▀▄░▀▄\n░░░█░░░░░░░░░▄▀█░░█░░█\n░░░█░░░░░░░░░░░█▄█░░▄▀\n░░░█░░░░░░░░░░░████▀\n░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀\n'

@app.on_message(filters.command('pikachu', prefixes='.') & filters.me)
async def betaloves(_, msg):
	current = ''
	for chunk in pika.splitlines():
		current += f"{chunk}\n"
		if not chunk.strip():
			pass
		else:
			await msg.edit(current)
			await asyncio.sleep(0.6)
	else:
		pass

spanch = '\n╲┏━┳━━━━━━━━┓╲╲\n╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n╲┃◯┃╭╮╰╯┏━━━┳╯╲\n╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n'

@app.on_message(filters.command('gubka', prefixes='.') & filters.me)
async def betaloves(_, msg):
	current = ''
	for chunk in list(spanch):
		current += chunk
		if not chunk.strip():
			pass
		else:
			await msg.edit(current)
			await asyncio.sleep(0.4)
	else:
		pass

@app.on_message(filters.command('spamstick', prefixes='.') & filters.me)
async def spam(app, message):
	global number
	number = number + 1
	try:
		stick_id = str(message.text.split()[2])
		for _ in range(int(message.command[1])):
			await asyncio.sleep(0.01)
			await app.send_sticker(message.chat.id, stick_id)

	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
			await message.edit('<b>Вы не ввели ID стикера!!\nПример:</b><code>.spamstick 5 CAACAgIAAxkBAAEEEDZiI8ZlrkTWVAVlsaJ1yfd63euS2AACMgwAAgqBoEs52ePcv8NaIiME</code> (ID стикера можно узнать здесь: @idstickerbot)')
		finally:
			e = None
			del e

@app.on_message(filters.command('vip', prefixes='.') & filters.me)
async def ment(app, message):
	await message.edit('❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️')
	sleep(1)
	await message.edit('❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️')
	sleep(1)
	await message.edit('❇️❇️❇️❇️❇️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️❇️❇️❇️❇️❇️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️✴️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️✴️❇️✴️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️❇️❇️✴️\n❇️✴️❇️❇️❇️✴️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️✴️❇️❇️❇️✴️❇️\n✴️❇️❇️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️❇️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️❇️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️❇️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️❇️\n❇️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️❇️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️❇️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️❇️❇️✴️')
	sleep(1)
	await message.edit('✴️❇️✴️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️❇️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n❇️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️✴️❇️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️❇️❇️❇️❇️❇️✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑❇️❇️❇️👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑❇️👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑💍👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑🟠👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️👑👑👑👑👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑🟠🟠🟠👑✴️\n✴️👑👑👑👑👑✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('✴️✴️✴️✴️✴️✴️✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️🟠🟠🟠🟠🟠✴️\n✴️✴️✴️✴️✴️✴️✴️')
	sleep(1)
	await message.edit('🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠\n🟠🟠🟠🟠🟠')
	sleep(1)
	await message.edit('🟠🟠🟠\n🟠🟠🟠\n🟠🟠🟠')
	sleep(1)
	await message.edit('🟠')
	sleep(3)

@app.on_message(filters.command('prefix', prefixes='.') & filters.me)
async def prefix(_, message):
	global prefix
	try:
		prefix = str(message.text.split()[1])
		prefix = prefix
		await message.edit('<b>Префикс установлен!</b>')
	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
			await message.edit('<b>Вы забыли указать префикс\nПример:</b><code>.prefix TGScripts</code>')
		finally:
			e = None
			del e


prefix = 'Отсутствует'

@app.on_message(filters.command('tea', prefixes='.') & filters.me)
async def betaloves(app, message):
	global number
	try:
		try:
			teatext = str(message.text.split()[1])
			tea = f"\n─▄▀─▄▀\n──▀──▀\n█▀▀▀▀▀█▄\n█░░░░░█─█\n▀▄▄▄▄▄▀▀\n\n{teatext}\n"
			time = 0.6
			current = ''
			for chunk in list(tea):
				current += chunk
				if not chunk.strip():
					pass
				else:
					await message.edit(current)
					await asyncio.sleep(0.01)
			else:
				sleep(5)
				number = number + 1

		except FloodWait as e:
			try:
				sleep(e.x)
			finally:
				e = None
				del e

	finally:
		pass

@app.on_message(filters.command('spamreaction', prefixes='.') & filters.me)
async def spam(app, message):
	global number
	number = number + 1
	try:
		score = int(message.text.split()[1])
		reaction = str(message.text.split()[2])
		h = await app.get_history(chat_id=(message.chat.id), limit=score)
		for x in h:
			x = x.message_id
			await app.send_reaction(message_id=x, chat_id=(message.chat.id), emoji=reaction)

	except Exception as e:
		try:
			print(f" {Fore.YELLOW} Ошибка - {e}")
			await message.edit('<b>Вы не ввели реакцию или количество повторов!\nПример:</b> <code>.spamreaction 10 🔥</code>')
		finally:
			e = None
			del e

@app.on_message(filters.command("like", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f'''      
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
		sleep(5)
		global number
		number = number + 1

@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f'''
🟥''')  # red
		sleep(0.001)
		msg.edit(f'''
🟥🟥''')  # red
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
		sleep(0.001)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
		sleep(1)
		msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
		sleep(1)
		msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
		sleep(1)
		msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
		sleep(4)
		global number
		number = number + 1

@app.on_message(filters.command("loves", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')  # red
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨✨✨✨✨''')  # red
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️✨✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨❤️❤️✨❤️❤️✨✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨✨❤️❤️❤️❤️❤️✨✨
✨✨✨❤️❤️❤️✨✨✨
✨✨✨✨❤️✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💚💚✨💚💚✨✨
✨💚💚💚💚💚💚💚✨
✨💚💚💚💚💚💚💚✨
✨✨💚💚💚💚💚✨✨
✨✨✨💚💚💚✨✨✨
✨✨✨✨💚✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💙💙✨💙💙✨✨
✨💙💙💙💙💙💙💙✨
✨💙💙💙💙💙💙💙✨
✨✨💙💙💙💙💙✨✨
✨✨✨💙💙💙✨✨✨
✨✨✨✨💙✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💜💜✨💜💜✨✨
✨💜💜💜💜💜💜💜✨
✨💜💜💜💜💜💜💜✨
✨✨💜💜💜💜💜✨✨
✨✨✨💜💜💜✨✨✨
✨✨✨✨💜✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🤍🤍✨🤍🤍✨✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨✨🤍🤍🤍🤍🤍✨✨
✨✨✨🤍🤍🤍✨✨✨
✨✨✨✨🤍✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🖤🖤✨🖤🖤✨✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨✨🖤🖤🖤🖤🖤✨✨
✨✨✨🖤🖤🖤✨✨✨
✨✨✨✨🖤✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💛💛✨💛💛✨✨
✨💛💛💛💛💛💛💛✨
✨💛💛💛💛💛💛💛✨
✨✨💛💛💛💛💛✨✨
✨✨✨💛💛💛✨✨✨
✨✨✨✨💛✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(time)
		msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🧡🧡✨🧡🧡✨✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨✨🧡🧡🧡🧡🧡✨✨
✨✨✨🧡🧡🧡✨✨✨
✨✨✨✨🧡✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
		sleep(3)
		global number
		number = number + 1

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
		sleep(time)
		msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
		sleep(1)
		global number
		number = number + 1

@app.on_message(filters.command("showdown", prefixes=".") & filters.me)
def valentine(app, msg):
	msg.edit(f"<b>Начало через: 13s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 12s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 11s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 10s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 9s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 8s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 7s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 6s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 5s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 4s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 3s</b>")  # orange
	sleep(0.6)
	msg.edit(f"<b>Начало через: 2s</b>")  # red
	sleep(0.6)
	msg.edit(f"<b>Начало через: 1s</b>")  # orange
	sleep(0.2)
	msg.edit(f"<b>Бу, блять! Ха-ха</b>") 
	sleep(1.2)
	msg.edit(f"<b>Просыпайтесь нахуй (Let's go!)</b>")  # orange
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Похоронный марш гулей, на часах последний тик</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Моя тати — Бравл Шелли, я несу ей дробовик</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Ваши головы — мишени, я снесу их в один миг</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Никаких резких движений — ваш хилбар на один хит</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Динамайк трипл килл, ха, нервы на пределе</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Voice в моих ушах — я позабыл все дни недели</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Как на лезвии ножа и шквал патрон, летят шрапнели</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Psychokilla — весь мой шарм, вся эта мапа поредели</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>Эй, погоди, мои парни на Стокгольме</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Мой showdown 1x1, и мои демоны все в форме</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Если я зайду к вам в лобби — оно станет вам могилой</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Если ты зайдешь — мне похуй, я не стартану и выйду, а-ха</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>По приказу Генерала Гавса!</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>— Бро, тут вообще сложная ситуация, все границы позакрывали нахуй. Ваще пиздец полный. Ща просто едем ближе ко Львову, но во Львове тоже пиздец начался, поэтому хуй знает</b>
	''')
	sleep(1.9)
	app.send_message(msg.chat.id, f'''
	<b>— Бля, чуваки, шутки шутками, но не занимайтесь хуйнёй, я вас умоляю. А-а-а!</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Головы сияют на моей едкой катане</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Голоса этих ублюдков по пятам бегут за нами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Погружённый в Изанами, все колёса под глазами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Её взгляд убьёт любого, её взгляд убьёт цунами</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Генерал Гавс, ха, вижу вас без гема</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Я отдал приказ, и все умрут от реквиема</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Дота-рэп — топ чарт, ха, наебал систему</b>
	''')
	sleep(1.3)
	app.send_message(msg.chat.id, f'''
	<b>Mute all chat, я на лям скупил все гемы, ха-ха</b>
	''')
	sleep(1.4)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, бля</b>
	''')

	sleep(0.5)
	global number
	number = number + 1
	app.send_message(message.chat.id, f'''
	 <b> </b>
	 ''')

@app.on_message(filters.command(["Oxxxymiron", "versus", "battle"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Гавно</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Залупа</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Пенис</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Хер</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Давалка</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Хуй</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Блядина</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Галовка</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Шлюха</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Жопа</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Член</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Еблан</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Петух</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Мудила</b>
	''')
	sleep(0.7)
	app.send_message(msg.chat.id, f'''
	<b>Рукаблуд</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Ссанина</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Очко</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Блядун</b>
	''')
	sleep(0.5)
	app.send_message(msg.chat.id, f'''
	<b>Вагина</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Сука</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Ебланище</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Влагалеще</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Пердун</b>
	''')
	sleep(0.4)
	app.send_message(msg.chat.id, f'''
	<b>Дрочила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пидор</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пизда</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Туз</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Малафья</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Гомик</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Мудила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Пилотка</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Манда</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Анус</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Вагина</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Путана</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Педрила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Шалава</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Хуила</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Мошонка</b>
	''')
	sleep(0.3)
	app.send_message(msg.chat.id, f'''
	<b>Елда</b>
	''')
	sleep(0.8)
	app.send_message(msg.chat.id, f'''
	<b>Раунд!</b>
	''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("zoo", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мне собачку тр*хнуть утром мало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Надо утром вечером и днем</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У меня вчера змея сосала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А сегодня я е*усь с ежом!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мама принесла вчера котенка</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>На ночь я его к себе забрал</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу во все дыры отъе*ал!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я е*у собак, всегда готов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сразу тр*хнуть несколько котов</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да, я зоофил, не говори</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Лучше мне собачку подари!</b>
	''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command(["polmateri", "stars"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да я скорей подохну, чем заговорю с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я точно буду одинок до конца своих дней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Парней так много, и чем я могу запомниться?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я сброшусь с крыши, лишь бы мне не опозориться</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Покинуть город, лишь бы не говорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Разбиться насмерть, лишь бы не говорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Потерять память, лишь бы не говорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Пропасть бесследно, лишь бы не говорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Её глаза прекрасны, детка LovelyLove</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Её волосы достойны самых преданных баллад, а</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Таких красивых мало просто поискать</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Она сияет ярче звёзд, и освещается Земля</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сброситься с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>«Привет, как день?» — щас подойду и скажу ей</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но я скорей… Скорей подохну, чем заговорю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой батя скажет мне, что я ёбаное ссыкло</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В мои годы был женат на маме и служил в ОМОН</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но зачем мне кто-то? Одинокий музыкант</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Презираю всё, что вижу, тут Марголдин — реальный панк, я</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Тёлки не нужны — мы и без них справимся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Нет лучше пизды, чем очко товарища</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Её глаза прекрасны, детка LovelyLove</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Её волосы достойны самых преданных баллад, а</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Таких красивых мало просто поискать</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Она сияет ярче звёзд, и освещается Земля</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сбросится с крыши или заговорить с ней</b>
	''')
	sleep(1)

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("landisi", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Толстый х*й под самый нос</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но меня не проебешь</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Х*й на ландыш не похож</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Х*й — большой</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты вчера мне преподнес</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мех с п*зды, клочек волос</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И сказал, что это ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но меня не наебешь</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Клок на ландыш не похож</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Клок — большой</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А ландыш — маленький</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Это весенние цветы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Их подарил мне ты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мы забрались в камыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Нае*ались от души</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Нах*я нам эти ландыши?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты и так, б*ядь, хороша</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ну и что</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Что ландыш маленький?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ландыши, ландыши</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Теплого мая привет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Девушка юноше</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Делает м*нет</b>
	''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command(["NeverEnough", "ne", "zxcursed"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>MUPP broken your heart</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, ха-а, а-а</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Крики necromastery и вопли подо мной</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Руки дезоляторы и shadow nevermore</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз в ебало, твоя сука вся течёт</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Она говорит ей мало, но я продолжу ход</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Твоё сердце так пылает, его превращаю в лёд</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Как Лелуш управляю этой сукой — она орёт</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я бегу ща как Соник, попробуй поймай</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Эта сука не знает, как подойти — отступай</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>На мне ща куча дури (А-а) и это не манта</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Вдавил шб и таунт трайни (А-а), один из ста</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Записал тебя в тетрадку и я не Ягами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Zero reasons to talk, ублюдки, это цунами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я, бля, Тобирама — все бастарды за бортами</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я неуязвим, моя клятва — это синигами (Ага)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Fear — это страх, а страх — это я</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Под баффом агилы берсерк mode Киллуа</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Эй, я как Вольт — называй неуловимый</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я в showdown'е, как Кольт — твои патроны летят мимо</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ты на этой мапе — ноль, ты не скрывайся — тебя видно</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я как Рико, дал обойму, мой лайфстайл — psychokilla</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>De-Dead inside mode, я бегу по головам</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Оверсайз весь шмот, я на трапе тут и там</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой скилл — шаблон, я по рофлу на битах</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Зачем мне октагон? Могу выйти на финдах, ха</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Sla-Sla-Slayer убийца, Рефреш обновился</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Реквием в сердце — ты болью проникся</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>За спиной нет крыльев, но я лечу</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Butterfly на руке и я его точу (А)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Emotional emptiness — совсем не грущу</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Why do you even try? Заживо сожру</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я-Я не под спидами, просто под хастой</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Су-Су-Супер Сайян, so slow — это штрафной</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Выпал крит, это не Кристалис</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Моб Психо сто, но мы не сыгрались</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Зеницу Агацума — называй меня скорость</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Меня не остановить, тревела на ноги полная готовность</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>See you later на полу следы от ног остались навсегда</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Позади меня нет жара, only холода</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Не оставлю тебе выбора, творя, бля, чудеса</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Never enough даю те полчаса, убив всех enemy, ну да-да</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Ха-а, продолжай, ха-а (Yeah, ho)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Демоны в башке, рэйзы на тебе</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Кричишь от боли, приклонись судьбе</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Поток Акаши, ты вставший на колени</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Не посмел бы даже думать о замене</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>У меня нет кагуне, просто я ебанутый</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Feel no pain — и я стал культом</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Тысячи гулей узнают по никнейму</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Чекай телеграм, там весь сквад Антейку</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Если у тя бабочка — я не миссую</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Если у тя мкб — ты вовсе не хитуешь</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>W/W — сияю ярче Иллидана (А-а)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Парень ставит паузу и я достаю катану</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Ха-а, ха-а, а-а**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Залетаю с автоматом, ставлю лазер коллиматор</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Твоя тати — моя тати, со мной едет в Maserati</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Фиолетовая shawty, её тело на кровати</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Я снёс им всем ебало — это стиль аннигилятор</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Третий глаз как шинигами, в темноте не вижу свет</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Venom orb в моём пресете, замедляю в интернете</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Вооружён зубами, я их отправлю на тот свет</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Они стреляют в моё тело, мой armor бронежилет (Арата)</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Мо-Моя катана самехада — поедает этих тварей</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Холодает в моём теле, бью — я будто Гаара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>Один hit по тебе — ты пропал с радара</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Крики Necromastery и вопли подо мной**</b>
	''')
	sleep(0.6)
	app.send_message(msg.chat.id, f'''
	<b>**Руки дезоляторы, shadow nevermore**</b>
	''') 
	sleep(1)
	app.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEENvNiNs_MoD7fFverk1v5wqoX2Fd-tQACxgoAAiu8OUlTcsBdvR5J0iME")

	sleep(0.5)
	global number
	number = number + 1
	app.send_message(message.chat.id, f'''
	 <b> </b>
	 ''')

@app.on_message(filters.command(["kaif", "konfuz"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты в моих мыслях так плотно засела</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А я не был грубым, так, просто манера</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Все подружки в шоке, Gucci, Panamera</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>От голоса моего ты опьянела</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Где девочка манит, там так сильно дурманит</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждую секунду я звоню, но телеф занят</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кайф ты поймала, тебе всегда мало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты не представляешь, как мне тебя не хватало</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сильно бьётся сердце, сама не ожидала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Наконец-то твоя совесть тебя наказала</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Девочка в предвкушении азарта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Когда встретил тебя, не нашёл пути обратно</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты — моё сокровище, козырная карта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мы дошли до финиша, не дойдя до старта</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Что ты забыла у меня на repeat'е?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В твоих глазах я тону — помогите!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, моя родная, не грусти, не сердись так</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты просто лови, ты лови, ты лови кайф</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твои подружки хотят ко мне в Panamer'у</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Говорят мне о любви, но я не верю</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчат мне в Inst'у для отметки в Storie</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я выбрал тебя, а остальным — sorry</b>
	''')

	app.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEEPJ1iOeGaHrwudfx0VAkPdzcJV7rSsAACLBYAAqlr0EsgtENNn-yMxyME")

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command(["zelglaz", "minin"], prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Глаз, зеленый глаз, влюбился в тебя так легко</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Строчка горяча — кипяток</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сел ща микро и вые*ал биток</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У тебя спереди неплохой видок</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты не ровный пацан, ты кидок</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Она красивая, будто модель</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мне повезло быть вместе с ней</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не видел девушек горячей</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Такую жизнь мог увидеть во сне (Только там)</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Помню, как при встрече сразу же в тебя влюбился</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>С тобою проходили быстро дни и месяца</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Помню из-за ревности сильно на тебя злился</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но Минин влюбился в твои зеленые глаза</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Зеленый глаз, влюбился в тебя так легко</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Носишь оверсайз, встретиться было суждено</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не спрошу за прайс, ведь это дело не мое</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты будто Пеннивайз, но мнение о себе wow</b>
	''')

	sleep(5)
	msg.edit(f'''
		🍃 author: @no_gold''')
	sleep(5)
	msg.delete()

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command("shadowfiend", prefixes=".") & filters.me)
def valentine(app, msg):

	app.send_message(msg.chat.id, f'''
	<b>PLVSTIC, ты такой стильный!</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– shadowraze?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Нет, блять, Pavshiy</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Mariyaunban?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>– Нет, блять, Prepodobniy, ха-ха-ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Shadow-Shadow Fiend, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Парень без обид</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твой ugly face уже разбит</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Слышь, ебучий псих, твой playstyle — это стыд, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я, бля, Shadow Fiend, ты — ебучий психокид, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты, блядь, кто такой, а? Сука, чё не нравится?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз в ебло и твоё эго, блядь, расплавится</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твоя блядь на пос-пять — она лает и кусается</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я бля perfect player, меня это не касается, сука</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ах-ха-ха, привет, Каспер, помнишь меня?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Как там твой сыночек, безмозглый дегенерат, Стасик,</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>поживает? Никто его ещё не пришиб, как муху ебаную?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>А, броу? Как там твоя мать, шлюха гнилозубая, поживает,</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>тоже, рассказывай</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>До встречи на эпицентре, сын шлюхи</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Коил, коил, коил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Сука, прямо подо мною</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Каждый рэйз наполнен болью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кричат души на Стокгольме</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC и ты покойник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моём лобби ты не воин</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не рычи, надень намордник</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Реквием, тебе хуёво, ха</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Трипл рэйз на шее</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мне не нужно разрешение, ха</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Убрал тебя с мида, в моём лобби стал мишенью</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Твой Титаник пал, блядь, или сука, потерпел крушение</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Ты ебучий dead inside интернетных отношений</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Моё лобби ZXC, но я не жду больше минуты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В деле топовый SF, мои коилы – терракоты</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мои коилы — ZXC, мои души — громче всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>ZXC — ты отлетаешь от раскаста shadowraze</b>
	''')

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command("astralstep", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Разрубаю глефой ноги, я бегу, за спиной Боги (А-а)</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Как на ринге, только в лобби, ты подох, бля (Ха-ха)</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я стреляю — это step, бро, you low</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я быстрее этих lame'ов, you slow, братан</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я use'аю эти spell'ы — это мой lifesteal</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я sip'ую эти step'ы — это жёсткий стиль</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Долбоёб назвал НН-ом, я его простил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я убил их, даже не завейстил сил</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Погасил этих псин, курю бензин, I'm steal</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Показал им старый стиль, добил их всех, а кто спросил?</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Astral step поразил долбоёбов и терпил</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У меня сотка гулей, посмотри — ты вновь один</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Вот ты прикинь, челы чё-то там на Дота-рэп гонят, да</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>А я за один квартал лям рублей получил, бля</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>Лимон за Дота-рэп, ха-ха-ха-ха</b>
	''')
	sleep(1.5)
	app.send_message(msg.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, лечу прям вверх</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой красный сет убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>У них в башке один preset</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я покажу тоннельный свет</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не найти меня, я скрылся</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я пропавший в dissimilate</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не оставлю им и следа</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Из ниоткуда выйду в late</b>
	''')
	app.send_message(msg.chat.id, f'''
	<b>Hunter on ghoul, я убил их всех</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Уворот от пуль, у меня есть вес</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Нахуй граммовка, у меня есть весы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я не злодей, но у меня свои бесы</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Много валюты, имею и песо</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Много энергии, я будто Тесла</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю так метко, все пули прям в висок, а</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>В моих глазах горит квазар</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Иду вперёд, ни шагу назад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Кидаю step, бегу на старт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Весь твой профит идёт на спад</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Стреляю метко, как солдат</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Мой step сияет — это факт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И я step'ую прямо в такт</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Им не убить меня, so hard</b>
	''')

	sleep(0.5)
	global number
	number = number + 1

@app.on_message(filters.command("gay", prefixes=".") & filters.me)
def betaloves(_, msg):
	gay1 = 0

	msg.edit(f'''
	Превращяем тебя в гея!''')
	sleep(0.6)
	while gay1 <= 100:
		sleep(0.1)
		gay1 += 1
		msg.edit(f'''
		{gay1}%''')
	if gay1 >= 100:
		msg.edit(f'''
		Загрузка.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка...''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка...''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации.''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации..''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации...''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации.''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации..''')
		sleep(0.6)
		msg.edit(f'''
		Смена ориентации...''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного.''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного..''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного...''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного.''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного..''')
		sleep(0.6)
		msg.edit(f'''
		Подождите немного...''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена...''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка почти завершена...''')
		sleep(1)
		msg.edit(f'''
		Поздравляем! Загрузка успешно завершена! ''')
		sleep(1)
		msg.edit(f'''
		Теперь ты 100% гей! ''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("bogdan", prefixes=".") & filters.me)
def betaloves(_, msg):
	kakish1 = 0
	kakish = random.randint(1, 25)

	msg.edit(f'''
	Богдан начел искать какиш.''')
	sleep(0.7)
	msg.edit(f'''
	Богдан начел искать какиш..''')
	sleep(0.7)
	msg.edit(f'''
	Богдан начел искать какиш...''')
	sleep(0.7)
	while kakish1 <= 99:
		sleep(0.1)
		kakish1 += 1
		msg.edit(f'''
		Поиск какиша выполнен на {kakish1}%''')
	if kakish1 >= 99:
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл.''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл..''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл...''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл.''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл..''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл...''')
		sleep(1)
		msg.edit(f'''
		Богдан нашел {kakish} кг какиша!''')


	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def betaloves(_, msg):
	hack = 0

	msg.edit(f'''
	Идёт взлом чата.''')
	sleep(0.2)
	msg.edit(f'''
	Идёт взлом чата..''')
	sleep(0.2)
	msg.edit(f'''
	Идёт взлом чата...''')
	sleep(0.2)
	while hack <= 99:
		sleep(0.1)
		hack += 1
		msg.edit(f'''
		Взлом чата выполнен на {hack}%''')
	if hack >= 99:
		msg.edit(f'''
		Загрузка файлов.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка файлов..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка файлов...''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка файлов.''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка файлов..''')
		sleep(0.6)
		msg.edit(f'''
		Загрузка файлов...''')
		sleep(0.6)
		msg.edit(f'''
		Чат успешно взломан! Все данные отправятся в облоко Telegram.''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("onal", prefixes=".") & filters.me)
def betaloves(_, msg):
	onal = 0
	onal2 = random.randint(0, 325)

	msg.edit(f'''
	Поиск админа.''')
	sleep(0.6)
	msg.edit(f'''
	Поиск админа..''')
	sleep(0.6)
	msg.edit(f'''
	Поиск админа...''')
	sleep(0.6)
	msg.edit(f'''
	Админ найден!''')
	sleep(0.8)
	msg.edit(f'''
	Идёт поиск анального отверстия админа.''')
	sleep(0.6)
	msg.edit(f'''
	Идёт поиск анального отверстия админа..''')
	sleep(0.6)
	msg.edit(f'''
	Идёт поиск анального отверстия админа...''')
	sleep(0.6)
	msg.edit(f'''
	Найдено!''')
	sleep(0.8)
	msg.edit(f'''
	Измерение анального отверстия админа.''')
	sleep(0.6)
	msg.edit(f'''
	Измерение анального отверстия админа..''')
	sleep(0.6)
	msg.edit(f'''
	Измерение анального отверстия админа...''')
	sleep(0.6)
	msg.edit(f'''
	Анальное отверстие админа состовляет {onal2} км''')
	sleep(1)
	while onal <= 55:
		sleep(0.1)
		onal += 1
		msg.edit(f'''
		Анальное проникновение админу выполнено на {onal}%''')
	if onal == 56:
		sleep(0.3)
		onal += 1
		msg.edit(f'''
		Рука устала''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки.''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки..''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки...''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки.''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки..''')
		sleep(0.6)
		msg.edit(f'''
		Отдых руки...''')
		sleep(0.6)
		msg.edit(f'''
		Рука отдохнула, можно продолжать...''')
		sleep(0.8)
		while onal >= 57:
			sleep(0.1)
			onal += 1
			msg.edit(f'''
			Анальное проникновение админу выполнено на {onal}%''')
			if onal == 99:
				sleep(0.6)
				msg.edit(f'''
				Жопа админа порвана. Поздравляю!''')
				break

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("stop", prefixes=".") & filters.me)
def betaloves(_, msg):
	msg.edit('''
		<b>[!] Скрипт был остановлен командой .stop!\nДля перезапуска введите в термукс команду -\n`cd tgscript && python tgscript.py`\n\nАвтор скрипта: @no_gold</b>''')
	sleep(1)
	print(Fore.RED + "Скрипт остоновлен командой .stop!\nДля перезапуска нажмите CTRL + Z и введите 'python tgscript.py'\n")
	quit()

@app.on_message(filters.command("magic", prefixes=".") & filters.me)
def betaloves(_, msg):

	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍 
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🧡🧡🤍🧡🧡🤍🤍
	🤍🧡🧡🧡🧡🧡🧡🧡🤍
	🤍🧡🧡🧡🧡🧡🧡🧡🤍 
	🤍🧡🧡🧡🧡🧡🧡🧡🤍
	🤍🤍🧡🧡🧡🧡🧡🤍🤍
	🤍🤍🤍🧡🧡🧡🤍🤍🤍
	🤍🤍🤍🤍🧡🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛💛🤍💛💛🤍🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍🤍💛💛💛💛💛🤍🤍
	🤍🤍🤍💛💛💛🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚💚🤍💚💚🤍🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍🤍💚💚💚💚💚🤍🤍
	🤍🤍🤍💚💚💚🤍🤍🤍
	🤍🤍🤍🤍💚🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💙💙🤍💙💙🤍🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍🤍💙💙💙💙💙🤍🤍
	🤍🤍🤍💙💙💙🤍🤍🤍
	🤍🤍🤍🤍💙🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💜💜🤍💜💜🤍🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍🤍💜💜💜💜💜🤍🤍
	🤍🤍🤍💜💜💜🤍🤍🤍
	🤍🤍🤍🤍💜🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍💛🧡🤍🤍
	🤍🧡🧡💜🧡💚💙💛🤍
	🤍💛💚💙💚💜💚💜🤍
	🤍💙💛💜🧡🧡💚💛🤍
	🤍🤍🧡💚🧡💚💙🤍🤍
	🤍🤍🤍💜💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍❤️🧡🤍🤍
	🤍💙❤️💜❤️💚💙💛🤍
	🤍💛💚💙💚💜💚❤️🤍
	🤍💙❤️💜❤️💙💚💙🤍
	🤍🤍🧡💚🧡❤️💙🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛❤️🤍💛💛🤍🤍
	🤍💙❤️💜💛❤️💙💛🤍
	🤍❤️💚❤️💚💜💚❤️🤍
	🤍💙❤️💜❤️❤️💚💙🤍
	🤍🤍💛💚🧡💛❤️🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍💛🧡🤍🤍
	🤍🧡🧡💜🧡💚💙💛🤍
	🤍💛💚💙💚💜💚💜🤍
	🤍💙💛💜🧡🧡💚💛🤍
	🤍🤍🧡💚🧡💚💙🤍🤍
	🤍🤍🤍💜💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍❤️🧡🤍🤍
	🤍💙❤️💜❤️💚💙💛🤍
	🤍💛💚💙💚💜💚❤️🤍
	🤍💙❤️💜❤️💙💚💙🤍
	🤍🤍🧡💚🧡❤️💙🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛❤️🤍💛💛🤍🤍
	🤍💙❤️💜💛❤️💙💛🤍
	🤍❤️💚❤️💚💜💚❤️🤍
	🤍💙❤️💜❤️❤️💚💙🤍
	🤍🤍💛💚🧡💛❤️🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️
	❤️❤️❤️❤️
	❤️❤️❤️❤️
	❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️
	❤️❤️❤️
	❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️
	❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("f", prefixes=".") & filters.me)
def betaloves(_, msg):
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)
	msg.edit(f'''
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌓🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌑🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌓🌕🌕🌕
🌕🌕🌗🌑🌑🌑🌑🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌗🌑🌓🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕🌕''')
	sleep(0.4)

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("loveyou", prefixes=".") & filters.me)
def betaloves(_, msg):
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
💜💜💜❤️❤️❤️💜💜💜
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
💜💜💜❤️❤️❤️💜💜💜
💙💙💙💙❤️💙💙💙💙
''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
💜💜💜❤️❤️❤️💜💜💜
💙💙💙💙❤️💙💙💙💙
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
💜💜💜❤️❤️❤️💜💜💜
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💛💛❤️❤️❤️❤️❤️💛💛
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
🧡❤️❤️❤️❤️❤️❤️❤️🧡
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
🤎❤️❤️❤️❤️❤️❤️❤️🤎
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
🖤❤️❤️❤️❤️❤️❤️❤️🖤
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘❤️❤️💘❤️❤️💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💝💝💝💝💝💝💝💝💝
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f'''
💘💘💘💘💘💘💘💘💘''')
	sleep(0.4)
	msg.edit(f"I love you 💘")
	
	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("try", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[Удачно]", "[Не удачно]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: Вы не ввели вопрос!\nИспользование: .try <вопрос>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("text", prefixes=".") & filters.me)
def betaloves(_, msg):
	text1 = " ".join(msg.command[1:])

	if not text1:
		msg.edit(f'''
			**Error: Вы не ввели текст!\nИспользование: .text <текст>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{text1}ㅤㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤ{text1}ㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤ{text1}ㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤ{text1}ㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤ{text1}ㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤㅤ{text1}''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤ{text1}ㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤ{text1}ㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤ{text1}ㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤ{text1}ㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			{text1}ㅤㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			{text1}''')

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("hackpc", prefixes=".") & filters.me)
def go(_, msg):
	perc = 0
	while(perc < 100):
		try:
			text = "👮‍ Взлом твоего ПК в процессе ... " + str(perc) + "%"
			msg.edit(text)
			perc += random.randint(1, 3)
			sleep(0.1)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🟢 Ты успешно взломан!")
	sleep(3)
	msg.edit("😈 Поиск секретных данных ...")
	perc = 0
	while(perc < 100):
		try:
			text = "😈 Поиск секретных данных ... " + str(perc) + "%"
			msg.edit(text)
			perc += random.randint(1, 5)
			sleep(0.15)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🤑 Найдены важные данные!!!")

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("run", prefixes="."))
def run(app, msg):
	testr = 0
	while(testr < 50):
		try:
			text = "🏃"
			msg.edit(text)
			sleep(0.1)
			text = "🚶"
			msg.edit(text)
			sleep(0.1)
			testr += random.randint(1, 3)
		except FloodWait as e:
			sleep(e.x)

	msg.edit("добежал")

@app.on_message(filters.command("pong", prefixes="."))
def pong(app, msg):
	testr = 0
	while(testr < 5):
		try:
			text = "▐⠂       ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐⠈       ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠂      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠠      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⡀     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠠     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠂    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠈    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠂   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠠   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⡀  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠠  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠂ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠈ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⠂▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⠠▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⡀▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠠ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠂ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠈  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠂  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠠   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⡀   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠠    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠂    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠈     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠂     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠠      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⡀      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐⠠       ▌"
			msg.edit(text)
			sleep(0.1)
			testr += random.randint(1, 3)
		except FloodWait as e:
			sleep(e.x)

	msg.edit("▐⠂⠂⠂⠂⠂⠂⠂⠂▌")

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command(["console", "cmd"], prefixes="."))
def brain(app, msg):
	msg.edit("`>_`")
	sleep(0.1)
	msg.edit("`>  `")
	sleep(0.1)
	msg.edit("`>_`")
	sleep(0.1)
	msg.edit("`>  `")
	sleep(0.1)
	msg.edit("`>_`")
	sleep(0.1)
	msg.edit("`>c_`")
	sleep(0.1)
	msg.edit("`>cd`")
	sleep(0.1)
	msg.edit("`>cd _`")
	sleep(0.1)
	msg.edit("`>cd p`")
	sleep(0.1)
	msg.edit("`>cd pr_`")
	sleep(0.1)
	msg.edit("`>cd pro`")
	sleep(0.1)
	msg.edit("`>cd proj_`")
	sleep(0.1)
	msg.edit("`>cd proje`")
	sleep(0.1)
	msg.edit("`>cd projec_`")
	sleep(0.1)
	msg.edit("`>cd project`")
	sleep(0.6)
	msg.edit("`>cd project`\n" + "`project>_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>g`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>gi_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git i_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git in`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git ini_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`")
	sleep(0.6)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>g_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>gi`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git a_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git ad`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 3%`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 5%`")
	sleep(0.3)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 30%`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 36%`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [====------] 41%`")
	sleep(0.4)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [======----] 67%`")
	sleep(0.2)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>g_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>gi`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git c`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git co_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git com`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git comm_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commi`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -a_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"I`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`")
	sleep(2)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>g_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>gi`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git p`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pu_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pus`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push h`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push he_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push her`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push hero_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push herok`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku m`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku ma_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mas`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mast_`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku maste`")
	sleep(0.1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`")
	sleep(2)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.`")
	sleep(1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.`")
	sleep(1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.`")
	sleep(1)
	msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.\n  remote: Verifying deploy... done.`")

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command(["brain", "b"], prefixes="."))
def brain(app, msg):
	msg.edit("Твой мозг \n🗑          🧠🏃🏻")
	msg.edit("Твой мозг \n🗑         🧠🏃🏻")
	msg.edit("Твой мозг \n🗑        🧠🏃🏻")
	msg.edit("Твой мозг \n🗑       🧠🏃🏻")
	msg.edit("Твой мозг \n🗑      🧠🏃🏻")
	msg.edit("Твой мозг \n🗑     🧠🏃🏻")
	msg.edit("Твой мозг \n🗑    🧠🏃🏻")
	msg.edit("Твой мозг \n🗑   🧠🏃🏻")
	msg.edit("Твой мозг \n🗑 🧠🏃🏻")
	msg.edit("Твой мозг в мусорке \n🗑 🙍🏼‍♂️")

	sleep(5)
	global number
	number = number + 1

@app.on_message(filters.command("vopros", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.4
	for i in range(1):
		sleep(0.001)
		msg.edit(f'''      
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
''')
	sleep(5)
	global number
	number = number + 1


@app.on_message(filters.command("toxic", prefixes=".") & filters.me)
def valentine(app, message):
	app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>пиздобратия мандопроушечная, уебище залупоглазое</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>гнидопаскудная хуемандовина</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>хуй тебе в глотку через анальный проход</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	<b>гандон с гонореей...</b>
	''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>сортирующего яйца в пизде кастрированной кобылы</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>ебун хуеголовый, пидрасня ебаная. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Залупоголовая блядоящерица. .</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Трипиздоблядская промудохуина! </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>ебаквакнутый распиздаеб... </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Промудохуепиздамразоблядское злоепиздие </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Облямудевшая хуеблядина четырестохуйная</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>вестипёздная мразотоблядская шлюхасосалка. </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>блядь шмара козельуебок сдохни </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
	 ''')
	sleep(0.5)
	app.send_message(message.chat.id, f'''
	 <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
	 ''')
	sleep(0.5)
	global number
	number = number + 1
	app.send_message(message.chat.id, f'''
	 <b>️</b>
	 ''')

jopa = '''
		   <b>ВЗЛОМ ЖОПЫ</b> 
		   <b><i>Loading...</i></b> 
	10%  █▒▒▒▒▒▒▒▒▒▒▒▒
	30%  ███▒▒▒▒▒▒▒▒▒▒    
	50%  █████▒▒▒▒▒▒▒▒
	66%  ██████▒▒▒▒▒▒▒
	79%  ████████▒▒▒▒▒
	84%  █████████▒▒▒▒
	89%  ██████████▒▒▒
	95%  ████████████▒
	99%  █████████████
	100% █████████████
	<b> ВАША ЖОПА ВЗЛОМАНА </b>
	<b><i>Создатель: "Прощайте"</i></b>
	<b><i>Создатель: "Прощайте"</i></b>
	<b><i>Создатель: "Прощайте"</i></b>
'''
zxc = '''
<b>- All my friends are toxic, all ambitionless 💚</b>

<b>- All my friends are toxic, all ambitionless 💜</b>

<b>- All my friends are toxic, all ambitionless 💛</b>

<b>- So rude and always negative 🤍</b>

<b>- So rude and always negative 💚</b>

<b>- So rude and always negative 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💔</b>

<b>- I need new friends, but it's not  that quick and easy 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💚</b>

<b>- Oh, I'm drowning, let me breathe 💜</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

'''


love = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
<b>Загрузка любви...</b>
❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>

'''

comp = '''
<b>Крошечные напоминания того, что ты...</b> 

<b>Самая удивительная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая красивая</b> ✨

<b>Самая успешная</b> ✨

<b>Самая заботливая</b> ✨

<b>Самая милая</b> ✨

<b>Самая прекрасная</b> ✨

<b>Самая умная</b> ✨

<b>Самая шикарная</b> ✨

<b>Самая обалденная ✨</b>

<b>Самая очаровашка</b> ✨

<b>Самая любимая</b> ✨

<b>Самая весёлая</b> ✨

<b>Самая нежная</b> ✨

<b>Самая яркая</b> ✨

<b>Самая прелестная</b> ✨

<b>Самая приятная</b> ✨

<b>Самая сладкая</b> ✨

<b>Самая дивная</b> ✨

<b>Самая ангельская</b> ✨

<b>Самая добрая</b> ✨

<b>Самая бесподобная</b> ✨

<b>Самая волшебная</b> ✨

<b>Самая лучшая</b> ✨

<b>Самая крутышка</b> ✨

<b>Самая аромтная</b> ✨

<b>Самая единственная</b> ✨

<b>Самая искренняя</b> ✨

<b>Самая ласковая</b> ✨

<b>Самая романтичная</b> ✨

<b>Самая великолепная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая страстная</b> ✨

<b>Самая игривая</b> ✨

<b>Самая стройная</b> ✨

<b>Самая безумная</b> ✨

<b>Самая симпатичная</b> ✨

<b>Самая изящная </b> ✨

<b>Самая талантливая ✨</b>

<b>Самая элегантная ✨</b>

<b>Самая чуткая ✨</b>

<b>Самая отзывчивая ✨</b>

<b>Самая уникальная ✨</b>

<b>Самая смелая ✨</b>

<b>Самая уверенная ✨</b>

<b>Самая особенная ✨</b>

<b>Самая изумительная ✨</b>

<b>Самая настоящая ✨</b>

<b>Самая обаятельная ✨</b>

<b>Самая пушистая ✨</b>

<b>Самая кокетливая ✨</b>

<b>Самая теплая ✨</b>

<b>Самая энергичная ✨</b>

<b>Самая неотразимая ✨</b>

<b>Самая неописуемая ✨</b>

<b>Самая грациозная ✨</b>

<b>Самая сказочная ✨</b>

<b>Самая желанная ✨</b>

<b>Самая изысканная ✨</b>

<b>Самая мечтательная ✨</b>

<b>Самая безупречная ✨</b>

<b>Самая совершеная ✨</b>

<b>Самая честная ✨</b>

<b>Самая улыбчивая ✨</b>

<b>Самая ненаглядная ✨</b>

<b>Самая женственная ✨</b>

<b>Самая цветущая ✨</b>

<b>Самая гармоничная ✨</b>

<b>Самая отрадная ✨</b>
'''

comp1 = '''
<b>Ты удивительная</b> ✨

<b>Ты внимательная</b> ✨

<b>Ты красивая</b> ✨

<b>Ты успешная</b> ✨

<b>Ты заботливая</b> ✨

<b>Ты милая</b> ✨

<b>Ты прекрасная</b> ✨

<b>Ты умная</b> ✨

<b>Ты шикарная</b> ✨

<b>Ты обалденная ✨</b>

<b>Ты очаровашка</b> ✨

<b>Ты любимая</b> ✨

<b>Ты весёлая</b> ✨

<b>Ты нежная</b> ✨

<b>Ты яркая</b> ✨

<b>Ты прелестная</b> ✨

<b>Ты приятная</b> ✨

<b>Ты сладкая</b> ✨

<b>Ты дивная</b> ✨

<b>Ты ангельская</b> ✨

<b>Ты добрая</b> ✨

<b>Ты бесподобная</b> ✨

<b>Ты волшебная</b> ✨

<b>Ты лучшая</b> ✨

<b>Ты крутышка</b> ✨

<b>Ты аромтная</b> ✨

<b>Ты единственная</b> ✨

<b>Ты искренняя</b> ✨

<b>Ты ласковая</b> ✨

<b>Ты романтичная</b> ✨

<b>Ты великолепная</b> ✨

<b>Ты внимательная</b> ✨

<b>Ты страстная</b> ✨

<b>Ты игривая</b> ✨

<b>Ты стройная</b> ✨

<b>Ты безумная</b> ✨

<b>Ты симпатичная</b> ✨

<b>Ты изящная </b> ✨

<b>Ты талантливая ✨</b>

<b>Ты элегантная ✨</b>

<b>Ты чуткая ✨</b>

<b>Ты отзывчивая ✨</b>

<b>Ты уникальная ✨</b>

<b>Ты смелая ✨</b>

<b>Ты уверенная ✨</b>

<b>Ты особенная ✨</b>

<b>Ты изумительная ✨</b>

<b>Ты настоящая ✨</b>

<b>Ты обаятельная ✨</b>

<b>Ты пушистая ✨</b>

<b>Ты кокетливая ✨</b>

<b>Ты теплая ✨</b>

<b>Ты энергичная ✨</b>

<b>Ты неотразимая ✨</b>

<b>Ты неописуемая ✨</b>

<b>Ты грациозная ✨</b>

<b>Ты сказочная ✨</b>

<b>Ты желанная ✨</b>

<b>Ты изысканная ✨</b>

<b>Ты мечтательная ✨</b>

<b>Ты безупречная ✨</b>

<b>Ты совершеная ✨</b>

<b>Ты честная ✨</b>

<b>Ты улыбчивая ✨</b>

<b>Ты ненаглядная ✨</b>

<b>Ты женственная ✨</b>

<b>Ты цветущая ✨</b>

<b>Ты гармоничная ✨</b>

<b>Ты отрадная ✨</b>

<b>Ты няшка милашка ✨</b>
'''

ziga = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''

end_message = '<b>  </b>'
app.run()