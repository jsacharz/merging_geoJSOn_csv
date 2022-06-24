import geojson
import pandas as pd
import csv

with open('Boundry2.geojson') as f:
    geo_json_suburbs = geojson.loads(f.read())

with open('clean_avg_melb_sales.csv') as csv_file:
    melb_house_avg_sales = []
    melb_avg_sales = csv.reader(csv_file)
    for row in melb_avg_sales:
        melb_house_avg_sales.append(row)

# matching_suburbs = {}

for suburb in geo_json_suburbs['features']:
    for row in melb_house_avg_sales[1:]:
        if suburb['properties']['vic_loca_2'].lower() == row[1].lower():
            print(suburb['properties']['vic_loca_2'], row)
            if not row[3]:
                suburb['properties']['mean_price'] = 'NA'
            else:
                suburb['properties']['mean_price'] = row[3]
            # matching_suburbs[suburb['properties']['vic_loca_2'].lower()] = {
            #     'suburb': row[1],
            #     'postcode': row[2],
            #     'mean_price': row[3],
            #     'geo_json': suburb
            # }
        # else:
        #     suburb['properties']['mean_price'] = 'NA'

for suburb in geo_json_suburbs['features']:
    if 'mean_price' not in suburb['properties'].keys():
        suburb['properties']['mean_price'] = 'NA'

pass

with open('geo_json_mean_price_dump', 'w') as f:
    f.write(geojson.dumps(geo_json_suburbs, sort_keys=True))