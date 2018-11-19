import json
import os
import flask
from flask import jsonify
from flask import Flask
from flask import Flask, request, render_template


app = Flask(__name__)




class Book(object):

    def __init__(self, bookname=None, author=None, ISBN=None, Availability=None):
        self.bookname = bookname
        self.author = author
        self.ISBN = ISBN
        self.Availability = Availability
        
        
class BookRepository(object):
    def __init__(self):
        
        self.BookList = []
        self.BookList.append(Book("Clean Architecture", "Robert Martin", "978-0134494166", "In-Stock"))
        self.BookList.append(Book("Cryptography and Network Security", "William Stallings", "978-93-325-8522-5", "In-Stock"))
        self.BookList.append(Book("Fundamentals of Information Systems Security", "David Kim", "978-1-284-11645-8", "In-Stock"))

        import operator
        self.BookList.sort(key=operator.attrgetter('ISBN'))

    def lookUp(self, ISBN):
        for libBook in self.BookList:
            if ISBN in libBook.ISBN:
                return ("Your selected book is: %s, %s, %s, %s" % (libBook.bookname.title(), libBook.author, libBook.ISBN, libBook.Availability))
        return ("Not found")

    
@app.route('/search', methods=(['GET', 'POST']))
def CallClassSearch():
    ID = request.args['book']
    book = BookRepository().lookUp(ID)
    
    return jsonify (book)

if __name__ == '__main__':
    app.run()
