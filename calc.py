import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while 1:
    hello = input(">>> ")
    if hello == "clear".lower():
        clear()
    elif hello == "quit".lower():
        quit()
    else:
        try:
            print(eval(hello))
        except Exception as e:
            print("", end="")
