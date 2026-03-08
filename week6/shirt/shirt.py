import sys
from os import path
from PIL import Image
from PIL import ImageOps
def main():
    if len(sys.argv) != 3 :
        sys.exit("Invalid arguments.1")
    end_1 = path.splitext(sys.argv[1])
    end_2 = path.splitext(sys.argv[2])
    types = (".jpg",".jpeg",".png")
    if end_1[1] not in types or end_2[1] not in types or end_2[1] != end_1[1]:
        sys.exit("Invalid arguments.2")
    try :
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        before = ImageOps.fit(before,shirt.size)
        before.paste(shirt,mask=shirt)
        before.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("file not found")
if __name__ == "__main__":
    main()