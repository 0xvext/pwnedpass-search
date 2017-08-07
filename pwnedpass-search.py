#!/usr/bin/env python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import getpass
import hashlib
import fileinput
import sys

print """
===============================================================
pwnedpass-search.py  Copyright (C) 2017  vext
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the GNU GPL for details.
===============================================================
"""

#Declare object to contain the SHA1 hash of the entered password.
passhash = hashlib.sha1()

#Prompt the user to enter a password and store the value.
passhash.update(getpass.getpass("Password to parse for:"))

#Output the (uppercase) hash stored above and user-friendly output.
print "\nSHA1 hash of password:" + " " + passhash.hexdigest().upper()
print "\nSearching. This could take a few minutes..."

#Loop through the file(s) passed as CLI parameter(s).
for line in fileinput.input():
        #If line in file contains hash.
        if passhash.hexdigest().upper() in line:
                #When true, print the hash, the document and exit.
                print "\n[!] Hashed pass found:" + " " + line,
		print "[!] Found in file: " + fileinput.filename()
                print "\nDone."
                sys.exit()

#Output hash not found.
print "\n[-] Hashed pass not found."
print "\nDone."
