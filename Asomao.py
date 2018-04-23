#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Asomao: a IRC bot
# (c) 2018 Leo Hernandez
# (c) 2018 Linel
# Under GPLv3 license

import socket
import string
import sys

from time import sleep
from commands import getoutput
from urllib import urlopen
from re import search, sub

HOST="irc.freenode.net"
PORT=6667
NICK="Asomao1"
IDENT="Asomao"
REALNAME="Asomao IRC"
CHAN="#asomao"
readbuffer=""
track = ''
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHAN)

def send_msg(msg):
        s.send("PRIVMSG %s :%s" % (CHAN, msg))
def send_priv(user_send, msg):
        s.send("PRIVMSG %s :%s\n" %  (user_send, msg))
while 1:
        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        for line in temp:
                line=string.rstrip(line)
                line=line.split(CHAN + ' :')
                username = line[0].split('!')[0].split(':')[1]
                print line
                if line[0].find("PING") != -1:
                        pingid = line[0].split()[1]
                        s.send("PONG %s\r\n" % pingid)

                elif line[0].find('JOIN') != -1:
                        name = line[0].split('!')[0].split(':')[1]
                        if name != NICK and name.find(HOST) == -1:
                                sleep(5)
                                send_msg(% name "Bienvenido al canal oficial en IRC de la comunidad Canaima. Por favor, antes de usar el chat lee nuestras normativas: https://goo.gl/cSYrK8 %s \n")

                if len(line) > 1:
                        print(line[1])
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

                        if  'sexo' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'sexy' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'te amo' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  line[1] in 'telefono':
                                send_priv(username, "%s, No pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'tlfn' in line[1]:
                                send_priv(username, "%s, no pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'face' in line[1]:
                                send_priv(username, "%s, no pedir datos personales, esto no es chat lover ni chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'seiso' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'novia' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'novio' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'novia' in line[1]:
                                send_priv(username, "%s, Esto no es chat lover ni mucho menos chat hispano, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'joder' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if 'joda' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'njd' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'coño' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'csm' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'mierda' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'puta' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'puto' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'pt' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'marico' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'mrk' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'mmgb' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'mmgv' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'estupida' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)
                        if  'estupido' in line[1]:
                                send_priv(username, "%s, Modera tu lenguaje, por favor comportate. normativas: https://goo.gl/cSYrK8\n" % username)





                        if  line[1] == 'Hola Asomao' or line[1] == 'hola Asomao':
                                name = line[0].split('!')[0].split(':')[1]
                                send_msg("Saludos a ti también %s\n" % username)

                        if 'ayuda' in line[1]:
                                send_priv(username, "Por favor, dirigirse a los miembros con voice \n")

                        if line[1] == '$ ' :
                                send_msg("3 Puntos colega\n")

                        if line[1] == '$salir' :
                                # Change user for you IRC nick
                                if line[0].startswith(':linel'):
                                        send_msg("Hasta otra ^^\n")
                                        s.close()
                                        sys.exit(1)
