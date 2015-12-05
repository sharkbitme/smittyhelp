#!/usr/bin/env python
"""
This program will either encode or decode email addresses from a line separated email addresses for use with smitty.
The decode is used for measuring click-through on phishing links.

Usage:
  smittyhelp.py <command> <file>
  smittyhelp.py -h | --help
  smittyhelp.py --version
Commands:
	encode	Encodes the target email addresses in hex and outputs a line separated list for use with smitty.
	decode	Decodes the line separated hex-encoded email addresses into a line separated list.
 Options:
   -h, --help       Show this message.
   --version        Print the version.
"""

from docopt import docopt
import binascii
args = docopt(__doc__)

if args ['<command>'] == 'encode':
	def convert_emails(file):
		with open(file, 'r') as email:
			#open the file and start strokin!
			for addr in email:
				ready_addr = addr.rstrip('\n') #strip off the newline chars because, thats cool, man
				hex_addr = binascii.hexlify(ready_addr) #hexlify the email addr
				print(hex_addr)
elif args['<command>'] == 'decode':
	def convert_emails(file):
		with open(file, 'r') as hex_email:
			#opens file because, yeahman
			for encoded_email in hex_email:
				no_line_break_text = encoded_email.rstrip('\n')
				plaintext_addr = binascii.unhexlify(no_line_break_text)
				#strips off newline and then un-hexlifies the email addr
				print(plaintext_addr)
else:
	print "nope"
if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    convert_emails(arguments['<file>'])
