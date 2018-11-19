import json
import os
import flask
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

    def CheckActive(self, studentStatus):
        for status in self.StudentStatusList:
            if studentStatus == "Deactivated" in status.studentStatus:
                return (status.studentID)
                                      

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
        self.BookList.append(Book("Clean Architecture", "Robert Martin", "978-0134494166", "Unavailable", "1234567"))
        self.BookList.append(Book("Cryptography and Network Security", "William Stallings", "978-93-325-8522-5", "Available"))
        self.BookList.append(Book("Fundamentals of Information Systems Security", "David Kim", "978-1-284-11645-8", "Available"))
        self.BookList.append(Book("College Writing Skills", "John Langan", "978-1259988547", "Unavailable", "2345678"))
        self.BookList.append(Book("Campbell Biology", "Lisa A. Urry", "978-0134093413", "Available"))
        self.BookList.append(Book("A Book", "An Author", "1000", "Unavailable", "3456789"))

        import operator
        self.BookList.sort(key=operator.attrgetter('ISBN'))
        

    def lookUp(self, ISBN):
        for libBook in self.BookList:
            if ISBN in libBook.ISBN:
                return ("Your selected book is: %s, %s, %s, %s" % (libBook.bookname.title(), libBook.author, libBook.ISBN, libBook.Availability))
        return ("Not found")

    def checkUp(self):
        activeBooks = filter (StudentRentalStatus().CheckActive(status), StudentID)
        return (activeBooks)

        
        #status = StudentRentalStatus().CheckActive(nonActive)
        #nonActive = nonActive
        #for check in self.BookList:
            #if StudentID != nonActive in check.StudentID:
                #return ("Here are the available books/books with active students: %s, %s, %s, %s" % (libBook.bookname.title(), libBook.author, libBook.ISBN, libBook.Availability))
        
  

@app.route('/available', methods=(['GET', 'POST']))
def ListAvailable():
    List = BookRepository().checkUp(status)

    return jsonify (List)

    
@app.route('/search', methods=(['GET', 'POST']))
def CallClassSearch():
    ID = request.args['book']
    book = BookRepository().lookUp(ID)
    
    return jsonify (book)

if __name__ == '__main__':
    app.run()
