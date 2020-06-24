from bs4 import BeautifulSoup
import requests

headers = { 
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
  'Accept-Language' : 'en-US,en;q=0.5',
  'Accept-Encoding' : 'gzip', 
  'DNT' : '1', # Do Not Track Request Header 
  'Connection' : 'close'
}

def summary():
  resp = requests.get('http://ibdfam.org.br/covid19/summary', headers=headers)
  soup = BeautifulSoup(resp.content, 'html.parser') 

  return {
      "TotalConfirmed" : soup.find('span', {'id' : 'totalConfirmed'}).text,
      "TotalDeaths" : soup.find('span', {'id' : 'TotalDeaths'}).text,
      "TotalRecovered" : soup.find('span', {'id' : 'TotalRecovered'}).text
  }

def country(country):
  resp = requests.get('http://ibdfam.org.br/covid19/country/'+country, headers=headers)
  soup = BeautifulSoup(resp.content, 'html.parser') 

  return {
      "TotalConfirmed" : soup.find('span', {'id' : 'totalConfirmed'}).text
  }


print(summary())
#Today's date: 2020-06-24
#{'TotalConfirmed': '9366512', 'TotalDeaths': '486079', 'TotalRecovered': '4630051'}

print(country("brazil"))
#Today's date: 2020-06-24
#{'TotalConfirmed': '1145906'}

