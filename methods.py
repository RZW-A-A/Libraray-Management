class Book:
	def __init__(self, bookid, bookname, bookprice, bookauthor):
		self.__bookid=bookid
		self.__bookname=bookname
		self.__bookprice=bookprice
		self.__bookauthor=bookauthor

	def setbookid(self, bookid):
		self.__bookid=bookid
	def setbookname(self, bookname):
		self.__bookname=bookname
	def setbookprice(self, bookprice):
		self.__bookprice=bookprice
	def setbookauthor(self, bookauthor):
		self.__bookauthor=bookauthor

	def getbookid(self):
		return self.__bookid
	def getbookname(self):
		return self.__bookname
	def getbookprice(self):
		return self.__bookprice
	def getbookauthor(self):
		return self.__bookauthor
