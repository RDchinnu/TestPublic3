import os

print("Jenkins credential")

username = os.getenv('username')
password = os.getenv('password')

print('username', username)
print('password', password)