# ProductGroup.py
import requests
import json
import random
from decimal import Decimal


myKey = "&key=52ddafbe3ee659bad97fcce7c53592916a6bfd73"
search = "http://api.zappos.com/Search/term/"
limit = "?limit=1000"
page = "&page="
product_search = "http://api.zappos.com/Product?id="
terms = ["shoes", "bags", "clothing", "beauty", "accessories", "home"]

class ProductGroup:
	def __init__(self, num_items, max_spent):
		self.itemCount = num_items
		self.maxPrice = Decimal(max_spent)
		self.totalSpent = Decimal(0)
		self.items = []
		self.products = []
		self.counter = 0

	def addOne(self,item):
		self.items.append(item)

	def returnOneByProductName(self,name,key):
		for item in self.items:
			if item["productName"] == name:
				return item[key]

	def printAllByKey(self,key):
		for item in self.items:
			print item[key]

	def returnAllByKey(self,key):
		info = []
		for item in self.items:
			info.append(item[key])
		return info

	def getResultsFromAPI(self):
		call = search + random.choice(terms) + limit + page + str(random.randint(1,5)) + myKey
		print "calling"
		print len(self.items)
		r = requests.get(call)
		data = json.loads(r.text)
		self.counter = len(data['results']) - 1
		return data


	def populateOne(self,data):

		if (self.itemCount - len(self.items) == 0):
			return True

		targetHigh = Decimal(2) * (self.maxPrice - self.totalSpent) / (self.itemCount - len(self.items))
		targetLow = Decimal(.5) * (self.maxPrice - self.totalSpent) / (self.itemCount - len(self.items))
		# print targetHigh
		# print targetLow
		# print "==========="
		
		while self.counter > 0:
			current = random.choice(data['results'])
			# print current
			# current = data['results'][self.counter]
			price = Decimal(current['price'].strip("$u',").replace(",", ""))
			#print price
			# if price <= targetPrice and self.maxPrice > (self.totalSpent + price):
			if (price < targetHigh) and price > targetLow and self.maxPrice > (self.totalSpent + price):
				if current['productId'] not in self.products:
					self.items.append(current)
					self.products.append(current['productId'])
					self.totalSpent += price
				# print current
					return True
			#else:
				#data.remove(current)
			self.counter -= 1
		return False

	def populateAll(self):
		data = self.getResultsFromAPI()
		tryValue = 0
		while self.itemCount > len(self.items):
			# print "ok"
			print tryValue
			tryValue += 1
			if self.populateOne(data) == False:
				
				if tryValue > 3:
					if len(self.items) > 0:
						self.totalSpent -= Decimal(self.items.pop()['price'].strip("$u',"))
						self.products.pop()
					tryValue = 0
				data = self.getResultsFromAPI()

			if (self.itemCount == len(self.items) and self.maxPrice > self.totalSpent + 5):
				self.totalSpent -= Decimal(self.items.pop()['price'].strip("$'u,"))
				self.products.pop()
				data = self.getResultsFromAPI()
				tryValue = 0
				# self.items = []
				# self.totalSpent = 0
			# return False

		return True
