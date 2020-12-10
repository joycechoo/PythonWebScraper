import multiprocessing
import schedule
import time
from elasticsearch import Elasticsearch
from database_Core import core
from database_DOAJ import doaj
from database_Unpaywall import unpaywall

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
    
'''def pp():
    for i in range(10):
        print(i)
'''

keywords = 'search.json'

def runThreads(): 
        pcore = multiprocessing.Process(target=core, args=(keywords,))
        pdoaj = multiprocessing.Process(target=doaj, args=(keywords,))
        punpaywall = multiprocessing.Process(target=unpaywall, args=(keywords,))

        start_time = time.time()
        pcore.start()
        pdoaj.start()
        punpaywall.start()

        try: 
            pcore.join()
        except:
            print("Error occured when indexing CORE")
        try: 
            pdoaj.join()
        except:
            print("Error occured when indexing DOAJ")
        try: 
            punpaywall.join()
        except: 
            print("Error occured when indexing Unpaywall")

        es = Elasticsearch()
        es.indices.refresh("amr")
        elasticSearchTotal = es.cat.count("amr")
        print("Total documents indexed (epoch|timestamp|count): ", elasticSearchTotal)
        e = int(time.time() - start_time) 
        print('All processes done')  
        print('Total indexing time: {:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))


if __name__ == '__main__':
    print("Running processes")
    runThreads()
    print("Running the schedule")
    try:
        print(" Will rerun the scrapers at 11:59 PM")
        schedule.every().day.at("23:59").do(runThreads) #Re run the scrapers every 11:59 PM
    except:
        print("Error with scheduling")

    while True: 
        try:
            schedule.run_pending()
            time.sleep(1)
        except:
            print("Error with scheduling")