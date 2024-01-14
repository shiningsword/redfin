from filterListing import filterListing
from send_email import send_notification
import os

zipcode = '96761'
url = f'https://www.redfin.com/zipcode/{zipcode}/filter/property-type=condo,max-price=800k'
filename = "/Users/shiningsword/Projects/redfin/maui.log"
if os.path.exists(filename):
    log = open(filename, "a+")
else:
    log = open(filename, "w") 
text = filterListing(url, zipcode, log)
if text is not None:
    send_notification("Maui founded property:\n"+ text)
log.close()