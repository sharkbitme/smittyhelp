#!/usr/bin/env python
"""
This program will either encode or decode email addresses from a line separated email addresses for use with smitty.
The decode is used for measuring click-through on phishing links.

Usage:
  smittyhelp.py <command> <file>
  smittyhelp.py -h | --help
  smittyhelp.py --version
Commands:
    encode    Encodes the target email addresses in hex and outputs a line separated list for use with smitty.
    decode    Decodes the line separated hex-encoded email addresses into a line separated list.
 Options:
   -h, --help       Show this message.
   --version        Print the version.
"""

import binascii

from docopt import docopt


def convert_emails(filename, method):
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n').encode("utf-8")
            if method == 'encode':
                yield binascii.hexlify(line).decode("utf-8")
            elif method == 'decode':
                yield binascii.unhexlify(line).decode("utf-8")


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    method = arguments['<command>'].lower()

    if method not in ('encode', 'decode'):
        print("nope")
    exit(1)
    for line_out in convert_emails(arguments['<file>'], method):
        print(line_out)
