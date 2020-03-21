import requests
from bs4 import BeautifulSoup

"""
a program to retrieve the number of global as well as US cases of coronavirus.

@author Chris Schulz
3/21/2020
"""

html_text = requests.get('https://www.worldometers.info/coronavirus/')
bs = BeautifulSoup(html_text.text, 'html.parser')

global_cases = bs.select('.maincounter-number')[0].get_text().strip('\n')
global_deaths = bs.select('.maincounter-number')[1].get_text().strip('\n')

print("\nGlobal coronavirus cases: " + global_cases)
print("Global coronavirus deaths: " + global_deaths)

html_text = requests.get('https://www.worldometers.info/coronavirus/country/us/')
bs = BeautifulSoup(html_text.text, 'html.parser')

us_cases = bs.select('.maincounter-number')[0].get_text().strip('\n')
us_deaths = bs.select('.maincounter-number')[1].get_text().strip('\n')

print("\nUS coronavirus cases: " + us_cases)
print("US coronavirus deaths: " + us_deaths)
