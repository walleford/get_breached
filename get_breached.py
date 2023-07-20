from pwn import *
import requests
import sys
import os
import urllib.parse

api_key = os.environ["HIBP_KEY"]

def find_breaches(email):
    s = requests.Session()
    encoded_email = urllib.parse.quote(email)
    print(s.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{encoded_email}?truncateResponse=false', headers={'hibp-api-key':api_key, 'user-agent':'get_breached.py'}).text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Incorrect amount of arguments\n')
        print(f'>> {sys.argv[0]} <email address to search>')
    else:
        email_to_search = sys.argv[1]
        find_breaches(email_to_search)
