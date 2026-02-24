def main() :
    st = (
          input("What is the Answer to the Great Question of Life, the Universe and Everything?")
          .strip()
          .lower()
          )
    if st == "42" or st == "forty-two" or st == "forty two" :
        print("Yes")
    else :
        print("No")

main()