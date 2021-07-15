#!/bin/python3

# pip install --user pyshorteners

import os
import pyshorteners

os.system('clear')
url = input('Cole a url aqui:\n\n')
s = pyshorteners.Shortener()
shortUrl = s.tinyurl.short(url)
print(f'\nUrl encurtada: {shortUrl}')
