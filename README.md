
# Checksum tester

This tool is designed to verify the integrity of a file using checksums. It calculates the checksum value for the selected file based on the specified hash algorithm (MD5, SHA-1, SHA-256, or SHA-512) and then compares it to the user-provided checksum value. If the two values match, the file integrity is confirmed, otherwise, it raises an integrity warning.


## How to use

 - Run the script in a Python environment.
 - You will be prompted to select the file you want to verify.
 - Enter the desired checksum type (MD5, SHA1, SHA256, or SHA512) for the file.
 - The script will calculate the checksum value for the selected file based on the chosen algorithm.
 - Enter the checksum value you received from a trusted source for the same file.
 - The tool will compare the calculated checksum with the provided checksum.
 - If the two checksums match, it will display "Checksum value verified," confirming the file's integrity.
 - If the checksums do not match, it will display "Checksum value not verified," indicating a potential integrity issue.


## Example usage

```bash
$ python checksum_verification_tool.py

[File Selection Dialog Appears]
Enter the checksum type (MD5, SHA1, SHA256, SHA512): sha256
Enter the SHA256 checksum value: e35a5b687a2c7d5e8f4b647b55b91db6604d3368455016a3210f1b6072390b4c
SHA256 Checksum value verified

```


## Supported Hash Algorithms

- MD5
- SHA-1
- SHA-256
- SHA-512

## Requirements

- Python 3.x
- tkinter module


## Note

This tool is meant for basic integrity verification purposes. For more robust security requirements, consider using cryptographic libraries and protocols. Always obtain checksum values from trusted sources to ensure the authenticity of the verification process.
