import os
import subprocess
import re
from tkinter.filedialog import askopenfilename

def osfunction(filepath, checksumtype):
    cmd = "certutil -hashfile \"{0}\" {1}".format(filepath, checksumtype)  # Enclose file path in double quotes for paths with spaces
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout

    checksum_value = None
    if checksumtype.lower() == 'md5':
        checksum_value = re.search(r"([a-fA-F0-9]{32})", output)
    elif checksumtype.lower() == 'sha1':
        checksum_value = re.search(r"([a-fA-F0-9]{40})", output)
    elif checksumtype.lower() == 'sha256':
        checksum_value = re.search(r"([a-fA-F0-9]{64})", output)
    elif checksumtype.lower() == 'sha512':
        checksum_value = re.search(r"([a-fA-F0-9]{128})", output)


    if checksum_value:
        return checksum_value.group(1)
    else:
        return "Checksum value not found."

filepath = askopenfilename()

checksumtype = input("Enter the checksum type (MD5, SHA1, SHA256, SHA512): ").lower()
filechecksum = osfunction(filepath, checksumtype)

checksumvalue = input("Enter the checksum value: ").lower()

if (checksumvalue == filechecksum):
    print("Checksum value verified")
else:
    print("Checksum value not verified")
