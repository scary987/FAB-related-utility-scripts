import requests 
import json
import urllib.request
import csv
def getFilename_fromCd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

sets = [
    "WTR",
    "ARC",
    "CRU",
    "MON",
    "ELE",
    "EVR"
    "RVD",
    "DVR",
    "UPR"
 ] 


fabdb_api = "https://api.fabdb.net"
class_ = "wizard"

cardlistfile = "cardlist.csv"
with open(cardlistfile,"w") as output:
    csv_out=csv.writer(output)
    csv_out.writerow(['name','set','rarity', 'stats','keywords', 'image link'])
    for code in sets:
        url_ = fabdb_api+f"/cards?set={code}&per_page=100&class={class_}"
        counter = 0
        while True:
            resp = requests.get(url_)
            print(resp.text)
            json_dic = json.loads(resp.text)
            print("rofl")
            for num,card in enumerate(json_dic['data']):
                image_url = card['image']
                
                card_name = card['name']
                card_rarity = card['rarity']
                card_keywords = card['keywords']
                card_stats = card['stats']
                with open(cardlistfile,"a") as output:
                    row = (card_name,code,card_rarity, card_stats,card_keywords,image_url,)
                    csv_out.writerow(row)

                
                if ('dragon' in card['keywords'] and 'ally' in card['keywords']) or 'dragon ally' in card['keywords']: #its an uprising dragon
                    cardcode_back = f"{code}{'{:03d}'.format(counter-1+400)}" 
                    # handle the back of an invocation as the same, but +400 for an unique indentifier   
                                                               


                    # DOWNLOAD IMAGES
                    #urllib.request.urlretrieve(
                    #    image_url, 
                    #    f"{cardcode_back}.jpg")
                    print(cardcode_back)
                    continue
                cardcode = f"{code}{'{:03d}'.format(counter)}"
                #urllib.request.urlretrieve(
                #    image_url, 
                #    f"{cardcode}.jpg")
                print(cardcode)
                counter+=1
            if json_dic['links']['next']!= None:
                url_ = fabdb_api+json_dic['links']['next']
                continue

            else:
                break




    