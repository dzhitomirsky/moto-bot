import requests
from lxml import html
import time
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch():
    logger.info("Fetching data about motos...")
    response_data = requests.post('https://mb.onliner.by/search', data = {
                                    'min-year':2000,
                                    'min-capacity': 800,
                                    'engine_configuration[]': 1,
                                    'drivetrain[]': 1,
                                    'currency': 'USD',
                                    'sort[]':'creation_date',
                                    'page':1,
                                    'type[0][1]':''
                                    }, headers = {
                                    'Accept': 'application/json'
                                    }).json()
    if response_data['success']:
        logger.info("Successfully fetched data. Starting data aggregation...")
        current_unix_date = int(time.time())
        was_updated_hrs_ago = []

        for update_time in sorted(response_data['result']['counters']['update_date'].keys(), reverse=True):
            update_delta = (current_unix_date - int(update_time)) / 3600
            if(update_delta < 30):
                was_updated_hrs_ago.append(update_delta)
            else:
                break

        new_position_ids = [td.get('id').replace("moto_","") for td in html.fromstring(response_data['result']['content']).xpath("//tr[contains(@id,'moto_')]")[:len(was_updated_hrs_ago)]]
        logger.info("Data aggregation is done.")

        moto_data = zip(new_position_ids, was_updated_hrs_ago, ["https://mb.onliner.by/moto/" + id for id in new_position_ids])
        return moto_data
    else:
        logger.warning("Somthing gone wrong: cant fetch data from onliner...")
        return []

if __name__ == '__main__':
    fetch()
