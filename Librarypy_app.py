# -*- coding: utf-8 -*-

class Library:
    __book_list = list()
    def __init__(self,book_list):
        self.__book_list=book_list  
    def print_library(self):
        print(self.__book_list)

        


class Book:
    def __init__(self,booktitle,bookid,checkout_date,return_date,is_returned):
        self.__booktitle=booktitle
        self.__bookid=bookid
        self.__checkout_date=checkout_date
        self.__return_date=return_date
        self.__is_returned=is_returned    
    def print_book_list(self):
        print(self.__booktitle, self.__bookid, self.__checkout_date, self.__return_date, self.__is_returned)




class Human:
    __book_list = list()
    def __init__(self,name,user_id):
        self.__name=name
        self.__user_id=user_id
    def print_human_list(self):
        print(self.__name, self.__user_id, self.__book_list)
    def add_book(self,book):
        self.__book_list.append(book)

book = Book('python','0001','2019/4/1','2019/4/8','return')
book.print_book_list()
book_list = list()
book_list.append(book)
library = Library(book_list)
library.print_library()
human = Human('山田太郎', '01')
human.print_human_list()






