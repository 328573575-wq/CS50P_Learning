import random
while True :
    try:
        level = int(input("Level: "))
        ans = random.randint(1,level)
        break
    except ValueError:
        pass
while True : 
    try:
        res = int(input("Guess: "))
        if res <= 0 :
            raise ValueError
    except ValueError:
        continue
    if ans<res:
        print("Too large!")
    elif res<ans:
        print("Too small!")
    else:
        print("Just right!")
        break
