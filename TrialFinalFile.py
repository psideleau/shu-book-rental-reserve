import json
import os
import flask
import random
from flask import jsonify
from flask import Flask
from flask import Flask, request, render_template


app = Flask(__name__)


class Student(object):
    def __init__(self, studentID=None, studentStatus=None):
        self.studentID = studentID
        self.studentStatus = studentStatus

class StudentRentalStatus(object):
    def __init__(self):
        self.StudentStatusList = []
        self.StudentStatusList.append(Student("1234567", "Deactivated"))
        self.StudentStatusList.append(Student("2345678", "Deactivated"))
        self.StudentStatusList.append(Student("3456789", "Active"))

    def CheckActive(self):
        deactivatedStudents = []
        for status in self.StudentStatusList:
            if status.studentStatus == "Deactivated":
                deactivatedStudents.append(status.studentID)
        return deactivatedStudents
    def checkStudents(self):
        activeStuds = []
        for status in self.StudentStatusList:
            if status.studentStatus == "Active":
                activeStuds.append(status.studentID)
        return activeStuds
    def IDconfirm(self):
        for num in self.StudentStatusList:
            if num.studentID == "3456789":
                return ("confirmed")
                                      
class Randomizer(object):
    def getcode(self):
        randoNum = str(random.randrange(100000,999999))
        return (randoNum)

class Book(object):

    def __init__(self, bookname=None, author=None, ISBN=None, Availability=None, StudentID=None):
        self.bookname = bookname
        self.author = author
        self.ISBN = ISBN
        self.Availability = Availability
        self.StudentID = StudentID
        
class BookRepository(object):
    def __init__(self):
        
        self.BookList = []
        self.BookList.append(Book("Clean Architecture", "Robert Martin", "978-0134494166", "Rented", "1234567"))
        self.BookList.append(Book("Cryptography and Network Security", "William Stallings", "978-93-325-8522-5", "Available", "0000000"))
        self.BookList.append(Book("Fundamentals of Information Systems Security", "David Kim", "978-1-284-11645-8", "Available", "0000000"))
        self.BookList.append(Book("College Writing Skills", "John Langan", "978-1259988547", "Rented", "2345678"))
        self.BookList.append(Book("Campbell Biology", "Lisa A. Urry", "978-0134093413", "Available", "0000000"))
        self.BookList.append(Book("A Book", "An Author", "1000", "Rented", "3456789"))

        import operator
        self.BookList.sort(key=operator.attrgetter('ISBN'))

    #def wantedBook(self, StudentID):
        #selected = "A Book"
        #IDselect = "3456789"
        #for want in self.BookList:
            #if StudentID != want.StudentID and selected == want.bookname:
                #want.StudentID.replace(IDselect)
        #return (want.BookList)
        

    def lookUp(self, ISBN):
        for libBook in self.BookList:
            if ISBN in libBook.ISBN:
                return ("Your selected book is: Title - %s, Author - %s, ISBN - %s, Status - %s" % (libBook.bookname.title(), libBook.author, libBook.ISBN, libBook.Availability))
        return ("Not found")

    def checkUp(self):
        inActiveStudents = StudentRentalStatus().CheckActive()
        
        StockList = []
        StockAuthor = []
        StockISBN = []
        StockAvail = []
        for avail in self.BookList:
            if avail.StudentID != inActiveStudents[0] and avail.StudentID != inActiveStudents[1]:
                StockList.append(avail.bookname.title())
                StockAuthor.append(avail.author)
                StockISBN.append(avail.ISBN)
                StockAvail.append(avail.Availability)
        return ('Here is the stock list: %s, %s, %s, %s' % (StockList, StockAuthor, StockISBN, StockAvail))
    
        #activeBooks = filter (deactivatedStudents, self.BookList)
        #return activeBooks
        

        
        #status = StudentRentalStatus().CheckActive(nonActive)
        #nonActive = nonActive
        #for check in self.BookList:
            #if StudentID != nonActive in check.StudentID:
                #return ("Here are the available books/books with active students: %s, %s, %s, %s" % (libBook.bookname.title(), libBook.author, libBook.ISBN, libBook.Availability))
        
  

@app.route('/available', methods=(['GET', 'POST']))
def ListAvailable():
    
    Stock = BookRepository().checkUp()
    
    return jsonify (Stock)


#def ListAvailable():
    #List = BookRepository().checkUp()

    #return jsonify (List)

    
@app.route('/search', methods=(['GET', 'POST']))
def CallClassSearch():
    ID = request.args['book']
    book = BookRepository().lookUp(ID)
    
    return jsonify (book)

#Pages below set up as fake two way authentication

#This page isn't meant to be seen by client and is used to test checking active students
@app.route('/active', methods=(['GET', 'POST']))
def can_rent():
    rentalStuds = str(StudentRentalStatus().checkStudents())
    return jsonify (rentalStuds)

#This page is the "technical" submitting ID number and getting it checked
@app.route('/confirmation',methods=(['GET', 'POST']))
def confirmID():
    confirmation = StudentRentalStatus().IDconfirm()
    if confirmation == "confirmed":
        return ("StudentID is active and confirmed")
    else:
        return ("Incorrect ID")

#This page represents the randomizing and submitting of random number
@app.route('/randoCode', methods=(['GET', 'POST']))
def confirmCode():
    newCode = Randomizer().getcode()
    enteredCode = newCode
    if enteredCode == newCode:
        return ("%s is the generated code. %s is the code you submitted. Move on to /rentalConfirmation" % (newCode,enteredCode))

#Final page http://127.0.0.1:5000/rentalConfirmation?select=1000
@app.route('/rentalConfirmation', methods=(['GET', 'POST']))
def confirmBook():
    #YourBook = str(BookRepository().wantedBook(BookList))
    Book = request.args['select']
    select = BookRepository().lookUp(Book)
    return jsonify ("Your book rental is confirmed. %s" % select)
    

#This page isn't meant to be seen by client and is used to test the randomizer
@app.route('/random', methods=(['GET', 'POST']))
def generate_code():
    randoNum = str(random.randrange(100000,999999))
    return jsonify (randoNum)



if __name__ == '__main__':
    app.run()
