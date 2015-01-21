import re
import urllib2
from bs4 import BeautifulSoup

def total(soup, dt):
	"""find the domestic total for the movie
		soup: soup object
		dt: dictionary """
	
	keys = ['Worldwide', 'Domestic']
	for i in range(len(keys)):
		raw_total = (soup.find(text=re.compile(keys[i])).find_next()).text
		raw_total = raw_total.replace('$', '').replace(',','')
		raw_total = int(raw_total)
		raw_total = raw_total/1000000.0
		dt[keys[i]] = raw_total
	
	return dt

def genre(soup, dt):
	"""find a genre for a movie"""
	
	genre = soup.find(text=re.compile('Genre:')).findNextSibling().text
	genre = genre.split('/')
	
	dt['genre'] = genre
	
	return dt

def budget(soup, dt):
	"""find the production budge"""
	
	production_budget = soup.find(text=re.compile('Production Budget'))
	production_budget = production_budget.findNextSibling().text
	production_budget = production_budget.replace('$', '')
	production_budget = production_budget.split(' ')

	dt['Production Budget'] = production_budget[0]
	
	return dt

def runTime(soup, dt):
	"""convert movie runtimes to minutes"""

	return dt

def main():

	#url="http://www.boxofficemojo.com/yearly/?view2=domestic&view=releasedate&p=.htm"
	stats = {}
	page = urllib2.urlopen("http://www.boxofficemojo.com/movies/?id=marvel2014a.htm")
	soup = BeautifulSoup(page)
	stats = total(soup, stats)
	stats = genre(soup, stats)
	stats = budget(soup, stats)
	
	print stats

if __name__ == '__main__':
	main()
