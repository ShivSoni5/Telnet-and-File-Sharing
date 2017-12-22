#!/usr/bin/python2

import os
import getpass
import argparse as ap
import socket
import sys

parser = ap.ArgumentParser()
parser.add_argument("-s","--send",help = "used to send or connect another system on network")

parser.add_argument("-r","--receive",help = "start receiving connection",action = "store_true")

parser.add_argument("-f","--file",help = "used to send file")

args = parser.parse_args()

def create_socket():
	return socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip=args.send #when we are sender and ip is receiver ip

if args.receive:
	x=create_socket()
	a=socket.gethostname()
	rip=socket.gethostbyname(a)
	x.bind((rip,9898))
	p=x.recvfrom(100)
	print p

elif args.send:
	x=create_socket()
	x.sendto("hey shiv",(ip,9898))
