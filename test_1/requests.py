import requests
import sys
import json
if len(sys.argv) != 2 :
    sys.exit()
o = (requests
     .get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
     .json() 
     )
for i in o["results"] :
    print(i["trackName"])
