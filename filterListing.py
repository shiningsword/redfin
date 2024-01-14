import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
import time
import random
from datetime import datetime

def check_listing(list_url):
    print(f"checking {list_url} ...")
    url = "https://www.redfin.com" + list_url
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    fee_simple = False
    short_term = True
    for item in soup.findAll('span', class_="entryItemContent"):
        if item.text.startswith("Lease Terms"):
            fee_simple = (item.find("span").text == "Fee Simple")
        if item.text.startswith("Short Term Rental"):
            short_term = (item.find("span").text == "Yes")
    return fee_simple, short_term

class ListingRecord:
    def __init__(self, path="listing_record.txt"):
        self.path = path
        if os.path.exists(path):
            with open(path, "r") as file:
                data = file.read()
                data_into_list = data.split("\n")[:-1]
            self.data = set(data_into_list)
        else:
            self.data = set()
    
    def write_set(self, set_urls):
        with open(self.path, "w") as file:
            for url in set_urls:
                file.write(url + "\n")
        print(f"checked list writing to {self.path}")

def filterListing(url, zipcode, log):
    log.writelines(f"listing checked {datetime.now()} \n")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    listing_record = ListingRecord(f"/Users/shiningsword/Projects/redfin/{zipcode}.txt")
    checked_urls = set(listing_record.data)
    return_text=""
    found= False
    for one_a_tag in soup.findAll('a'): #'a' tags are for links
        if one_a_tag.has_attr("href") and one_a_tag["href"].startswith("/HI/"):
            property_url = one_a_tag["href"]
            if property_url in checked_urls:
                continue
            fee_simple, short_term = check_listing(property_url)
            checked_urls.add(property_url)
            if fee_simple and short_term:
                found = True
                text = f"find a property https://redfin.com{property_url}\n" 
                print(text)
                log.write(text)
                return_text = return_text + text
            time.sleep(random.randint(10,30))

    listing_record.write_set(checked_urls)
    if found:
        return return_text
    else:
        return None
    
def filterListing2(url, zipcode, log, prefix):
    log.writelines(f"listing checked {datetime.now()} \n")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    listing_record = ListingRecord(f"/Users/shiningsword/Projects/redfin/{zipcode}.txt")
    checked_urls = set(listing_record.data)
    return_text=""
    found= False
    for one_a_tag in soup.findAll('a'): #'a' tags are for links
        if one_a_tag.has_attr("href") and one_a_tag["href"].startswith(prefix):
            property_url = one_a_tag["href"]
            if property_url in checked_urls:
                continue
            checked_urls.add(property_url)
            found = True
            text = f"find a property https://redfin.com{property_url}\n" 
            print(text)
            log.write(text)
            return_text = return_text + text
            
    listing_record.write_set(checked_urls)
    if found:
        return return_text
    else:
        return None