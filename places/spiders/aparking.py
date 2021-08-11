import scrapy
import time

from items import GeojsonPointItem
from settings import WAREHOUSE, FEED_EXPORTERS

class AparkingSpider(scrapy.Spider):
    name = 'aparking'
    allowed_domains = ['aparking.kz']
    start_urls = ['https://old.aparking.kz/admin/terminals.php']
    current_time = round(time.time())
    
    custom_settings = {
        'FEEDS': {
            f'{WAREHOUSE}/{name}-{current_time}.geojson': {
                "format": "geojson", 
                'encoding': 'utf8'
            },
            f'{WAREHOUSE}/{name}-{current_time}.csv': {
                'format': 'csv', 
                'encoding': 'utf8'
            },
        },
        'FEED_EXPORTERS': FEED_EXPORTERS,
        'FEED_EXPORT_FIELDS': [
            'ref',
            'brand',
            'addr_full',
            'housenumber',
            'street',
            'city',
            'country',
            'postcode',
            'website',
            'email',
            'lat',
            'lon',
        ],
    }


    def parse(self, response):
        data = response.json()['data']

        for row in data:
            item = GeojsonPointItem()

            postcode = row.get('mail_index')
            country = 'Kazakhstan'
            street = row.get('street')
            city = row.get('city')
            housenumber = row.get('house_number')

            item['ref'] = row.get('terminal_id')
            item['brand'] = 'Aparking'
            item['addr_full'] = f'{postcode},{country},{city},{street},{housenumber}'
            item['street'] = street
            item['housenumber'] = housenumber
            item['city'] = city
            item['postcode'] = postcode
            item['country'] = country
            item['website'] = 'https://aparking.kz/'
            item['email'] = 'pr@aparking.kz'
            item['lat'] = row.get('placemarkCoords')[0]
            item['lon'] = row.get('placemarkCoords')[1]

            yield item