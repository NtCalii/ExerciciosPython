'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.youtube.com/")
except:
    print("O site youtube não está dísponivel no momento.")
else:
    print("Site acessado com sucesso.")
