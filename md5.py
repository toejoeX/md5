#!usr/bin/python 
#Mass MD5 Password CRACKER

import requests
import sys
from time import time as timer

print "\n"
print "                            _           ___   ___  "
print "                            | |         / _ \ / _ \ "
print "   __ _ _ __   __ _ _ __ ___| |__  _   | (_) | (_) |"
print "  / _` | '_ \ / _` | '__/ __| '_ \| | | \__, |\__, |"
print " | (_| | | | | (_| | | | (__| | | | |_| | / /   / / "
print "  \__,_|_| |_|\__,_|_|  \___|_| |_|\__, |/_/   /_/  "
print "                                    __/ |           "
print "                                   |___/            \n"
print "					Mass MD5 Password CRACKER			"
print "					Coded By : ANARCHY99 				"

def cek(listindex, email, password):
    try:
        kosong = ""
        link = "http://www.nitrxgen.net/md5db/{}".format(str(password))
        r = requests.get(link)
        hasil = email+":"+r.text+"\n"
        res = r.content.decode('utf-8')
        nList.append(hasil)		
        LFile = open("result.txt", "a")
        LFile.write(hasil)
        LFile.close()
        if res not in kosong:
            print("\033[92m")
            print "[-] Found : {0}|{1}".format(str(email),str(res))
        else:
            print("\033[91m")
            print "[-] Not Found {}".format(str(email))
    except:
        pass

md5 = raw_input(" [ - ] List File MD5 Nya : ")
try: 
    list = list(open(md5))
except: 
	print"\n[+] File e Raonok Cok"
	print"\n[+] Cek Maneh ..."
#listindex = 0
nList = []
for line in list:
	try:
		    email = line.split(':')[0]
		    password = line.split(':')[1].replace('\n', '')
		    cek(list.index(line), email, password)
	except:
            print "Format Salah"
            print "Format File Harus Email:Password"
            exit(1)
            
start = timer()        
print('Time: ' + str(timer() - start) + ' seconds')
