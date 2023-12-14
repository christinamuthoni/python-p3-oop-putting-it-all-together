#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count

    def get_page_count(self):
        print("Retrieving page_count.")
        return self._page_count
    
    def get_title(self):
        print("Retrieving title.")
        return self._title

    def set_page_count(self, page_count):    
        if isinstance(page_count, int):
            print(f"Setting page_count to {page_count}.")
            self._page_count = page_count

        else:
            print('page_count must be an integer')

    def set_title(self, title):
        self._title = title        

    page_count =property(get_page_count, set_page_count) 
    title = property(get_title, set_title)   

    def turn_page(self):  
        print("Flipping the page...wow, you read fast!")
        

#my_book = Book("Sample Book", "800")
#my_book.page_count = "jjj"
#print(my_book.page_count)    

