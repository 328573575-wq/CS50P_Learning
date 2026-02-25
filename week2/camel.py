def main() :
    s = input("camelCase: ")
    s = convert(s)
    print(f"snake_case: {s}")
def convert( s ) :
    st = ""
    for c in s :
        if (c.isupper()) :
            c = c.lower()
            st+="_"
        st += c
    return st 
main()