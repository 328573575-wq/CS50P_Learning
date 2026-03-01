def get_num():
    while True:
        try:
            return int(input())
        except ValueError:
            pass
def main():
    print("x is",get_num())
main()