import random

def main():
    lev = get_level()
    score = 0
    for _ in range(10) :
        x , y = generate_integer(lev) , generate_integer(lev)
        result = x + y
        score += play(x,y,result)
        
    print(f"Score: {score}")


def get_level():
    while True:
        try:        
            res = int(input("Level: "))
            if res not in [1,2,3] :
                raise ValueError
            break
        except ValueError:
            pass
    return res

def generate_integer(level):
    if level == 1 :
        return random.randint(0,9)
    else :
        return random.randint( 10**(level - 1) , 10**level - 1 )

def play( x , y , result) :
    counts = 0
    while counts < 3:
        try:
            ans = int(input(f"{x} + {y} = "))
        except ValueError:
                print("EEE")
                counts += 1
                continue
        if ans != result :
            print("EEE")
            counts += 1
        else :
            break

    if counts == 3 :
        print(f"{x} + {y} = {result}")
        return 0
    return 1
    
if __name__ == "__main__":
    main()