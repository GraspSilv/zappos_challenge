# ProductGroup.py
import requests
import json
import random
from decimal import Decimal


myKey = "&key=52ddafbe3ee659bad97fcce7c53592916a6bfd73"
search = "http://api.zappos.com/Search/term/"
limit = "?limit=1000"
product_search = "http://api.zappos.com/Product?id="
terms = ["shoes", "bags", "clothing", "beauty", "accessories", "home"]

class ProductGroup:
	def __init__(self, num_items, max_spent):
		self.itemCount = num_items
		self.maxPrice = Decimal(max_spent)
		self.totalSpent = Decimal(0)
		self.items = []

	def addOne(self,item):
		self.items.append(item)

	def printAllByKey(self,key):
		for item in self.items:
			print item[key]

	def populateOne(self,spacing):
		if (self.itemCount - len(self.items) == 0):
			return 0
		if (self.itemCount - len(self.items) == 1):
			spacing = 1
		targetPrice = Decimal(spacing) * (self.maxPrice - self.totalSpent) / (self.itemCount - len(self.items))
		call = search + random.choice(terms) + limit + myKey
		print "calling"
		print len(self.items)
		r = requests.get(call)
		data = json.loads(r.text)

		counter = len(data['results']) - 1
		while counter > 0:
			current = random.choice(data['results'])
			# current = data['results'][counter]
			price = Decimal(current['price'].strip('$'))
			if price <= targetPrice and self.maxPrice > (self.totalSpent + price):
			# if (abs(targetPrice - price) < 3) and self.maxPrice > (self.totalSpent + price):
				self.items.append(current)
				self.totalSpent += price
				# print current
				return True
			counter -= 1
		return False

	def populateAll(self):
		while self.itemCount > len(self.items):
			# print "ok"
			if self.populateOne(random.uniform(.6,1.9)) == False and len(self.items) > 0:
				self.totalSpent -= Decimal(self.items.pop()['price'].strip('$'))

		if (self.maxPrice > self.totalSpent + 5):
			self.items = []
			self.totalSpent = 0
			return False

		return True
