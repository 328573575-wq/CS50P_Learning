import inflect
eng = inflect.engine()
namelist = []
while True:
    try:
        namelist.append(input("Name: "))
    except EOFError:
        print()
        break
print("Adieu, adieu, to",eng.join(namelist))