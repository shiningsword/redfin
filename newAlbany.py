from filterListing import filterListing, filterListing2
from send_email import send_notification
import os

# generate executible pyinstaller --onefile newAlbany.py 

zipcode = '43054'
url = f"https://www.redfin.com/school-district/3261/OH/New-Albany-Plain-Local-School-District/filter/property-type=house,max-price=475k,min-beds=3"
filename = "/Users/shiningsword/Projects/redfin/new_Albany.log"
if os.path.exists(filename):
    log = open(filename, "a+")
else:
    log = open(filename, "w") 
text = filterListing2(url, zipcode, log, "/OH/New-Albany")
if text is not None:
    send_notification("New Albany founded property:\n"+ text)
log.close()