item = {}
def main() :
    getitem()
    ans = sorted(item)
    for o in ans :
        print(item[o],o.upper())

def getitem() :
    while True:
        try:
            x = input()
        except EOFError:
            break
        if x in item :
            item[x] += 1
        else :
            item[x] = 1 
main()