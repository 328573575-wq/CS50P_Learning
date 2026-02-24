def main() :
    m = int(input("m: "))
    result = calculate(m)
    print(f"E: {result}")
def calculate(m) : 
    c = 300000000
    return m*pow(c,2)
main()