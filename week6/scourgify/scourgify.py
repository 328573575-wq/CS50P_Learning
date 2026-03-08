import sys
import csv
def main():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv") :
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as file_1, open(sys.argv[2],"w",newline="") as file_2:
            reader = csv.DictReader(file_1)
            writer = csv.DictWriter(file_2,["first","last","house"])
            writer.writeheader()
            for line in reader :
                last,first = line["name"].strip().split(", ")
                writer.writerow({"first":first,"last":last,"house":line["house"]})
    except FileNotFoundError:
        sys.exit(f"File does not exist.")
if __name__ == "__main__":
    main()