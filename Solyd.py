 #!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import session
import BeautifulSoup
KOZ = '''
         █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
         █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█ ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
         █░░║║║╠─║─║─║║║║║╠─░░█ ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
         █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█ ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
         █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒'''

print '----------------------------------------------------'
ZYX = '''
                ▒▒▒▒▒▒▐███████▌     łαbørαŧøriø Ŧαηŧαรмα
                ▒▒▒▒▒▒▐░▀░▀░▀░▌ Coded : ૐ łuŧЋ1єr - ルシアー
                ▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌     WebScraping Python
                ▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄
                ▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐
        +=========================================+
        |......♚ Solyd - Sistema de Ensinos.......|
        +-----------------------------------------+
        |♚Coded: @Tweelv5 (Telegram)              |
        |♚Contact:www.facebook.com/TerminalRoot404|
        |♚Date: 21/12/2016                        |
        |♚Chanell:telegram.me/Phantasm_Lab        |
        |♚Changing the Description of this tool   |
        |Won't made you the coder ^_^ !!!         |
        |♚Respect Coderz ^_^(Open_Source_Project) |
        |♚I take no responsibilities for the      |
        |  use of this program !                  |
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
print (KOZ)
print (ZYX)

USERNAME = raw_input('Digite Seu Login/Email ➣➣➣ ')
PASSWORD = raw_input('Digite Sua Senha ➣➣➣ ')
payload = { 'submit': 'login', 'username': USERNAME, 'password': PASSWORD } 
with session() as c:
	c.post('http://ensino.solyd.com.br/login/index.php', data=payload)
	response = c.get('http://ensino.solyd.com.br/user/profile.php')
 	#print(response.headers)
 	#print(response.text)
Beaut = BeautifulSoup.BeautifulSoup(response.content)
soup = BeautifulSoup.BeautifulSoup(response.content.decode('utf-8','ignore'))
Scraping = str(soup.title)
#print Login
#print 'Login Efetuado Com Sucesso!', soup.title.text
print "Status Do Perfil ➣➣➣", Beaut.title.text
if Scraping == '<title>Solyd - Ensino a Distância: Acesso ao site</title>':
	print '✘ Die Acount... Login Down! ✘\n Login Ou Senha Incorretos, Por Favor Faça uma Nova Requisição...'
else:
	print '✅ #Live Acount... Login Actived! ✅\n Bem vindo ao sistema de Ensino Solyd.\n Você acabou de fazer uma requisição Post...'
print " Obrigado Por Usar O Programa, Sinta A Vontade Para Melhora-lo! ^^\n", XXX

 	
