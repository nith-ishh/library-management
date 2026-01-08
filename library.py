# Simple Login System

USERNAME = "admin"
PASSWORD = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("Login successful!")
else:
    print("Invalid username or password.")
