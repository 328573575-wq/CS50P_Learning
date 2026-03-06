import csv
name = input()
region = input()
with open("name.csv","a",newline="") as file :
    writer = csv.DictWriter(file,fieldnames=["name","region"])
    writer.writerow({"name":name,"region":region})