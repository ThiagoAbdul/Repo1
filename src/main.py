import os

def bravo(func):
    return lambda: func().upper()

connection_strings = "<secret>"

def connect():
    print("Conectado")


@bravo
def hello():
    lang = os.environ.get('LANG')

    if lang is not None:
        lang = lang.lower()
        hellos = {
            'pt-br': 'Ola, mundo',
            'en': 'Hello, world' 
        }

        if lang in hellos:
            return hellos[lang]
    return '?'

connect()
print(hello())
