from librarymgmt import Book
class Booklibrary:
	booklist = []
	def addbooks(self):
		print()
		print("***Enter Book detail***")
		print()
		bookid = int(input("1. Enter Book Id : "))
		bookname = input("2. Enter Book Name : ")
		bookprice = int(input("3. Enter Book Price : "))
		bookauthor = input("4. Enter Book Author : ")
		obj = Book(bookid, bookname, bookprice, bookauthor)
		self.booklist.append(obj)
		print()
	def displaybooks(self):
		print()
		print("***All Available Books***")
		print()
		for i in range(self.booklist.__len__()):
			if self.booklist[i] != 'null':
				print("1) Book Id :", self.booklist[i].getbookid())
				print("2) Book Name :", self.booklist[i].getbookname())
				print("3) Book Price : $", self.booklist[i].getbookprice())
				print("4) Book Author :", self.booklist[i].getbookauthor())
				print()
		print()
	def updatebooks(self):
		print()
		print("***Edit Book Detail Here***")
		print()
		n = int(input("(~) Enter Book Id For Update = "))
		for i in range(self.booklist.__len__()):
			if self.booklist[i].getbookid() == n:
				bname = input("1) Enter Book Name =")
				bprice = input("2) Enter Book Price =")	
				bauthor = input("3) Enter Book Author =")
				self.booklist[i].setbookname(bname)
				self.booklist[i].setbookprice(bprice)
				self.booklist[i].setbookauthor(bauthor)
		print()
	def deletebooks(self):
		print()
		print("***Remove Book From Library***")
		print()
		n = int(input("(~) Enter Book Id For Removing = "))
		for i in range(self.booklist.__len__()):
			if self.booklist[i].getbookid() == n:
				self.booklist[i] = 'null'
				print("Book Removed Successfully")
		print()


print("()*()*()*()WELCOME TO LIBRARY MANAGEMENT SYSTEM()*()*()*()")
print()
while True:
	print("~ To Add book Press 1")
	print("~ To Display book Press 2")
	print("~ To Update book Press 3")
	print("~ To Delete book Press 4")
	print("~ To Exit Library Press 5")
	print()
	ch = int(input("Enter your choice = "))

	b=Booklibrary()
	if ch == 1:
		b.addbooks()
	elif ch == 2:
		b.displaybooks()
	elif ch == 3:
		b.updatebooks()
	elif ch == 4:
		b.deletebooks()
	elif ch == 5:
		break
	else:
		print("Enter correct option")
