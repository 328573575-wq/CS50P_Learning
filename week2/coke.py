def main() :
    coins = 50 
    while True :
        print(f"Amount Due: {coins}")
        insert = int(input("Insert Coin: ")) 
        coins -= insert if insert in [25,10,5] else 0

        if coins <= 0 :
            print("Change Owed:",abs(coins))
            break
main()