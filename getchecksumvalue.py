import os
import subprocess
import re
from tkinter.filedialog import askopenfilename

def osfunction(filepath, checksumtype):
    checksum_patterns = {
        'md5': r"([a-fA-F0-9]{32})",
        'sha1': r"([a-fA-F0-9]{40})",
        'sha256': r"([a-fA-F0-9]{64})",
        'sha512': r"([a-fA-F0-9]{128})"
    }

    cmd = f"certutil -hashfile \"{filepath}\" {checksumtype}"  # Enclose file path in double quotes for paths with spaces
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout

    checksum_value = re.search(checksum_patterns.get(checksumtype.lower(), ""), output)

    if checksum_value:
        return checksum_value.group(1)
    else:
        return "Checksum value not found."

filepath = askopenfilename()

for checksumtype in ['md5', 'sha1', 'sha256', 'sha512']:
    print(f"{checksumtype} -> {osfunction(filepath, checksumtype)}")

