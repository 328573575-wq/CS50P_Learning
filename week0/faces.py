def main() :
    st = input()
    ans = convert(st)
    print(ans)
def convert(a) :
    a = a.replace(":)","\U0001F642").replace(":(","\U0001F641")
    return a
main()