import g4f
#import tkinter as tk
import os
import sys
print(os.getcwd())
print(sys.executable)

g4f.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking

#print(g4f.version) # check version
#print(g4f.Provider.Ails.params)  # supported args


while True:
    print()
    ask=input("gpt-3.5-turbo слушает : ")
    if ask=="стоп" :
        break
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": ask}],
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
