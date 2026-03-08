import sys
import csv
from tabulate import tabulate
pizza_list = []
def main():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") :
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for line in reader :
                pizza_list.append(line)
    except FileNotFoundError:
        exit("File does not exist")
    print(tabulate(pizza_list,headers="keys",tablefmt="grid"))
if __name__ == "__main__":
    main()