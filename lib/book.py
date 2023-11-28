#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self._title=title
        self._page=page_count

    def set_page(self,page_count):
        if isinstance(page_count, int):
            self._page=page_count
        else:
            print("page_count must be an integer")
    def get_page(self)  :
        return self._page
    
    page_count=property(get_page,set_page)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        return "Flipping the page...wow, you read fast!"
    @property
    def title(self):
        return self._title