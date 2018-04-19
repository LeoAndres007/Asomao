#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Asomao: a IRC bot
# (c) 2018 Leo Hernandez
# Under GPLv3 license

import socket
import string

from time import sleep
from commands import getoutput
from urllib import urlopen
from re import search, sub

HOST="irc.freenode.net"
PORT=6667
NICK="Asomao"
IDENT="Asomao"
REALNAME="Asomao IRC"
CHAN="#Asomao"
readbuffer=""
track = ''
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)

def send_msg(msg):
	s.send("PRIVMSG %s :%s" % (CHAN, msg))

while 1:
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )
	for line in temp:
		print line
		line=string.rstrip(line)
		line=line.split(CHAN + ' :')

		if line[0].find("PING") != -1:
			pingid = line[0].split()[1]
			s.send("PONG %s\r\n" % pingid)

		elif line[0].find('JOIN') != -1:
			name = line[0].split('!')[0].split(':')[1]
			if name != NICK and name.find(HOST) == -1:
				sleep(5)
				send_msg("Benvenido al canal oficial en IRC de la comunidad Canaima. Por favor, antes de usar el chat lee nuestras normativas: https://goo.gl/cSYrK8 %s \n" % name)

		if len(line) > 1:
			if 'facebook' in line[1].split():
				send_msg("no pedir datos personales\n")
				sleep(2)
				send_msg("esto no es chat love\n")

			elif line[1].find('http') != -1:
				for u in line[1].split():
					d = search('(.+://)(www.)?([^/]+)(.*)', u)
					if d:
						raw = urlopen(u).read()
						title = search('<title>([\w\W]+)</title>', raw).groups()[0]
						title2 = ''
						for t in title.split('\n'):
							title2 += t.lstrip()+' '
						send_msg("%s en %s\n" % (title2, d.groups()[2]))
            def send_priv(user_send, msg):
			 s.send("PRIVMSG %s :%s\n" %  (user_send, msg))
			if  line[1] == 'sexo':
				send_msg("%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'sexy':
				send_msg("%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'te amo':
				send_msg("%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'kwargs':
				send_msg("kwargs es el lider :v\n")
			if  line[1] == 'telefono':
				send_msg("%s, No pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'tlfn':
				send_msg("%s, no pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'face':
				send_msg("%s, no pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'Gaara':
				send_msg("Gaara es un chico fresa xD\n")
			if  line[1] == 'Freya':
				send_msg("Freya es mi novia\n")
			if  line[1] == 'freya':
				send_msg("Freya es mi novia\n")
			if  line[1] == 'seiso':
				send_msg("%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'novia':
				send_msg("%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'novio':
				send_msg("%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
            if  line[1] == 'novia':
				send_msg("%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'joder':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'joda':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'njd':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'coño':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'csm':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'mierda':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'puta':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'puto':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'pt':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
		    if  line[1] == 'marico':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'mrk':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'mmgb':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
			if  line[1] == 'mmgv':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
				if  line[1] == 'estupida':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)
				if  line[1] == 'estupido':
				send_msg("%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % name)





			if  line[1] == 'Hola Asomao' or line[1] == 'hola Asomao':
				name = line[0].split('!')[0].split(':')[1]
				send_msg("Saludos a ti también %s\n" % name)

			if line[1] == 'ayuda' :
				send_msg("Por favor, dirigirse a los miembros con voice \n")

			if line[1] == '$ ' :
				send_msg("3 Puntos colega\n")

			if line[1] == '$salir' :
				# Change user for you IRC nick
				if line[0].startswith(':user'):
					send_msg("Hasta otra ^^\n")
					exit()
