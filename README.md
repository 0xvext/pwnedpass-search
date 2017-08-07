# pwnedpass-search
A python script to perform offline searches against the haveibeenpwned hash list(s), or similar

Initial version to make use of the hash files released by @troyhunt on https://www.haveibeenpwned.com 2017.08.03.

Use requires text file(s) containing SHA-1 hashes, one per line, of password strings in one or more text files. Based on the files available for download at https://haveibeenpwned.com/Passwords

Currently Python 2 compatible.


Usage:
python ./pwnedpass-search.py <dictionary file(s) containing SHA-1 hashes>

When prompted, enter a plaintext password string. Output will confirm if the SHA-1 hash of that string was found or not.


Example:

(In folder with text files described above)
python ./pwnedpass-search.py pwned-passwords-*.txt


Output:

```===============================================================
pwnedpass-search.py  Copyright (C) 2017  vext
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the GNU GPL for details.
===============================================================

Password to parse for:

SHA1 hash of password: F2F7D2A4E7C1D1FCC4EF7E7968586C99AADE8B5B

Searching. This could take a few minutes...

[!] Hashed pass found: F2F7D2A4E7C1D1FCC4EF7E7968586C99AADE8B5B
[!] Found in file: pwned-passwords-1.0.txt

Done.
```



Possible features to add:
  Colors
  Cleaner newline (replace \n) method
  Prompt user whether to perform another search yes/no at end
  Translate to python 3

Pull requests welcome.
