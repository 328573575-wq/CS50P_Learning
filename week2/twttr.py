def main() :
    st = input("Input: ").strip()
    ans = "".join(["" if s.lower() in "aeiou" else s for s in st ])
    print("Output:",ans)
main()