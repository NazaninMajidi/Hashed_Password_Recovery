# Hashed Password Recovery using Rainbow Tables

import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Read the CSV file and create a dictionary mapping hashed passwords to usernames
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        hashed_passwords_to_usernames = OrderedDict()
        for row in reader:
            username = row[0]
            hashed_password = row[1]
            hashed_passwords_to_usernames[hashed_password] = username

    # Create a dictionary mapping SHA256 hashes of four-digit passwords to the passwords themselves
    sha256_hashes_to_passwords = OrderedDict()
    sha256_hashes_to_passwords = {hashlib.sha256(str(password).encode('utf-8')).hexdigest(): password for password in range(1000, 10000)}

    # Write the output to a file
    with open(output_file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Username', 'Password'])
        for hashed_password, username in hashed_passwords_to_usernames.items():
            if hashed_password in sha256_hashes_to_passwords:
                password = sha256_hashes_to_passwords[hashed_password]
                writer.writerow([username, password])
    