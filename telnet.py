#!/usr/bin/python2

import os
import getpass
import argparse as ap
import socket
import commands

parser = ap.ArgumentParser()
parser.add_argument("-s","--send",help = "used to send or connect another system on network")

parser.add_argument("-r","--receive",help = "start receiving connection",action = "store_true")

parser.add_argument("-f","--file",help = "used to send file")

args = parser.parse_args()

def create_socket():
	return socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip=args.send #when we are sender and ip is receiver ip

if args.receive:
	x = create_socket()
	host_name = socket.gethostname()
	rip = socket.gethostbyname(host_name)
	x.bind((rip,9898))
	u_name = x.recvfrom(100)
	u_pass = x.recvfrom(100)
	
	if u_name[0] == 'root' and u_pass[0] == 'redhat':
		x.sendto("Connected Successfully!",u_name[1])
		x.sendto(host_name,u_name[1])
		"""d = commands.getoutput('pwd')
                e = d.split('/')
                cur_dir = e[-1]
                if cur_dir != "root":
			x.sendto(cur_dir,u_name[1])
                else :
			cur_dir == "~"
			x.sendto(cur_dir,u_name[1])
		"""
		try:
			while True:
				cmd = x.recvfrom(100)[0]
				op = commands.getoutput(cmd)
				x.sendto(op,u_name[1])
		except KeyboardInterrupt:		
			print "trl+C Pressed!! Closing Service."
	else:
		x.sendto("Unable to connect. Try again!",u_name[1])

elif args.send:
	x = create_socket()
	u_name = raw_input("Username: ")
	u_pass = getpass.getpass() 	
	x.sendto(u_name,(ip,9898))
	x.sendto(u_pass,(ip,9898))
	status = x.recvfrom(30)
	print status[0]
	host_name = x.recvfrom(100)
	#f = x.recvfrom(100)
	#cur_dir = f[0]
	try:
		while True:
			cmd = raw_input("[root@{} ]# ".format(host_name[0]))
			x.sendto(cmd,(ip,9898))
			print x.recvfrom(10000)[0]
	except KeyboardInterrupt:
		print "trl+C Pressed!! Closing Connection."

		"""
		d = commands.getoutput('pwd')
                e = d.split('/')
                cur_dir = e[-1]
                if cur_dir == "root":
			cur_dir = "~"
		"""
