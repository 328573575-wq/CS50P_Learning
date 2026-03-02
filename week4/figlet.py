import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fontlist = figlet.getFonts()
if len(sys.argv) == 1 :
    figlet.setFont(font=fontlist[random.randrange(0,len(fontlist))])
else :
    try:
        if sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in fontlist:
            raise ValueError
    except ValueError:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])

print(figlet.renderText(input("Input: ")))