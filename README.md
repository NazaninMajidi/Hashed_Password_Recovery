# Hashed_Password_Recovery
This code is a Python script that recovers hashed passwords using rainbow tables. It takes two arguments: an input file name (a CSV file with usernames and hashed passwords) and an output file name (another CSV file to which the recovered usernames and passwords will be written).

## Dependencies
* Python 3.x
* hashlib
* csv
* collections

## How it works
The script reads the input CSV file and creates an ordered dictionary `hashed_passwords_to_usernames` that maps hashed passwords to usernames. It then generates another ordered dictionary `sha256_hashes_to_passwords` that maps SHA256 hashes of four-digit passwords to the passwords themselves.

Next, the script writes the output to a file. For each hashed password in `hashed_passwords_to_usernames`, the script checks if the hashed password exists in `sha256_hashes_to_passwords`. If there is a match, it retrieves the corresponding password and writes the username and password to the output CSV file.

## Usage
To use this script, you need to provide an input file name and an output file name.

For example, to recover the passwords from an input file named `passwords.csv` and write the results to an output file named `recovered_passwords.csv`, you can do the following:

```python linenos
hash_password_hack('passwords.csv', 'recovered_passwords.csv')
```

The output CSV file will have two columns: `Username` and `Password`.
