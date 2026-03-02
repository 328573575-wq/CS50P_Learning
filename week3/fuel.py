while True: 
    try :
        n , d = map(int,input("Fraction: ").strip().split("/"))
        if n < 0 or d < 0 :
            raise ValueError
        if n > d :
            raise ValueError
        if d == 0 :
            raise ZeroDivisionError 
        break
    except (ZeroDivisionError,ValueError) :
        pass
re = round(n/d * 100) 
if 99 <= re :
    print("F")
elif  re <= 1 :
    print("E")
else :
    print(f"{re}%")

