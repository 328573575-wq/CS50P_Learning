import re
email = input()
if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("valid")
else :
    print("invalid")