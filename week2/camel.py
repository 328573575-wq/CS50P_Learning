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

"""
列表推导式
camel = input("camelCase: ").strip()
snake = "".join(["_" + ch.lower() if ch.isupper() else ch for ch in camel])
print(f"snake_case: {snake}")
"""