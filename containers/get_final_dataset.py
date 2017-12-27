import csv
import json

with open('final_data.csv', 'wb') as csvfile:
        fieldnames = ['origin_country','destination_country', 'rate_20_ft', 'rate_40_ft']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        australia = open('rates-freight-costs-australia.json', 'rb')
        data = json.load(australia)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "Australia (Sydney)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})

        uk = open('rates-freight-costs-uk.json', 'rb')
        data = json.load(uk)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "United Kingdom (London)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})

        east_canada = open('rates-freight-costs-canada-0.json', 'rb')
        data = json.load(east_canada)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "Eastern Canada (Montreal)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})

        west_canada = open('rates-freight-costs-canada-1.json', 'rb')
        data = json.load(west_canada)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "Western Canada (Vancouver)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})

        east_usa = open('rates-freight-costs-usa-0.json', 'rb')
        data = json.load(east_usa)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "Eastern United States (New York)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})

        west_usa = open('rates-freight-costs-usa-1.json', 'rb')
        data = json.load(west_usa)
        for p in data:
            if len(p)==0:
                pass
            else:
                writer.writerow({'origin_country': "Western United States (Los Angeles)",'destination_country': p[0], 'rate_20_ft': p[1], 'rate_40_ft': p[2]})
