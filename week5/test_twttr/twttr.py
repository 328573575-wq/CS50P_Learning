def main() :
    ans = shorten(input("Input: ").strip())
    print("Output:",ans)
def shorten(word):
    return "".join(["" if s.lower() in "aeiou" else s for s in word ])

if __name__ == "__main__":
    main()