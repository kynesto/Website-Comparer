import requests
from bs4 import BeautifulSoup


class Website2Text:

   def get(self, URL):
      r = requests.get(URL)
      page = r.text
      
      soup = BeautifulSoup(page, 'html.parser')
      return soup.get_text()
      # return soup.find('p').getText()
