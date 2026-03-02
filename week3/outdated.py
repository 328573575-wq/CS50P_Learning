months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "," in date:
        try:
            date = date.split(",")
            month , day = date[0].split()
            year , day = map(int,[date[1],day]) 
            month = months.index(month) + 1 
            if 1<=day<=31 and 1<=month<=12:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass
    elif "/" in date:
        try :
            date = date.split("/")
            month ,day ,year = map(int,date)
            if 1<=day<=31 and 1<=month<=12:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass
    else:
        pass