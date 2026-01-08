import re

# Input: comma separated passwords
passwords = input().split(",")

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()   # remove extra spaces

    if (6 <= len(pwd) <= 12 and
        re.search("[a-z]", pwd) and
        re.search("[A-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        
        valid_passwords.append(pwd)

# Output valid passwords separated by comma
print(",".join(valid_passwords))
import re

# Input: comma separated passwords
passwords = input().split(",")

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()   # remove extra spaces

    if (6 <= len(pwd) <= 12 and
        re.search("[a-z]", pwd) and
        re.search("[A-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        
        valid_passwords.append(pwd)

# Output valid passwords separated by comma
print(",".join(valid_passwords))
