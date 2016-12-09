
"""
Script that scrapes weather data from wunderground.com
website format:
    {base}{begindate}{end // customsearch}{enddate}{format=1 // returns csv format}

Script inputs
location code
beginYear
endYear

Scirpt hard-coded to get all daily info for year
"""

import requests
from bs4 import BeautifulSoup


base = "https://www.wunderground.com/history/airport"
end = "CustomHistory.html"

location = 'SCEL'

beginDay = '1' 
beginMonth = '1'
beginYear =  '1996'

endDay = '31'
endMonth = '12'
endYear = '2016'

for year in range(int(beginYear), int(endYear) + 1):
    url ="/".join([base, location, str(year), beginMonth, beginDay, end])
    site = requests.post(url=url, data={'dayend':endDay, 'monthend':endMonth,
                                        'yearend':year, 'format':1})
    soup = BeautifulSoup(site.text, 'html.parser')

    with open('example.txt', 'a') as output:
        output.write(soup.text)
            

