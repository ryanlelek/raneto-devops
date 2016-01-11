#!/usr/bin/env python

# Reference: http://stackoverflow.com/questions/15231661/how-do-i-create-a-user-and-set-a-password-using-ansible

# Recommended Install on a Mac
# $ brew install python
# $ pip install passlib

# Import the SHA256 Hash Algorithm
import sys
from passlib.hash import sha256_crypt

# Grab from CLI
if len(sys.argv) != 2:
  print "Please provide one argument: the plain-text password"
  exit()
password = sys.argv[1]

# Want a prompt instead?
# Use this code to get a prompt:
#
# from getpass import getpass
# print "Type your desired password"
# password = getpass()

# Generate a new salt and hash the provided password
hash = sha256_crypt.encrypt(password);

# Report Back
print hash
