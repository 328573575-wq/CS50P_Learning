def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    n , d = map(int,fraction.strip().split("/"))
    if n < 0 or d < 0 :
        raise ValueError
    if d == 0 :
        raise ZeroDivisionError 
    if n > d :
        raise ValueError
    
    return int(round(n/d*100))
def gauge(percentage):
    if 99 <= percentage :
        return "F"
    elif  percentage <= 1 :
        return "E"
    else :
        return f"{percentage}%"


if __name__ == "__main__":
    main()